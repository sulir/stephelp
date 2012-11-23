from django.db import models
from project import Project
from user import User

class ProjectPart(models.Model):
    project = models.ForeignKey(Project)
    assigned_to = models.ForeignKey(User)
    description = models.TextField()
    
    def __unicode__(self):
        return self.description
    
    class Meta:
        app_label= 'app'