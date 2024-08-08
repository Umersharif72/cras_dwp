# jobs/urls.py
from django.urls import path
from .views import run_etl_view, stop_etl_view, fetch_mappings,truncate_data_view

urlpatterns = [
    path('run_etl/', run_etl_view, name='run_etl'),
    path('stop_etl/', stop_etl_view, name='stop_etl'),
    path('fetch_mappings/', fetch_mappings, name='fetch_mappings'),
    path('truncate_data/', truncate_data_view, name='truncate_data'),
]

