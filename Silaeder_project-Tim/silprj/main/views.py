from re import S
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import RegisterForm, ProjectForm

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

def new_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            prj_name = form.cleaned_data['project_name']
            prj_autor = form.cleaned_data['autor']
            prj_sc_dir = form.cleaned_data['sc_dir']
            prj_short_desc = form.cleaned_data['short_desc']
            prj_full_desc = form.cleaned_data['full_desc']
            prj = Project(name=prj_name, autor=prj_autor, sc_dir=prj_sc_dir, short_desc=prj_short_desc, full_desc=prj_full_desc, icon=None)
            prj.save()
            if request.FILES.get('icon'):
                prj_icon = request.FILES['icon']
                prj.icon = prj_icon
                prj.save()
            else:
                text_ = 'Please, upload files!'
                form = ProjectForm(instance=prj)
        else:
            text_ = 'Please, fill the from correctly!'
            form = ProjectForm()
    else:
        text_ = 'New project'
        form = ProjectForm()
    return render(request, 'main/new_project.html', {'form': form, 'text_': text_})