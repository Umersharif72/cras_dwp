from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.management import call_command
from django.core.cache import cache
from django.utils import timezone
import datetime
import logging
from .models import *
import datetime
import pyodbc
from jobs.utils import connect_to_sql_server, execute_query

def convert_string(original_string):
    # Define the replacements
    prefix_replacement = {
        'C_EXTR_': 'CE_',
        'API_': ''  # Remove 'API_' part
    }
    
    # Start with the original string
    modified_string = original_string
    
    # Apply the replacements
    for old_prefix, new_prefix in prefix_replacement.items():
        if modified_string.startswith(old_prefix):
            modified_string = new_prefix + modified_string[len(old_prefix):]
    
    # Further remove specific parts if needed
    modified_string = modified_string.replace('API_', '')
    
    return modified_string

# Global variable to store the job status
job_status = {
    "job_name": "",
    "start_time": None,
    "end_time": None,
    "execution_time": None,
    "current_status": "Not started",
    "records_processed": 0  # Initialize records processed counter
}

# Flag to control job execution
STOP_JOB_FLAG = "stop_job_flag"
# Set up logging
logging.basicConfig(filename='job_execution.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def run_etl_view(request):
    jurisdictions = CeMapng.objects.values_list('jusrisdiction', flat=True).distinct()
    mapping = CeMapng.objects.values_list('mapng_nm', flat=True).distinct()
    
    if request.method == "POST":
        try:
            jurisdiction = request.POST.get('jurisdiction')  # Get selected jurisdiction from POST data
            mapping = request.POST.get('mapping')  # Get selected mapping from POST data
            print("this is mapping", mapping)
            if mapping:
                job_status["job_name"] = f"Specific table {mapping} from {jurisdiction} Jurisdiction"
            else:
                job_status["job_name"] = jurisdiction
            job_status["start_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            job_status["current_status"] = "Running"
            
            # Reset the stop flag
            cache.set(STOP_JOB_FLAG, False)

             # Call your management command 'etl' and pass jurisdiction and mapping (if provided)
            if mapping:
                records = call_command('etl', jurisdiction=jurisdiction, mapping=mapping)
                print("first ran")
            else:
                records = call_command('etl', jurisdiction=jurisdiction)
                print("second ran")

            job_status["end_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            job_status["execution_time"] = str(datetime.datetime.strptime(job_status["end_time"], "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(job_status["start_time"], "%Y-%m-%d %H:%M:%S"))
            job_status["current_status"] = "Completed"
            job_status["records_processed"] = records
            logging.info(f"Job '{jurisdiction}' completed successfully. Records processed: {records}")
            return render(request, 'Main/jobs/etl.html', {'status': 'ETL process started successfully.', 'jurisdictions': jurisdictions})
        except Exception as e:
            job_status["current_status"] = "Failed"
            logging.info(f"Job '{jurisdiction}' completed successfully. Records processed: {records}")
            return render(request, 'Main/jobs/etl.html', {'status': str(e), 'jurisdictions': jurisdictions})
    elif request.method == "GET" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse(job_status)
    return render(request, 'Main/jobs/etl.html', {'status': 'Invalid request method.', 'jurisdictions': jurisdictions, 'mappings': mapping})

def fetch_mappings(request):
    jurisdiction = request.GET.get('jurisdiction')
    mappings = CeMapng.objects.filter(jusrisdiction=jurisdiction).values_list('mapng_nm', flat=True).distinct()
    return JsonResponse({'mappings': list(mappings)})

def stop_etl_view(request):
    if request.method == "POST":
        # Set the flag to stop the job
        cache.set(STOP_JOB_FLAG, True)

        # Update job_status with "Job Killed" and clear other fields
        job_status.update({
            "job_name": "",
            "start_time": "",
            "end_time": "",
            "execution_time": "",
            "current_status": "Job Killed",
            "records_processed": 0  # Reset the records processed counter
        })
        return redirect('run_etl')
    return JsonResponse({"status": "Invalid request method."}, status=400)

def truncate_data_view(request):
    if request.method == "POST":
        jurisdiction = request.POST.get('jurisdiction')
        mapping = request.POST.get('mapping')
        #print(jurisdiction,mapping)
        try:
            server = '10.254.19.7'
            database = 'cras'
            username = 'sa'
            password = 'sa-1234'
            conn = connect_to_sql_server(server, database, username, password)

            if conn:
                cursor = conn.cursor()
                if mapping:
                    mapping = convert_string(mapping)
                    query = "SELECT tgt_tblnm AS jb FROM ce_mapng WHERE Jusrisdiction = ? and tgt_tblnm = ?;"
                    jobs = execute_query(conn,query, (jurisdiction, mapping,))
                else:
                    query = "SELECT tgt_tblnm AS jb FROM ce_mapng WHERE Jusrisdiction = ?;"
                    jobs = execute_query(conn,query, (jurisdiction,))
                
                for job in jobs:
                    
                    

                    query = f"TRUNCATE TABLE {job[0]}"
                    execute_query(conn,query)
                #convert_string('TB C_EXTR_TB_API_Purchases')
                conn.commit()
                return JsonResponse({'message': 'Data truncated successfully.'})
        except pyodbc.Error as e:
            return JsonResponse({'message': f'SQL Server Error: {e}'}, status=500)
        except Exception as e:
            return JsonResponse({'message': f'Error: {e}'}, status=500)

    return JsonResponse({'message': 'Invalid request method.'}, status=400)