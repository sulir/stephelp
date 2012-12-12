from django.shortcuts import render, redirect
from django.views.generic import DetailView
from ..models import Category, Project
from ..forms import UserForm, ProjectForm

def project_list(request, category_id=None):
    return render(request, 'app/project_list.html', {
        'category_id': int(category_id or 0),
        'category_list': Category.objects.all(),
        'project_list': Project.objects.top(category_id=category_id)
    })

def project_detail(request, project_id):
    return DetailView.as_view(model=Project)(request, pk=project_id)

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(request.user)
            return redirect('project', project_id=project.id)
    else:
        form = ProjectForm()
    
    return render(request, 'app/project_create.html', {'form': form})

def project_update(request, project_id):
    pass