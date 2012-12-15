from django.views.decorators.http import require_POST
from django.views.generic import UpdateView
from django.shortcuts import render
from ..decorators import require_ajax
from ..forms import TaskForm
from ..helpers import render_json
from ..models import Project, Task, User

def task_list(request, project_id):
    return render(request, 'app/task_list.html', {
        'tasks': Task.objects.filter(project__id=project_id)
    })


def task_create(request):
    data = request.POST.copy()
    try:
        data['assigned_to'] = User.objects.get(username=data['assigned_to']).id
    except User.DoesNotExist:
        return render_json({'errors': {'assigned_to': "The username does not exist."}})
    
    form = TaskForm(data)
    if form.is_valid():
        if Project.objects.get(pk=data['project']).owner == request.user:
            form.save()
            return render_json({'success': "The task was added."})
        else:
            return render_json({'error': "You can only add tasks to you own projects."})
    else:
        return render_json({'errors': form.errors})

class TaskUpdate(UpdateView):
    pass