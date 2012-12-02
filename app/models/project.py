from django.db import models
from django.db.models.aggregates import Avg
from user import User
from category import Category

class ProjectManager(models.Manager):
    def by_top_users(self, count):
        return self.order_by('-owner__points')[:count]
    
    def by_category(self, category_id):
        return self.filter(category=category_id).order_by('-owner__points')

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
        return sum(parts_pct) / len(parts_pct)
    
    class Meta:
        app_label= 'app'