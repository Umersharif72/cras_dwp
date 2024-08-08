# myapp/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password

class UsersManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=150)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False)

    objects = UsersManager()

    USERNAME_FIELD = 'username'

    # Specify related_name to avoid clashes
    groups = models.ManyToManyField(Group, related_name='user_accounts', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_accounts', blank=True)

    class Meta:
        managed = False
        db_table = 'Users'

class UserDetailManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class UserDetail(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('User', 'User'),
        ('Manager', 'Manager'),
    ]
    
    DEPARTMENT_CHOICES = [
        ('HR', 'Human Resources'),
        ('IT', 'Information Technology'),
        ('Finance', 'Finance'),
    ]
    
    PERMISSION_CHOICES = [
        ('read', 'Read'),
        ('write', 'Write'),
        ('execute', 'Execute'),
    ]
    
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    entity_name = models.CharField(max_length=100)
    cluster_name = models.CharField(max_length=100)
    part_of_group_reporting = models.BooleanField(default=False)
    permissions = models.CharField(max_length=10, choices=PERMISSION_CHOICES, default='read')
    password = models.CharField(max_length=128, default='PLACEHOLDER_DEFAULT_PASSWORD')
    activation_date = models.DateTimeField(default=timezone.now)
    activation_end_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default=1)
    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'UserDetail'

    objects = UserDetailManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return self.name
    
class Userpermissionlog(models.Model):
    email = models.CharField(max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    permissions = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserPermissionLog'
