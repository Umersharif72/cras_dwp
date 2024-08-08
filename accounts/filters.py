# filters.py
import django_filters
from .models import UserDetail

class UserDetailFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    role = django_filters.ChoiceFilter(choices=UserDetail.ROLE_CHOICES)
    department = django_filters.ChoiceFilter(choices=UserDetail.DEPARTMENT_CHOICES)
    permissions = django_filters.ChoiceFilter(choices=UserDetail.PERMISSION_CHOICES)

    class Meta:
        model = UserDetail
        fields = ['name', 'email', 'role', 'department', 'permissions']
