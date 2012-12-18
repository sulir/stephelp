from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView
from django.views.generic.edit import ModelFormMixin, FormMixin
from ..models import Category, Project, Task
from ..forms import ProjectForm, TaskForm

def project_list(request, category_id=None):
    """List all projects or projects from a specific category."""
    return render(request, 'app/project_list.html', {
        'category_id': int(category_id or 0),
        'category_list': Category.objects.all(),
        'project_list': Project.objects.top(category_id=category_id)
    })

class ProjectDetail(DetailView):
    """Display a page containing the project description and tasks."""
    model = Project
    
    def get_context_data(self, **kwargs):
        form = TaskForm(initial={'project': self.object.pk})
        return super(ProjectDetail, self).get_context_data(
            task_add_form=form,
            task=get_object_or_404(Task, pk=self.request.GET['task']) if 'task' in self.request.GET else None,
            assignee=self.request.GET['user'] if 'user' in self.request.GET else None
        )

class ProjectMixin(ModelFormMixin):
    """The behavior common for both the Create and Update form."""
    model = Project
    form_class = ProjectForm
    
    def form_valid(self, form):
        project = form.save(self.request.user)
        messages.success(self.request, self.success_message)
        return redirect('project', pk=project.pk)

class ProjectCreate(CreateView, ProjectMixin):
    """Project creation. Only logged users are allowed."""
    template_name = 'app/project_create.html'
    success_message = "Your project was successfully created. Now you can add some tasks."
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous():
            return render(request, self.template_name)
        else:
            return super(ProjectCreate, self).dispatch(request, *args, **kwargs)

class ProjectUpdate(UpdateView, ProjectMixin):
    """Project editing. A user can only edit its own projects."""
    template_name = 'app/project_update.html'
    success_message = "The project was updated."
    
    def dispatch(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['pk'])
        if project.owner == request.user:
            return super(ProjectUpdate, self).dispatch(request, *args, **kwargs)
        else:
            messages.error(request, "You can only update your own projects.")
            return redirect('project', pk=project.pk)
