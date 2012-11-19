from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)    
    password = models.CharField(max_length=100)	
    points = models.IntegerField()
    mail = models.EmailField()
    description = models.TextField()

    class Meta:
        app_label= 'app'