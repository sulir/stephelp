from django.db import models
from project import Project
from user import User

PLANNED, LAUNCHED, FINISHED = 'P', 'L', 'F'
STATUS = (
    (PLANNED, "planned"),
    (LAUNCHED, "launched"),
    (FINISHED, "finished")
)

class ProjectPart(models.Model):
    project = models.ForeignKey(Project, related_name='parts')
    assigned_to = models.ForeignKey(User, null=True, related_name='parts')
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS)
    
    def __unicode__(self):
        return self.description
    
    class Meta:
        app_label= 'app'