from django.urls import path
from . import views

urlpatterns = [
    path('login', views.user_login, name='login'), 
    path('', views.homepage, name="homepage"),
    path('logout', views.logout_button, name="logout_button"),
    path('admin_interface', views.admin_interface, name='admin_interface'),
    path('create', views.create, name='create'),
    path('view', views.user_list, name='view'),
    path('update_or_delete', views.update_or_delete, name='update_or_delete_users'),
    path('permission_history', views.view_user_activity_logs, name='useractivity')
]