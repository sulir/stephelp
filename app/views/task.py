from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST
from django.views.generic import UpdateView
from django.shortcuts import render
from ..decorators import require_ajax
from ..forms import TaskForm
from ..helpers import render_json
from ..models import Project, Task, User
from django.http import HttpResponseForbidden

def task_list(request, project_id):
    return render(request, 'app/task_list.html', {
        'tasks': Task.objects.filter(project__id=project_id)
    })

@require_POST
@require_ajax
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

@require_POST
def task_update(request, pk):
    name, value = request.POST['name'], request.POST['value']
    if name in ('description', 'assigned_to', 'status'):
        task = Task.objects.get(pk=pk)
        setattr(task, name, value)
        
        try:
            task.full_clean()
            task.save()
        except ValidationError as error:
            return HttpResponseForbidden(" ".join(error.messages))
    
    return render_json({'s': ''})
