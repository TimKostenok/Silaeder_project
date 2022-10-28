from email import message
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import RegisterForm, ProjectForm, LoginForm
from django import urls
from .auth import authenticate
from django.contrib import auth
from django.contrib.auth import logout, login
from .models import SUser, Project

def check_user(request):
    if request.user == None:
        return True
    return False
    

def register(request):
    message = 'Signing up'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password2']:
                try:
                    user = SUser.objects.create_user(
                        form.cleaned_data['username'],
                        form.cleaned_data['email'],
                        form.cleaned_data['password'],
                        form.cleaned_data['first_name'],
                        form.cleaned_data['last_name']
                    )
                    user.save()
                    login(request, user)
                    return redirect('main_page')
                except IntegrityError as e:
                    message = 'User with your username already exists'
            else:
                message = 'Passwords doesn\'t match'
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form, 'message': message})

def login_view(request):
    message = 'Login'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('main_page')
            else:
                message = 'Invalid username or password'
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form, 'message': message})

#@login_required(redirect_field_name='')
def logout_view(request):
    if not check_user:
        return redirect('main_page')
    if (request.method == 'POST'):
        if request.POST.get('Yes') != None:
            auth.logout(request)
            return redirect('login')
        else:
            return redirect('main_page')
    else:
        return render(request, 'main/logout.html', {'username': request.user.username})

#@login_required(redirect_field_name='')
def new_project(request):
    if not check_user:
        return redirect('main_page')
    text_ = 'New project'
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        print(form.data)
        print(request.FILES.get('icon'))
        if form.is_valid():
            users = []
            prj_icon = request.FILES.get('icon')
            prj_name = form.cleaned_data['project_name']
            prj_sc_dir = form.cleaned_data['sc_dir']
            prj_short_desc = form.cleaned_data['short_desc']
            prj_full_desc = form.cleaned_data['full_desc']
            prj = Project(project_name=prj_name, sc_dir=prj_sc_dir, short_desc=prj_short_desc, full_desc=prj_full_desc, icon=prj_icon)
            prj.save()
            for username in form.cleaned_data['author'].replace(' ', '').split(','):
                try:
                    users.append(SUser.objects.get(username=username))
                except SUser.DoesNotExist:
                    text_ = f'User {username} does not exists'
            prj.save()
        else:
            text_ = 'Please, fill the from correctly!'
            form = ProjectForm()
    else:
        form = ProjectForm()
    return render(request, 'main/new_project.html', {'form': form, 'text_': text_})

def main_page(request):
    return render(request, 'main/main_page.html', {'Projects': Project.objects.all()})