from django.db import models
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    name = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    info = models.TextField()
    
    def __unicode__(self):
        return self.name
    
    def update_points(self):
        from . import FINISHED
        assigned = Task.objects.filter(assigned_to=self.user)
        supported = assigned.exclude(project__owner=self.user).filter(status=FINISHED)
        self.points = supported.count()
        self.save()
    
    class Meta:
        app_label= 'app'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, raw, **kwargs):
    if created and not raw:
        UserProfile.objects.get_or_create(user=instance)

from . import Task

@receiver(pre_save, sender=Task)
@receiver(pre_delete, sender=Task)
def remember_old_assignee(sender, instance, **kwargs):
    try:
        instance.old_user = Task.objects.get(pk=instance.pk).assigned_to
    except:
        instance.old_user = None

@receiver(post_save, sender=Task)
@receiver(post_delete, sender=Task)
def update_affected_users(sender, instance, **kwargs):
    old_user = instance.old_user
    new_user = instance.assigned_to if hasattr(instance, 'assigned_to') else None
    
    if old_user:
        old_user.profile.update_points()
    
    if new_user and (old_user is None or old_user.pk != new_user.pk):
        new_user.profile.update_points()
