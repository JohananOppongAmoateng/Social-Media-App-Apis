from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    profile_image = models.ImageField()
    bio = models.TextField(max_length=300)
    