from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
import pyodbc
import logging
logger = logging.getLogger(__name__)
from django.db import connection
import logging
import os
from .models import SourceConn, c_app_db, ce_mapng, c_extr_table_cols, c_extr_tables
from .forms import SourceConnForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password


def admin_check(user):
    return user.is_authenticated and user.is_superuser

# def home(request):
#     return render(request, 'Main/landingpage.html', {'home': "Ok"})

def admin_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if not admin_check(request.user):
            messages.error(request, 'Only admins can access this page.')
            return redirect('landingpage')  # Replace 'admin_only_page' with your URL name
        return view_func(request, *args, **kwargs)
    return wrapped_view

def landingpage(request):
    return render(request, 'Main/landingpage.html', {'home': "Ok"})

def dummy(request):
    return render(request, 'sources/dummy.html')

def nvb(request):
    return render(request, 'Main/navbar.html')

def fp(request):
    return render(request, 'Main/first_page.html')

def lpnvbr(request):
    return render(request, 'Main/lp_nvb.html')

def connect_to_sql_server():
    try:
        # Get database connection settings from Django settings
        server = settings.DATABASES['default']['HOST']
        database = settings.DATABASES['default']['NAME']
        username = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        
        # Construct the connection string
        conn_str = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}'
        
        # Connect to the SQL Server
        conn = pyodbc.connect(conn_str)
        
        # Create a cursor
        cursor = conn.cursor()
        
        # Execute a query
        cursor.execute('SELECT * FROM dbo.employees')
        
        # Fetch and return data
        data = cursor.fetchall()
        
        # Close the connection
        conn.close()
        
        # Return data
        return data
        
    except pyodbc.Error as e:
        # If an error occurs, return None or any other appropriate value indicating failure
        return None
    

def fetch_SourceConn(request):
    
    if request.method == 'POST':
        if "add_connection" in request.POST:
                
            # Retrieve form data from POST request
            jurisdiction = request.POST.get('Jurisdiction')
            databases = request.POST.get('DATABASES')
            src_db_name = request.POST.get('Src_DB_NAME')
            src_user_name = request.POST.get('Src_USER_NAME')
            src_passwd = request.POST.get('Src_PASSWRD')
            src_host = request.POST.get('Src_HOST')
            src_port = request.POST.get('Src_PORT')
            # Create a new SourceConn instance and save it
            SourceConn.objects.create(
                Jurisdiction=jurisdiction,
                DATABASES=databases,
                Src_DB_NAME=src_db_name,
                Src_USER_NAME=src_user_name,
                Src_PASSWRD=src_passwd,
                Src_HOST=src_host,
                Src_PORT=src_port
            )
            # Redirect to the same page after adding the record
            return redirect('fetch_sourceConn')
        
        elif "delete" in request.POST:
            sid = request.POST.get('SID')
            if sid:
                source_conn = SourceConn.objects.get(SID=sid)
                source_conn.delete()
                return redirect('fetch_sourceConn')
        
        elif "edit" in request.POST: 
            sid = request.POST.get('SID')
            if sid:
                source_conn = SourceConn.objects.get(SID=sid)
                
                # Update fields with new values
                source_conn.Jurisdiction = request.POST.get('new_jurisdiction')
                source_conn.DATABASES = request.POST.get('new_databases')
                source_conn.Src_DB_NAME = request.POST.get('new_src_db_name')
                source_conn.Src_USER_NAME = request.POST.get('new_src_user_name')
                source_conn.Src_PASSWRD = request.POST.get('new_src_passwd')
                source_conn.Src_HOST = request.POST.get('new_src_host')
                source_conn.Src_PORT = request.POST.get('new_src_port')
                
                # Save the updated object
                source_conn.save()

                return redirect('fetch_sourceConn')
            return redirect('fetch_sourceConn')

    else:
        records = SourceConn.objects.all()
        for objects in records:
            objects.Src_PASSWRD = make_password(objects.Src_PASSWRD)
        return render(request, 'Main/landingpage.html', {'records': records})



