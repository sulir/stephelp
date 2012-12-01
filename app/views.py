from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response

def index(request):
    return render(request, 'app/index.html')

def projects(request):
    return render(request, 'app/projects.html')

def userlogin(request):
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