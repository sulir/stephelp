from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def require_AJAX(function):
    def view(request, *args, **kwargs):
        if request.is_ajax():
            return function(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("This URL requires an AJAX request.")
    
    return view

def require_POST_params(**params):
    def decorator(function):
        def view(request, *args, **kwargs):
            for name, allowed_values in params.iteritems():
                if name not in request.POST:
                    return HttpResponseForbidden("The required parameter '%s' was not supplied." % name)
                if allowed_values is not () and request.POST[name] not in allowed_values:
                    return HttpResponseForbidden("The value of parameter '%s' is invalid." % name)
            return function(request, *args, **kwargs)
        return view

    return decorator

def show_profile_if_logged(function):
    def view(request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('user', user_id=request.user.id)
        else:
            return function(request, *args, **kwargs)
    
    return view