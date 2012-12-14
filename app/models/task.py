from django.db import models
from django.contrib.auth.models import User
from . import Project

PLANNED, LAUNCHED, FINISHED = 'P', 'L', 'F'
STATUS = (
    (PLANNED, "planned"),
    (LAUNCHED, "launched"),
    (FINISHED, "finished")
)

class Task(models.Model):
    project = models.ForeignKey(Project, related_name='tasks')
    description = models.CharField(max_length=200)
    assigned_to = models.ForeignKey(User, null=True, related_name='tasks')
    status = models.CharField(max_length=1, choices=STATUS, default=PLANNED)
    
    def __unicode__(self):
        return self.description
    
    @property
    def completion(self):
        percentage = {PLANNED: 0, LAUNCHED: 50, FINISHED: 100}
        return percentage[self.status]
    
    @property
    def can_be_supported(self):
        return (status == PLANNED) and (self.assigned_to != self.project.owner)
    
    class Meta:
        app_label= 'app'