# myapp/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password'}),
    )

    is_admin = forms.BooleanField(label='Is Admin', required=False)

    class Meta:
        model = Users
        fields = ('username', 'password1', 'password2', 'is_admin')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Users.objects.filter(username=username).exists():
            raise ValidationError("A user with that username already exists.")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("The two password fields didn't match.")
        else:
            return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['is_admin']:
            user.is_superuser = True
        if commit:
            user.save()
        return user

# myapp/forms.py

# class LoginForm(AuthenticationForm):
#     name = forms.CharField(
#         max_length=150,
#         required=True,
#         widget=forms.TextInput(attrs={'placeholder': 'Name'}),
#     )
#     password = forms.CharField(
#         label="Password",
#         widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
#     )

#     def clean(self):
#         name = self.cleaned_data.get('name')
#         password = self.cleaned_data.get('password')

#         if not UserDetail.objects.filter(name=name).exists():
#             raise ValidationError("This username does not exist.")
#         return self.cleaned_data
    
class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if not UserDetail.objects.filter(email=email).exists():
            raise ValidationError("This email does not exist.")

        # Additional check for password if needed
        # UserDetail model handles password validation separately

        return cleaned_data

class UserDetailForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = UserDetail
        fields = ['name', 'email', 'role', 'department', 'entity_name', 'cluster_name', 'part_of_group_reporting', 'permissions']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data.get('password'):
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
        