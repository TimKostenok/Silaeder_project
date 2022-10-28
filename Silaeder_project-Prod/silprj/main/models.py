from datetime import datetime
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, username, email, password, first_name, last_name):
        user = self.model(username=username, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, first_name, last_name):
        user = self.create_user(username, email, password, first_name, last_name)
        user.is_admin = True
        user.save(using=self._db)
        return user

class SUser(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    @property
    def is_staff(self):
        return self.is_admin

class Project(models.Model):
    project_name = models.CharField(default='Random project', max_length=127, unique=True)
    authors = models.ManyToManyField(SUser, null=True)
    sc_dir = models.CharField(default='OA', max_length=255)
    # s_dir = models.ForeignKey(customUser, on_delete=models.CASCADE, related_name='student')
    short_desc = models.CharField(default='It is a project', max_length=511)
    full_desc = models.CharField(default='It is a project', max_length=4095)
    icon = models.FileField(upload_to='icons')

class Reward(models.Model):
    full_name = models.CharField(max_length=255)
    reward_photo = models.FileField(upload_to='reward_photos')