from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField('self', related_name='follower', blank=True, null=True)
    following = models.ManyToManyField('self', related_name='following', blank=True, null=True)
