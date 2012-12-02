from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from app.models import UserProfile, Project, ProjectPart

def index(request):
    return render(request, 'app/index.html')

def projects(request):
    return render(request, 'app/projects.html')

def about(request):
    return render(request, 'app/about.html')

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
            if user.is_active:
                login(request, user)

    return render(request, 'app/index.html')

def logout_view(request):
    logout(request)
    return render(request, 'app/index.html') 

def user_detail(request, user_id):
    p = UserProfile.objects.get(pk=user_id)
    pr= Project.objects.filter(owner=user_id)
    prp= ProjectPart.objects.filter(assigned_to=user_id)
    return render(request,'app/profile.html', {'userd': p,'projects':pr,'project_parts':prp})