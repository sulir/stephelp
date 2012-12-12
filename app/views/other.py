from django.views.generic import ListView
from django.shortcuts import render
from ..models import Project

def index(request):
    return ListView.as_view(
        queryset=Project.objects.top(count=5),
        template_name='app/index.html'
    )(request)

def about(request):
    return render(request, 'app/about.html')