def fetch_c_app_db(request):
    if request.method == 'POST':
        Apps = request.POST.get('Apps')
        DB_name = request.POST.get('DB_name')

        c_app_db.objects.create(Apps=Apps, DB_name=DB_name )
        return redirect('fetch_cappdb')
    # Query all records from the SourceConn table
    else:
        records = c_app_db.objects.all()
        return render(request, 'Main/landingpage.html', {'records': records}) 
    
def fetch_ce_mapng(request):
    records = ce_mapng.objects.all()
    return render(request, 'Main/landingpage.html', {'records': records}) 



# -----------------------------Functionalities forSource Tables -------------------------------------
# ----------------------------------------------------------------------------------------------------

from django.http import JsonResponse


# @admin_required
def get_unique_jurisdictions_tbextr(request):
    if request.method == 'POST':
        from django.db import connection

        selected_jurisdiction = request.POST.get('jurisdiction')
        request.session['selected_jurisdiction'] = selected_jurisdiction
        print(selected_jurisdiction, 'here is ajax response')
        print(selected_jurisdiction, 'post here')
        return redirect('table_extraction')

    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT DISTINCT Jurisdiction FROM SourceConn")
        juri = [row[0] for row in cursor.fetchall()]

    return render(request, 'Main/landingpage.html', {'juriss': juri, 'table_display':"OK"})


def table_extraction(request):
    # Retrieve the selected jurisdiction from the session
    selected_jurisdiction = request.session.get('selected_jurisdiction')
    print(selected_jurisdiction, '333333')
    # Define the directory to look for files
    directory = 'C:\Tools'
    
    # Try to get the list of files in the specified directory
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    except Exception as e:
        files = []

    # Redirect to 'juri_table' if no jurisdiction is selected
    if not selected_jurisdiction:
        return redirect('juri_table')

    # Fetch the source connection details for the selected jurisdiction
    try:
        source_conn_details = SourceConn.objects.get(Jurisdiction=selected_jurisdiction)
    except SourceConn.DoesNotExist:
        return redirect('juri_table')

    # Construct the connection string for the database
    conn_str = (
        f"DRIVER=ODBC Driver 17 for SQL Server;"
        f"SERVER={source_conn_details.Src_HOST};"
        f"DATABASE={source_conn_details.Src_DB_NAME};"
        f"UID={source_conn_details.Src_USER_NAME};"
        f"PWD={source_conn_details.Src_PASSWRD};"
        f"PORT={source_conn_details.Src_PORT}"
    )
    
    # Establish a connection to the database
    connection = pyodbc.connect(conn_str)
    cursor = connection.cursor()
    
    # Execute the query to get the list of tables
    cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = 'dbo'")
    tables = [row.TABLE_NAME for row in cursor.fetchall()]

    # Handle form submission
    if request.method == 'POST':
        src_type = request.POST.get('actionCol')
        if src_type == 'tables':
            tables_selected = request.POST.getlist('tables[]')
            src_tables = ', '.join([f"'{table}'" for table in tables_selected])
        elif src_type == 'api':
            tables_selected = request.POST.get('tablesCol[]')
            src_tables = f"'{tables_selected}'"
        elif src_type == 'file':
            # Extract file names only (without uploading files)
            tables_selected = request.FILES.getlist('fileclls[]')
            file_names = [file.name for file in tables_selected]
            print(file_names)
            src_tables = ', '.join([f"'{file}'" for file in tables_selected])
        
        # Store connection details and selected tables in the session
        request.session['source_conn_details'] = {
            'Src_HOST': source_conn_details.Src_HOST,
            'Src_DB_NAME': source_conn_details.Src_DB_NAME,
            'Src_USER_NAME': source_conn_details.Src_USER_NAME,
            'Src_PASSWRD': source_conn_details.Src_PASSWRD,
            'Src_PORT': source_conn_details.Src_PORT,
            'DATABASES': source_conn_details.DATABASES,
        }
        request.session['src_type'] = src_type
        request.session['tables_selected'] = tables_selected
        request.session['src_tables'] = src_tables
        # print(tables, 'here are tables')
        # Redirect to the insert_record view after form submission
        return redirect('insert_record')

    # Render the template with the retrieved data
    return render(request, 'Main/landingpage.html', {
        'selected_jurisdiction': selected_jurisdiction,
        'tabless': tables,
        'files': files,
        'table_display': "OK"
    })


