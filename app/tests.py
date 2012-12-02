from django.test import TestCase
from models.project import Project
from models.project_part import *

class ProjectTest(TestCase):
    def setUp(self):
        self.project = Project(pk=1)
        
        for i, status in enumerate((PLANNED, LAUNCHED, FINISHED, FINISHED)):
            self.project.parts.add(ProjectPart(pk=i, status=status))
    
    def test_completion(self):
        self.assertEqual(self.project.completion, 62)