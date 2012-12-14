from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def require_ajax(function):
    def view(request, *args, **kwargs):
        if request.is_ajax():
            return function(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("This URL requires an AJAX request.")
    
    return view

def show_profile_if_logged(function):
    def view(request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('user', user_id=request.user.id)
        else:
            return function(request, *args, **kwargs)
    
    return view