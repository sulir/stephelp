from django.db import models

class ProjectPart(models.Model):
    Description = models.TextField()
    AssignedTo = models.IntegerField()
    
    
    
    class Meta:
        app_label= 'app'