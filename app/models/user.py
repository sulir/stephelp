from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    name = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    description = models.TextField()
    
    class Meta:
        app_label= 'app'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, User)