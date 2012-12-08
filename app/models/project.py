from django.db import models
from django.db.models.aggregates import Avg
from django.contrib.auth.models import User
from category import Category

class ProjectManager(models.Manager):
    def top(self, category_id=None, count=None):
        projects = self.filter(category=category_id) if category_id else self
        return projects.order_by('-owner__profile__points')[:count]

class Project(models.Model):
    owner = models.ForeignKey(User, related_name='projects')
    category = models.ForeignKey(Category, related_name='projects')
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    objects = ProjectManager()
    
    def __unicode__(self):
        return self.name
    
    @property
    def completion(self):
        parts_pct = [part.completion for part in self.parts.all()]
        return sum(parts_pct) / len(parts_pct) if len(parts_pct) else 0
    
    class Meta:
        app_label= 'app'