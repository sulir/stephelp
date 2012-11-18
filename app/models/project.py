from django.db import models

class Project(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField()
    
    class Meta:
        app_label= 'app'