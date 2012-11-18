from django.db import models

class ProjectPart(models.Model):
    project_id = models.ForeignKey(Project)
    assignedTo = models.ForeignKey(User)
    description = models.TextField()
    assignedTo = models.IntegerField()
    
    
    
    class Meta:
        app_label= 'app'