def insert_record_c_extr_tables(request):
    selected_jurisdiction = request.session.get('selected_jurisdiction')
    source_conn_details = request.session.get('source_conn_details')
    src_type = request.session.get('src_type')
    src_tables = request.session.get('src_tables')

    if not all([selected_jurisdiction, source_conn_details, src_type, src_tables]):
        return HttpResponse("Missing or invalid session data")

    c_extr_table = c_extr_tables(
        Jurisdiction=selected_jurisdiction,
        AcctSytesm=source_conn_details.get('DATABASES'),
        Src_Host=source_conn_details.get('Src_HOST'),
        Src_DB_Name=source_conn_details.get('Src_DB_NAME'),
        Src_Port=source_conn_details.get('Src_PORT'),
        Src_Tables=src_tables,
        src_type=src_type,
    )

    try:
        c_extr_table.save()
        request.session.clear()
        return redirect("table_extraction")
    except Exception as e:
        return HttpResponse(f"Error saving record: {e}")



# -----------------------------Functionalities for source columns -------------------------------------
# ----------------------------------------------------------------------------------------------------
def get_unique_jurisdictions_colextr(request):
        if request.method == 'POST':
            from django.db import connection
            
                
            selected_jurisdiction = request.POST.get('jurisdictionCol')
            request.session['selected_jurisdiction'] = selected_jurisdiction

            print(selected_jurisdiction, 'post here')
            return redirect('columns_extraction')
        from django.db import connection
        with connection.cursor() as cursor:
                cursor.execute("SELECT DISTINCT Jurisdiction FROM SourceConn")
                juri = [row[0] for row in cursor.fetchall()]
                selected_jurisdiction = request.POST.get('jurisdictionCol')
                request.session['selected_jurisdiction'] = selected_jurisdiction
        return render(request, 'Main/landingpage.html', {'juri': juri, 'column_display':"OK"})

def columns_extraction(request):
    if request.method == 'POST':
        selected_jurisdiction = request.session.get('selected_jurisdiction')
        try:
            source_conn_details = SourceConn.objects.get(Jurisdiction=selected_jurisdiction)
        except SourceConn.DoesNotExist:
            return render(request, 'Main/landingpage.html', {'jurisdictions': selected_jurisdiction})

        source_conn_dict = {
            'Src_HOST': source_conn_details.Src_HOST,
            'Src_DB_NAME': source_conn_details.Src_DB_NAME,
            'Src_USER_NAME': source_conn_details.Src_USER_NAME,
            'Src_PASSWRD': source_conn_details.Src_PASSWRD,
            'Src_PORT': source_conn_details.Src_PORT,
            'DATABASES': source_conn_details.DATABASES
        }
        request.session['source_conn_details'] = source_conn_dict
        src_type = request.POST.get('actionCol')

        with connection.cursor() as cursor:
            cursor.execute(f"""
                SELECT Src_Tables 
                FROM c_extr_tables 
                WHERE Jurisdiction = %s 
                AND Src_type = %s
            """, [selected_jurisdiction, src_type])
            result = cursor.fetchone()

            if result:
                tables_string = result[0]  # Assuming the table names are in the first column
                tables = [table.strip("'") for table in tables_string.split(', ')]
            else:
                tables = []  # Handle the case where no tables are found

        request.session['tables'] = tables
        tableclls = request.POST.get('tableclls')
        request.session['tableclls'] = tableclls
        tables_colls = request.POST.getlist('columns[]')
        request.session['src_type'] = src_type
        request.session['tables_colls'] = tables_colls
        src_colmns = ', '.join([f"'{table}'" for table in tables_colls])
        request.session['src_colmns'] = src_colmns

        conn_str = f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={source_conn_details.Src_HOST};DATABASE={source_conn_details.Src_DB_NAME};UID={source_conn_details.Src_USER_NAME};PWD={source_conn_details.Src_PASSWRD};PORT={source_conn_details.Src_PORT}"
        connectionn = pyodbc.connect(conn_str)
        cursor = connectionn.cursor()
        cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{tableclls}'")
        columns = [row.COLUMN_NAME for row in cursor.fetchall()]
        request.session['columns'] = columns

        return redirect('colums')

    selected_jurisdiction = request.session.get('selected_jurisdiction')
    try:
        source_conn_details = SourceConn.objects.get(Jurisdiction=selected_jurisdiction)
    except SourceConn.DoesNotExist:
        return render(request, 'Main/landingpage.html', {'jurisdictions': selected_jurisdiction})

    source_conn_dict = {
        'Src_HOST': source_conn_details.Src_HOST,
        'Src_DB_NAME': source_conn_details.Src_DB_NAME,
        'Src_USER_NAME': source_conn_details.Src_USER_NAME,
        'Src_PASSWRD': source_conn_details.Src_PASSWRD,
        'Src_PORT': source_conn_details.Src_PORT,
        'DATABASES': source_conn_details.DATABASES
    }
    request.session['source_conn_details'] = source_conn_dict

    with connection.cursor() as cursor:
        cursor.execute(f"""
            SELECT Src_Tables 
            FROM c_extr_tables 
            WHERE Jurisdiction = %s
        """, [selected_jurisdiction])
        tables_string = [row[0] for row in cursor.fetchall()]
        tables = []
        for tables_str in tables_string:
            split_tables = tables_str.split(', ')
            tables.extend([table.strip("'") for table in split_tables])

    src_type = request.POST.get('actionCol')


    with connection.cursor() as cursor:
        cursor.execute(f"""
            SELECT Src_Tables 
            FROM c_extr_tables 
            WHERE Jurisdiction = %s 
            AND Src_type = 'file'
        """, [selected_jurisdiction])
        files_string = [row[0] for row in cursor.fetchall()]
        files = []
        for files_str in files_string:
            split_files = files_str.split(', ')
            files.extend([file.strip("'") for file in split_files])

    return render(request, 'Main/landingpage.html', {
        'selected_jurisdiction': selected_jurisdiction,
        'files': files,
        'tablescls': tables,
        'column_display':"OK"
    })



