import pyodbc
import time
import logging

from django.core.management.base import BaseCommand
from jobs.utils import connect_to_sql_server, execute_query

logging.basicConfig(filename='job_execution.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

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

class Command(BaseCommand):
    help = 'Run ETL jobs'
    
    def add_arguments(self, parser):
        parser.add_argument('jurisdiction', nargs='?', type=str, help='Jurisdiction to run ETL jobs for')
        # Add the 'mapping' argument, which is optional and should be passed if provided
        parser.add_argument('--mapping', type=str,default=None, help='Optional mapping to run ETL jobs for')

    def handle(self, *args, **kwargs):
        
        jurisdiction = kwargs['jurisdiction']
        
        mapping = kwargs['mapping']
        
        print("This is jurisdiction:", jurisdiction)
        print("this is mapping", mapping)
        try:
            server = '10.254.19.7'
            database = 'cras'
            username = 'sa'
            password = 'sa-1234'

            conn = connect_to_sql_server(server, database, username, password)
            if conn:
                logging.info("Connected to SQL Server.")
                
                if(mapping):

                    # Query to get the list of jobs
                    mapping_name  = convert_string(mapping)
                    query = "SELECT CONCAT(Jusrisdiction, ' ', mapng_nm) AS jb FROM ce_mapng WHERE Jusrisdiction = ? and tgt_tblnm = ?;"
                    jobs = execute_query(conn, query, (jurisdiction,mapping_name,))
                    print("jahhdkskjd")
                    logging.info("Fetched job list: %s", jobs)
                else:
                    # Query to get the list of jobs
                    query = "SELECT CONCAT(Jusrisdiction, ' ', mapng_nm) AS jb FROM ce_mapng WHERE Jusrisdiction = ?;"
                    jobs = execute_query(conn, query, (jurisdiction,))
                    logging.info("Fetched job list: %s", jobs)
                total_records_processed = 0
                print(jobs,"ssdsdsds")
                for job in jobs:
                    print("fdsfsdsdfdsfsdfffdfsfffffffffffffffffffffffffffffffffff")
                    jb = job[0]
                    loc_id, mapping_name = jb.split(' ', 1)
                    print(loc_id,mapping_name)

                    logging.info(f"Calling ETL job for {loc_id} with mapping name '{mapping_name}'...")
                    total_records_processed += call_etl_job(loc_id, mapping_name, server, database, username, password)

                    # Sleep for a while to allow the previous job to finish
                    time.sleep(10)

                logging.info(f"All jobs executed successfully. Total records processed: {total_records_processed}")
                print("Total records processed:", total_records_processed)
                #job_status["records_processed"] = total_records_processed  # Update job status
                return str(total_records_processed)
        except pyodbc.Error as e:
            logging.error(f"SQL Server Error: {e}")
        except Exception as e:
            logging.error(f"Error: {e}")

def call_etl_job(loc_id, mapping_name, server, database, username, password):
    try:
        records_processed = etl_main(loc_id, mapping_name, server, database, username, password)
        logging.info(f"ETL job for {loc_id} with mapping name '{mapping_name}' executed successfully. Records processed: {records_processed}")
        return records_processed
    except Exception as e:
        logging.error(f"Error executing ETL job for {loc_id} with mapping name '{mapping_name}': {e}")
        return 0



def etl_main(loc_id, mapping_name, server, database, username, password):
    records_processed = 0

    try:
        start_time = time.time()  # Record start time
        conn = connect_to_sql_server(server, database, username, password)
        if conn:
            logging.info("Connected to SQL Server for ETL job.")

            query = """
            SELECT  Src_HOST, 
                    Src_DB_NAME, 
                    Src_USER_NAME, 
                    Src_PASSWRD,
                    mpngtxt,
                    tgt_tblnm,
                    tgt_tblcols
            FROM SourceConn s, ce_mapng cm
            WHERE s.Jurisdiction = cm.Jusrisdiction AND s.Jurisdiction = ? AND cm.mapng_nm = ?
            """
            connection_info = execute_query(conn, query, (loc_id, mapping_name))
            logging.info(f"Connection info: {connection_info}")  # Debug log
            
            if connection_info:
                # Extract connection information
                hst, dse, user, passw, srcq, tgttb, tgtcols = connection_info[0]
                
                # Connect to the source database
                Src_conn = connect_to_sql_server(hst, dse, user, passw)
                if Src_conn:
                    logging.info("Connected to source SQL Server.")
                    
                    # Execute the source query
                    srcqry = execute_query(Src_conn, srcq)
                    logging.info(f"Source Query result: {srcqry}")  # Debug log    
                                    
                    # Prepare INSERT query for SQL Server
                    insert_query = f"""
                    INSERT INTO {tgttb} ({tgtcols})
                    VALUES ({', '.join(['?' for _ in tgtcols.split(',')])})
                    """
                    
                    # Insert data into target database
                    cursor = conn.cursor()
                    for i, row in enumerate(srcqry, start=1):
                        logging.info(f"Inserting row: {row}")
                        cursor.execute(insert_query, row)
                        records_processed += 1  # Update records processed counter
                    
                    conn.commit()
                    
                    
                    
                    

                    logging.info("Data inserted successfully.")
            else:
                logging.info("No connection information found for the given inputs.")
    except pyodbc.Error as e:
        logging.error(f"Failed to execute the query: {e}")
    except Exception as e:
        logging.error(f"Error in ETL main process: {e}")
    
    return records_processed  # Return the count of records processed
