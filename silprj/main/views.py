from re import S
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import RegisterForm

def index(request):    
    return render(request, 'main/index.html', {'Text': 'Igor is a teamlead'})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            user.save()
            return render(request, 'main/register.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})