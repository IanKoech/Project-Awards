from django.test import TestCase
from .models import Rating, Profile,Project

# Create your tests here.

class TestProfile(TestCase):

    def setUp(self):
        self.new_profile = Profile(name='Ian', bio='Yes', phone='0798940016', email='moringa@gmail.com')

    def tearDown(self):
        Profile.objects.all().delete()

    def testinstance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def testsaving(self):
        profiles = Profile.objects.all()
        self.new_profile.saveProfile()
        self.assertTrue(len(profiles)>0)


class TestProject(TestCase):

    def setUp(self):
        self.new_profile = Profile(name='Ian', bio='Yes', phone='0798940016', email='moringa@gmail.com')
        self.new_project = Project(Title = 'Yes', Description='No', User=self.new_profile)

    def tearDown(self):
        Profile.objects.all().delete()
        Project.objects.all().delete()
    
    def testinstance(self):
        self.assertTrue(isinstance(self.new_project, Project))

    def testsaving(self):
        projects = Project.objects.all()
        self.new_profile.saveProfile()
        self.new_project.saveProject()
        self.assertTrue(len(projects)>0)

class TestProject(TestCase):

    def setUp(self):
        self.new_profile = Profile(name='Ian', bio='Yes', phone='0798940016', email='moringa@gmail.com')
        self.new_project = Project(Title = 'Yes', Description='No', User=self.new_profile)
        self.new_rate = Rating(Design=10, Usability=20, Content=0,Average=30, RatedBy=self.new_profile, project=self.new_project)
    
    def tearDown(self):
        Profile.objects.all().delete()
        Project.objects.all().delete()
        Rating.objects.all().delete()
    
    def testinstance(self):
        self.assertTrue(isinstance(self.new_rate, Rating))

    def testsaving(self):
        ratings = Rating.objects.all()
        self.new_profile.saveProfile()
        self.new_project.saveProject()
        self.new_rate.saveRating()
        self.assertTrue(len(ratings)>0)