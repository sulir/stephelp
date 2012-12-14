from django.http import HttpResponse
from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from ..decorators import show_profile_if_logged
from ..forms import UserForm
from ..models import User
from . import index

def user_detail(request, user_id):
    return render(request,'app/user_detail.html', {
        'user_d': User.objects.get(pk=user_id)
    })

@show_profile_if_logged
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(data['username'], data['email'], data['password'])
            user.save()
            user.profile.name, user.profile.info = data['name'], data['info']
            user.profile.save()
            
            messages.success(request, "Your account was successfully created!")
            user = auth.authenticate(username=data['username'], password=data['password'])
            auth.login(request, user)
            return redirect('user', user_id=user.id)
    else:
        form = UserForm()
    
    return render(request, 'app/register.html', {'form': form})

@require_POST
def login(request):
    username, password = request.POST['username'], request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            messages.success(request, "You were successfully logged in.")
            if request.is_ajax():
                return HttpResponse()
            else:
                return redirect('user', user_id=user.id)
        else:
            return HttpResponse("Your account has been disabled.", status=401)
    else:
        return HttpResponse("The username or password is invalid.", status=401)

def logout(request):
    auth.logout(request)
    messages.info(request, "You were logged out.")
    return redirect(index)