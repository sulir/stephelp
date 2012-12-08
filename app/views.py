from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView, ListView
from app.models import Category, Project, ProjectPart, UserProfile

def index(request):
    return ListView.as_view(
        queryset=Project.objects.top(count=5),
        template_name='app/index.html'
    )(request)

def project_list(request, category_id=None):
    return render(request, 'app/project_list.html', {
        'category_id': int(category_id or 0),
        'category_list': Category.objects.all(),
        'project_list': Project.objects.top(category_id=category_id)
    })

def project_detail(request, project_id):
    return DetailView.as_view(
        model=Project
    )(request, pk=project_id)

def project_create(request):
    return render(request, 'app/project_create.html') 

def project_update(request, project_id):
    pass

def user_detail(request, user_id):
    p = UserProfile.objects.get(pk=user_id)
    pr = Project.objects.filter(owner=user_id)
    prp = ProjectPart.objects.filter(assigned_to=user_id)
    return render(request,'app/user_detail.html', {'userd': p,'projects':pr,'project_parts':prp})

def register(request):
    pass

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
    
    return redirect(index)

def logout(request):
    logout(request)
    return redirect(index)

def about(request):
    return render(request, 'app/about.html')
