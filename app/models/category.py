from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        app_label= 'app'
        verbose_name_plural = "categories"