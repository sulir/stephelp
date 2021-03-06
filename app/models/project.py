from django.db import models
from django.db.models.aggregates import Avg
from django.contrib.auth.models import User
from . import Category

class ProjectManager(models.Manager):
    def top(self, category_id=None, count=None):
        projects = self.filter(category=category_id) if category_id else self
        return projects.order_by('-owner__profile__points')[:count]

class Project(models.Model):
    owner = models.ForeignKey(User, related_name='projects')
    category = models.ForeignKey(Category, related_name='projects')
    name = models.CharField(max_length=100)
    summary = models.TextField(max_length=800)
    image = models.URLField(max_length=1024, verbose_name="Image URL")
    description = models.TextField()
    
    objects = ProjectManager()
    
    def __unicode__(self):
        return self.name
    
    @property
    def completion(self):
        tasks_pct = [task.completion for task in self.tasks.all()]
        return sum(tasks_pct) / len(tasks_pct) if len(tasks_pct) else 0
    
    class Meta:
        app_label= 'app'