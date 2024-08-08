from django.shortcuts import render
from .models import EntityAdjustment
from django.http import JsonResponse
from .models import EJE
from django.shortcuts import render, redirect
from django.db import connection

# Create your views here.

def anything(request):
    return render(request, 'Main/landingpage.html')

def clstr_options(request):
    return render(request, 'Main/landingpage.html')



def aje_records(request):
    if request.method == 'POST':
        aje_number = request.POST.get('aje_number')
        request.session['aje_number'] = aje_number
        return redirect('get_aje_records')

    with connection.cursor() as cursor:
        cursor.execute("SELECT DISTINCT AJE_Number, Description FROM EJE")
        aa = [str(row[0]) + " " + row[1] for row in cursor.fetchall()]  # Extracting only the first element from each tuple
    return render(request, 'Main/landingpage.html', {'aa': aa,  'adj':'ok'})

def get_aje_records(request):
    # Retrieve the aje_number from the session
    aje_number = request.session.get('aje_number')
    aje_number = int(aje_number[0])
    
    if not aje_number:
        return redirect('xyz')  # Redirect to the main page if aje_number is not in session
    
    # Fetch records based on the aje_number from the session
    with connection.cursor() as cursor:
        cursor.execute("SELECT TOP 2 * FROM EJE WHERE aje_number = %s", [aje_number])
        aje_records = cursor.fetchall()

    return render(request, 'Main/landingpage.html', {'aje_records': aje_records, 'adj':'ok'})






def unique_clusters(request):
    selected_cluster = None
    if request.method == 'POST':
        selected_cluster = request.POST.get('cluster', '')
        # Handle the selected cluster if necessary
        return redirect('unique_company_types')  # Redirect after POST if needed

    # Fetch unique cluster values, ignoring nulls
    unique_clusters = EntityAdjustment.objects.all().values_list('cluster', flat=True).distinct()
    return render(request, 'Main/landingpage.html', {
        'unique_clusters': unique_clusters,
        'selected_cluster': selected_cluster
    })



def company_types(request):
    # Query to get unique company_type values
    unique_types = EntityAdjustment.objects.all().values_list('CompanyType', flat=True).distinct()
    
    # Convert the QuerySet to a list
  
    
    # Render the template with the unique values
    return render(request, 'Main/landingpage.html', {'company_types': unique_types})
