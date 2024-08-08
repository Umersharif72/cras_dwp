# myapp/authentication.py

from django.contrib.auth.backends import ModelBackend
from .models import UserDetail

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserDetail.objects.get(email=username)
            if user.check_password(password):
                return user
        except UserDetail.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserDetail.objects.get(pk=user_id)
        except UserDetail.DoesNotExist:
            return None
