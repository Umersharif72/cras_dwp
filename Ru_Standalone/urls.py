from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('table/', views.sql_server_data, name='sql_query_1'),
    path('table2/', views.sql_query_2, name='sql_query_2'),
    path('anything_ru', views.anything_ru, name='anything_ru'),
    path('highroad/', views.fetch_Highroad, name='highroad'),
    path('edw/', views.fetch_edw, name='edw'),
    path('edlab/', views.fetch_edl, name='edlab'),
    path('aquastar/', views.fetch_as, name='as'),
    path('mwb/', views.fetch_mwb, name='mwb'),
    path('bt/', views.fetch_bt, name='bt'),
    path('lkr/', views.fetch_lkr, name='lkr'),
    path('bel/', views.fetch_bel, name='bel'),
    path('ids/,', views.fetch_ids, name='ids'),
    path('ssp/,', views.fetch_ssp, name='ssp'),
    path('cwc/,', views.fetch_cwc, name='cwc'),
]
