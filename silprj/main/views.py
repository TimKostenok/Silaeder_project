from django.db.utils import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import RegisterForm
from django import urls
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from .models import SUser

def index(request):
    return render(request, 'main/index.html', {'user': request.user})

def logout_view(request):
    logout(request) 
    return redirect('index')

def register(request):
    message = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid(): # TODO: add a repeat-password field
            try:
                user = SUser.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password'],
                    form.cleaned_data['first_name'],
                    form.cleaned_data['last_name']
                )
                user.save()
                return redirect('index')
            except IntegrityError as e:
                message = 'User with your username already exist'
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form, 'message': message})

def login_view(request):
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                message = 'Invalid username or password'
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form, 'message': message})