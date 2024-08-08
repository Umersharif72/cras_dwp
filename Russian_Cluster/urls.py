from django.urls import path
from . import views

urlpatterns = [

    path('PnLByEntity/', views.PnLByEntity, name='PnLByEntity'),
    path('ru_cluster_opt/', views.ru_cluster_opt, name='ru_cluster_opt'),

]