def colums(request):
    if request.method == 'POST':
        tables_colls = request.POST.getlist('columns[]')
        # Concatenate selected tables into a single string
        src_colmns = ', '.join([f"'{table}'" for table in tables_colls])
        request.session['src_colmns'] = src_colmns
        request.session['src_colmns'] = src_colmns
        return redirect ('insert_record_c_extr_colls')
    fetched_cols = request.session.get('columns')
    return render(request, 'Main/landingpage.html',{'fetched_cols':fetched_cols})

def insert_record_c_extr_colls(request):
    # Retrieve data from session
    selected_jurisdiction = request.session.get('selected_jurisdiction')
    source_conn_details = request.session.get('source_conn_details')
    src_type = request.session.get('src_type')
    table = request.session.get('tableclls')
    src_colmns = request.session.get('src_colmns')

    # Validate session data
    if not all([selected_jurisdiction, source_conn_details, src_type,table]):
        logger.error("Missing or invalid session data")
        # Handle the error appropriately, e.g., return an error response
        return HttpResponse("Missing or invalid session data")

    # Ensure that source_conn_details is a dictionary
    if not isinstance(source_conn_details, dict):
        logger.error("Invalid session data: source_conn_details is not a dictionary")
        return HttpResponse("Invalid session data")

    # Extract values from source_conn_details dictionary
    jurisdiction = selected_jurisdiction
    databases = source_conn_details.get('DATABASES')
    host = source_conn_details.get('Src_HOST')
    db_name = source_conn_details.get('Src_DB_NAME')
    port = source_conn_details.get('Src_PORT')

    # Save the data in the c_extr_tables table
    c_extr_table_colss = c_extr_table_cols(
        Jurisdiction=jurisdiction,
        AcctSytesm=databases,
        Src_Host=host,
        Src_DB_Name=db_name,
        Src_Port=port,
        Src_Table=table,
        Src_Columns = src_colmns,
        src_type=src_type
    )

    try:
        c_extr_table_colss.save()
        logger.info("Record saved successfully")
        # Optionally, clear the session data after processing
        request.session.clear()
        return redirect("juri_col")
    except Exception as e:
        logger.error(f"Error saving record: {e}")
        # Handle the error appropriately, e.g., return an error response
        return HttpResponse("Error saving record")
    


def adjustment_screen(request):
    return render(request, "Main/landingpage.html")