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