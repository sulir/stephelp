from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView, ListView, CreateView
from django.template import RequestContext
from models import Category, Project, Task, User, UserProfile
from forms import UserForm

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
    return DetailView.as_view(model=Project)(request, pk=project_id)

def project_create(request):
    return render(request, 'app/project_create.html')

def project_update(request, project_id):
    pass

def user_detail(request, user_id):
    return render(request,'app/user_detail.html', {
        'user_d': User.objects.get(pk=user_id)
    })

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User(username=data['username'], email=data['email'])
            user.set_password(data['password'])
            user.save()
            user.profile.name, user.profile.info = data['name'], data['info']
            user.profile.save()
            messages.success(request, "Your account was successfully created!")
            # TODO: login
            return redirect('user', user_id=user.id)
    else:
        form = UserForm()
    
    return render(request, 'app/register.html', {'form': form})

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
