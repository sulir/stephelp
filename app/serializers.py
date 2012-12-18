from django.db.models import OneToOneField
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, ManyHyperlinkedRelatedField
from models import Category, Project, Task, User, UserProfile

class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category

class ProjectSerializer(HyperlinkedModelSerializer):
    tasks = ManyHyperlinkedRelatedField(view_name='task-detail')
    
    class Meta:
        model = Project

class TaskSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Task

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ('id', 'user')

class UserSerializer(HyperlinkedModelSerializer):
    profile = UserProfileSerializer()
    
    class Meta:
        model = User
        fields = ('username', 'is_active', 'is_superuser', 'profile')
        depth = 1