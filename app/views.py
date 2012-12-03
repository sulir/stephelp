from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from app.models import UserProfile, Project, ProjectPart

def index(request):
    return render(request, 'app/index.html')

def project_list(request, category_id=None):
    return render(request, 'app/project_lits.html')

def project_detail(request, project_id):
    pass

def project_create(request):
    pass

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
    
    return render(request, 'app/index.html')

def logout(request):
    logout(request)
    return render(request, 'app/index.html') 

def about(request):
    return render(request, 'app/about.html')
