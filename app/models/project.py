from django.db import models

class Project(models.Model):
    owner_id = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    class Meta:
        app_label= 'app'