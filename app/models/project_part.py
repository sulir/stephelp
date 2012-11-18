from django.db import models

class ProjectPart(models.Model):
    description = models.TextField()
    assignedTo = models.IntegerField()
    
    
    
    class Meta:
        app_label= 'app'