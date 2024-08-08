from django.urls import path
from .import views

urlpatterns = [
     # path('home/', views.home, name='home'),
     path('landingpage/', views.landingpage, name='landingpage'),
     path('nvb/', views.nvb, name='navbar'),
     path('nvb/', views.nvb, name='navbar'),
     path('fp',  views.fp, name ='fpage'),
     path('nvb', views.nvb, name ='navbar'),
     path('lp_nvb', views.lpnvbr, name ='lpnavbar'),


     path('sourceConn/', views.fetch_SourceConn, name='fetch_sourceConn'),
     path('cappdb/', views.fetch_c_app_db, name='fetch_cappdb'),
     path('cemapng/', views.fetch_ce_mapng, name='cemapng'),
     path('table_extraction/', views.table_extraction, name='table_extraction'),
     path('juri_table/', views.get_unique_jurisdictions_tbextr, name='juri_table'),
     path('insert_record/', views.insert_record_c_extr_tables, name='insert_record'),
     path('dummy/', views.dummy, name='dummy'),

     
     path('juri_col/', views.get_unique_jurisdictions_colextr, name='juri_col'),
     path('columns_extraction/', views.columns_extraction, name='columns_extraction'),
     path('colums/',  views.colums, name = 'colums'),
     # path('manual_columns/',  views.manual_columns, name = 'manual_columns'),
     path('insert_record_c_extr_colls/', views.insert_record_c_extr_colls, name='insert_record_c_extr_colls'),

     path('adjustment_screen/', views.adjustment_screen, name='adjustment_screen')
]