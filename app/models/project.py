from django.db import models
from user import User
from category import Category

class Project(models.Model):
    owner = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    class Meta:
        app_label= 'app'