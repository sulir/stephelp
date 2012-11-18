from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    class Meta:
        app_label= 'app'