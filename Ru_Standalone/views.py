# myapp/views.py

from django.shortcuts import render
import pyodbc
from django.conf import settings


def connection_details(query):
    connection = connect_to_ru_server()
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    rows = [dict(zip(columns, row)) for row in data]
    cursor.close()
    connection.close()
    return rows


def anything_ru(request):
    return render(request, 'Main/landingpage.html')

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

def sql_server_data(request):
    try:
        connection = connect_to_ru_server()
        cursor = connection.cursor()
        query = """
SELECT *
FROM 
(
    SELECT
        B.Code,
        B.[ItemID], 
        B.[Item],
        M.[FRP],
        B.[Entity], 
        E.BU,
        B.[Period], 
        B.[Value], 
        B.[Currency]
    FROM   IDS_DM.CRAS.BalanceFRP AS B
    LEFT JOIN IDS_DM.CRAS.IFRStoFRP AS M
        ON B.[ItemID] = M.[GLAccount]
    LEFT JOIN IDS_DM.CRAS.Entities AS E
        ON B.Entity = E.Entity
    WHERE
        B.[ReportType] = 'StandAlone'
        AND B.ItemID IS NOT NULL
        AND M.FRP IS NOT NULL
        AND M.FRP <> ''
        AND Period ='2024-05-01 00:00:00.000'
) src
PIVOT
(
    SUM(VALUE)
    FOR Entity IN ([HHL],[AS],[IDS],[SSP],[CWC],[EDW],[LKR],[BT],[KRZ],[MWB],[ELAB],[IDSBEL],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10])
) piv
ORDER BY 1 ASC
"""
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

def sql_query_2(request):
    try:
        connection = connect_to_ru_server()
        cursor = connection.cursor()
        query = """
select *
from 
(
 SELECT
b.Code,
	B.[ItemID], 
	B.[Note],
	M.[FRP],
	B.[Entity], 
	E.BU,
	B.[Period], 
	B.[Value], 
	B.[Currency]
FROM   IDS_DM.CRAS.BalanceFRP
  AS B
	LEFT JOIN IDS_DM.CRAS.IFRStoFRP
	AS M
	ON B.[ItemID] = M.[GLAccount]
	LEFT JOIN IDS_DM.CRAS.Entities
 AS E
	ON B.Entity = E.Entity
WHERE
	B.[ReportType] = 'StandAlone'
	AND
	B.ItemID IS NOT NULL
	and 
	M.FRP IS NOT NULL
	AND
	M.FRP <> ''
    AND Period ='2024-05-01 00:00:00.000'
) src
pivot
(
  sum(VALUE)
  for Entity in ([IDS],[AS],[SSP],[CWC],[EDW],[LKR],[BT],[KRZ],[MWB],[ELAB],[BYN],[IDSBEL])
                
) piv
order by 1  asc
"""
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

def fetch_Highroad(request):
    try:
        query = """ SELECT * FROM IDS_DM.CRAS.PnLByEntity where Entity = 'Highroad' """
        rows = connection_details(query)
        context = {
            'rows': rows,
        }
        print(context)
    except Exception as error:
        context = {
            'error_message': f"Error while fetching data from SQL Server: {error}",
        }
    return render(request, 'Main/landingpage.html', context)

def fetch_Highroad(request):
    try:
        query = """ SELECT * FROM IDS_DM.CRAS.PnLByEntity where Entity = 'Highroad' """
        rows = connection_details(query)
        context = {
            'rows': rows,
        }
        print(context)
    except Exception as error:
        context = {
            'error_message': f"Error while fetching data from SQL Server: {error}",
        }
    return render(request, 'Main/landingpage.html', context)

def fetch_edw(request):
    try:
        query = """ SELECT * FROM IDS_DM.CRAS.PnLByEntity where Entity = 'EDW' """
        rows = connection_details(query)
        context = {
            'rows': rows,
        }
        print(context)
    except Exception as error:
        context = {
            'error_message': f"Error while fetching data from SQL Server: {error}",
        }
    return render(request, 'Main/landingpage.html', context)

def fetch_edl(request):
    try:
        query = """ SELECT * FROM IDS_DM.CRAS.PnLByEntity where Entity = 'Elab' """
        rows = connection_details(query)
        context = {
            'rows': rows,
        }
        print(context)
    except Exception as error:
        context = {
            'error_message': f"Error while fetching data from SQL Server: {error}",
        }
    return render(request, 'Main/landingpage.html', context)

def fetch_as(request):
    try:
        query = """ SELECT * FROM IDS_DM.CRAS.PnLByEntity where Entity = 'AS' """
        rows = connection_details(query)
        context = {
            'rows': rows,
        }
    except Exception as error:
        context = {
            'error_message': f"Error while fetching data from SQL Server: {error}",
        }
    return render(request, 'Main/landingpage.html', context)

def fetch_mwb(request):
    try:
        query = """ SELECT * FROM IDS_DM.CRAS.PnLByEntity where Entity = 'MWB' """
        rows = connection_details(query)
        context = {
            'rows': rows,
        }
    except Exception as error:
        context = {
            'error_message': f"Error while fetching data from SQL Server: {error}",
        }
    return render(request, 'Main/landingpage.html', context)

def fetch_bt(request):
    try:
        query = """ SELECT * FROM IDS_DM.CRAS.PnLByEntity where Entity = 'BT' """
        rows = connection_details(query)
        context = {
            'rows': rows,
        }
    except Exception as error:
        context = {
            'error_message': f"Error while fetching data from SQL Server: {error}",
        }
    return render(request, 'Main/landingpage.html', context)

def fetch_lkr(request):
    try:
        query = """ SELECT * FROM IDS_DM.CRAS.PnLByEntity where Entity = 'LKR' """
        rows = connection_details(query)
        context = {
            'rows': rows,
        }
    except Exception as error:
        context = {
            'error_message': f"Error while fetching data from SQL Server: {error}",
        }
    return render(request, 'Main/landingpage.html', context)

def fetch_bel(request):
    try:
        query = """ SELECT * FROM IDS_DM.CRAS.PnLByEntity where Entity = 'Belarus' """
        rows = connection_details(query)
        context = {
            'rows': rows,
        }
    except Exception as error:
        context = {
            'error_message': f"Error while fetching data from SQL Server: {error}",
        }
    return render(request, 'Main/landingpage.html', context)

def fetch_ids(request):
    try:
        query = """ SELECT * FROM IDS_DM.CRAS.PnLByEntity where Entity = 'IDS' """
        rows = connection_details(query)
        context = {
            'rows': rows,
        }
    except Exception as error:
        context = {
            'error_message': f"Error while fetching data from SQL Server: {error}",
        }
    return render(request, 'Main/landingpage.html', context)

def fetch_ssp(request):
    try:
        query = """ SELECT * FROM IDS_DM.CRAS.PnLByEntity where Entity = 'SSP' """
        rows = connection_details(query)
        context = {
            'rows': rows,
        }
    except Exception as error:
        context = {
            'error_message': f"Error while fetching data from SQL Server: {error}",
        }
    return render(request, 'Main/landingpage.html', context)

def fetch_cwc(request):
    try:
        query = """ SELECT * FROM IDS_DM.CRAS.PnLByEntity where Entity = 'CWC' """
        rows = connection_details(query)
        context = {
            'rows': rows,
        }
    except Exception as error:
        context = {
            'error_message': f"Error while fetching data from SQL Server: {error}",
        }
    return render(request, 'Main/landingpage.html', context)