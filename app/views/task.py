from django.views.decorators.http import require_POST
from django.views.generic import UpdateView
from ..decorators import require_ajax
from ..forms import TaskForm
from ..helpers import render_json
from ..models import Project

@require_POST
#@require_ajax
def task_create(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        if Project.objects.get(pk=request.POST['project']).owner == request.user:
            form.save()
            return render_json({'success': "The task was added."})
        else:
            return render_json({'error': "You can only add tasks to you own projects."})
    else:
        return render_json({'errors': form.errors})

class TaskUpdate(UpdateView):
    pass