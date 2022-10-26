import email
from email import message
from django.db.utils import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import RegisterForm
from django import urls
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import logout

def index(request):    
    return render(request, 'main/index.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    message = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid(): # TODO: add a repeat-password field
            try:
                print(form.cleaned_data)
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name']
                )
                user.save()
                return redirect('index')
            except IntegrityError as e:
                message = 'User with your username already exist'
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form, 'message': message})

def login(request):
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                return redirect('index')
            else:
                user = authenticate(email=form.cleaned_data['username'], password=form.cleaned_data['password'])
                if user is not None:
                    return redirect('index')
                else:
                    message = 'Invalid username or password'
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form, 'message': message})