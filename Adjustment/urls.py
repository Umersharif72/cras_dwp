from django.urls import path
from .import views

urlpatterns = [
    path('xyz/', views.aje_records, name='xyz'),
    path('get_aje_records/', views.get_aje_records, name='get_aje_records'),
    path('anything/', views.anything, name='anythinga'),
    path('unique_clusters/', views.unique_clusters, name='unique_clusters'),
    path('unique_company_types/', views.company_types, name='unique_company_types'),

]

