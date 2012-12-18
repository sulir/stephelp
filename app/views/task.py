from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404
from django.template.context import Context
from django.template.loader import get_template
from ..decorators import require_AJAX, require_POST_params
from ..forms import TaskForm
from ..helpers import render_json
from ..models import Project, Task, User

def task_list(request, project_id):
    return render(request, 'app/task_list.html', {
        'tasks': Task.objects.filter(project__id=project_id)
    })

@require_POST
@require_AJAX
def task_create(request):
    data = request.POST.copy()
    try:
        data['assigned_to'] = User.objects.get(username=data['assigned_to']).id
    except User.DoesNotExist:
        pass
    
    form = TaskForm(data)
    if form.is_valid():
        if Project.objects.get(pk=data['project']).owner == request.user:
            form.save()
            return render_json({'success': "The task was added."})
        else:
            return render_json({'error': "You can only add tasks to you own projects."})
    else:
        return render_json({'errors': form.errors})

@require_AJAX
@require_POST_params(name=('description', 'assigned_to', 'status'), value=())
def task_update(request, pk):
    name, value = request.POST['name'], request.POST['value']
    task = get_object_or_404(Task, pk=pk)
    
    if task.project.owner == request.user:
        if name == 'assigned_to':
            if value:
                try:
                    value = User.objects.get(username=value)
                except User.DoesNotExist:
                    return HttpResponseForbidden("Enter a username or leave blank.")
            else:
                value = None
        
        setattr(task, name, value)
        
        try:
            task.full_clean()
            task.save()
            if name == 'assigned_to' and value:
                return render_json({'profile_url': reverse('user', args=[value.id])})
            else:
                return render_json({'success': ""})
        except ValidationError as error:
            return HttpResponseForbidden(" ".join(error.messages))
    else:
        return HttpResponseForbidden("You can only edit your own project tasks.")

@require_POST
@require_AJAX
def task_delete(request, pk):
    get_object_or_404(Task, pk=pk).delete()
    return render_json({'success': ""})

@require_POST
@require_AJAX
def task_support(request, pk):
    task = get_object_or_404(Task, pk=pk)
    text = request.POST['text']
    body = get_template('app/support_email.txt').render(Context({
        'user': request.user,
        'task': task,
        'text': text,
        'host': request.get_host()
    }))
    print(body) # debug
    send_mail("StepHelp project support", body, request.user.email, [task.project.owner.email])
    return render_json({'success': ""})
