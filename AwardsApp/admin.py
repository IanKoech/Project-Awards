from django.contrib import admin
from .models import Project, Profile, Rating

# Register your models here.
admin.register(Project)
admin.register(Profile)
admin.register(Rating)