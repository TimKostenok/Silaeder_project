from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(max_length=128)

class ProjectForm(forms.Form):
    project_name = forms.CharField(max_length=63)
    # Autor of project. Will it be like list?
    autor = forms.CharField(max_length=255)
    # Science director. Will it be like list?
    sc_dir = forms.CharField(max_length=255)
    #year_of_creating = forms.DateField()
    secion = forms.CharField(max_length=1)
    short_desc = forms.CharField(max_length=511)
    full_desc = forms.CharField(max_length=4095)
    icon = forms.FileField()