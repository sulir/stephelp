from django.shortcuts import redirect

def show_profile_if_logged(function):
    def view(request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('user', user_id=request.user.id)
        else:
            return function(request, *args, **kwargs)
    
    return view