from django.shortcuts import render
import pyodbc
from Extraction import settings
from .models import Record


def connect_to_ru_server():
    server = settings.DATABASES['Ru']['HOST']
    database = settings.DATABASES['Ru']['NAME']
    username = settings.DATABASES['Ru']['USER']
    password = settings.DATABASES['Ru']['PASSWORD']
    port = settings.DATABASES['Ru']['PORT']
    
    try:
        connection = pyodbc.connect(
            f"DRIVER=ODBC Driver 17 for SQL Server;"
            f"SERVER={server},{port};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password};"
        )
        return connection
    except Exception as e:
        raise e

def PnLByEntity(request):
    try:
        connection = connect_to_ru_server()
        cursor = connection.cursor()
        query = """ SELECT * FROM IDS_DM.CRAS.PnLByEntity"""
        cursor.execute(query)
        data = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        rows = [dict(zip(columns, row)) for row in data]
        context = {
            'rows': rows,
            
        }
    except Exception as error:
        context = {
            'error_message': f"Error while fetching data from SQL Server: {error}",
        }
    finally:
        if connection:
            cursor.close()
            connection.close()
    return render(request, 'Main/landingpage.html', context)


def ru_cluster_opt(request):
    return render(request, 'Main/landingpage.html')