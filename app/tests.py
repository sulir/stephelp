from django.test import TestCase
from models.project import Project
from models.project_part import ProjectPart, PLANNED, LAUNCHED, FINISHED
from models.user import User

class ProjectTest(TestCase):
    def setUp(self):
        self.project = Project(pk=1)
        
        for i, status in enumerate((PLANNED, LAUNCHED, FINISHED, FINISHED)):
            self.project.parts.add(ProjectPart(pk=i, status=status))
    
    def test_completion(self):
        self.assertEqual(self.project.completion, 62)

class UserTest(TestCase):
    fixtures = ['user_test']
    
    def setUp(self):
        self.user = User.objects.get(username='user')
        self.other_user = User.objects.get(username='other_user')
    
    def test_points(self):
        self.assertEqual(self.user.profile.points, 1)
        self.assertEqual(self.other_user.profile.points, 0)