from django.db import models

# Create your models here.
class Profile(models.Model):
    '''
    Class creates instances of Applications users
    '''
    name = models.CharField(max_length=30)
    profilepic = models.ImageField(upload_to = 'profiles/')
    bio = models.TextField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.name
    
    def saveProfile(self):
        self.save()

    def deleteProfile(self):
        self.delete()

class Project(models.Model):
    '''
    Class instantiates diff Users' projects
    '''
    Title = models.CharField(max_length=30)
    Landing = models.ImageField(upload_to = 'landings/')
    Description = models.TextField()
    User = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title

    def saveProject(self):
        self.save()

    def deleteProject(self):
        self.delete()

class Rating(models.Model):
    Design = models.IntegerField()
    Usability  = models.IntegerField()
    Content = models.IntegerField()
    Average  = models.IntegerField()
    RatedBy  = models.ForeignKey(Profile, on_delete= models.CASCADE)
    project  = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.Design

    def saveRating(self):
        self.save()