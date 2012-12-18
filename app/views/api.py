from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from ..models import Category, Project, Task, User
from ..serializers import CategorySerializer, ProjectSerializer, TaskSerializer, UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
    """The API entry."""
    return Response({
        'categories': reverse('category-list', request=request),
        'projects': reverse('project-list', request=request),
        'users': reverse('user-list', request=request),
    })

class CategoryMixin(object):
    model = Category
    serializer_class = CategorySerializer

class CategoryList(CategoryMixin, ListAPIView):
    """A category list API."""

class CategoryDetail(CategoryMixin, RetrieveAPIView):
    """A single category API."""

class ProjectMixin(object):
    model = Project
    serializer_class = ProjectSerializer

class ProjectList(ProjectMixin, ListAPIView):
    """A project list API."""

class ProjectDetail(ProjectMixin, RetrieveAPIView):
    """A single project API."""

class TaskMixin(object):
    model = Task
    serializer_class = TaskSerializer

class TaskList(TaskMixin, ListAPIView):
    """A task list API."""

class TaskDetail(TaskMixin, RetrieveAPIView):
    """A single task API."""

class UserMixin(object):
    model = User
    serializer_class = UserSerializer

class UserList(UserMixin, ListAPIView):
    """A user list API."""

class UserDetail(UserMixin, RetrieveAPIView):
    """A single user API."""
