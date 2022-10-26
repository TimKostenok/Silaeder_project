from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Project(models.Model):
    project_name = models.CharField(max_length=127)
    autor = models.CharField(max_length=255)
    year_of_creating = models.DateField()
    sc_dir = models.CharField(max_length=255)
    # s_dir = models.ForeignKey(customUser, on_delete=models.CASCADE, related_name='student')
    short_desc = models.CharField(max_length=511)
    full_desc = models.CharField(max_length=4095)
    icon = models.FileField(upload_to='icons')

class Reward(models.Model):
    full_name = models.CharField(max_length=255)
    reward_photo = models.FileField(upload_to='reward_photos')