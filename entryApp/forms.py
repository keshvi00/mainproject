from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUserr

class RegistrationForm(UserCreationForm):
    employee_id = forms.CharField(max_length=100)
    designation = forms.CharField(max_length=100)
    department = forms.CharField(max_length=100)

    class Meta:
        model = CustomUserr
        fields = ['username', 'employee_id', 'designation', 'department', 'password1', 'password2']

class LoginForm(forms.Form):
    employee_id = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())