# Create your models here.
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)  # Optional field for date of birth
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)  # Optional field for profile photo

    def __str__(self):
        return self.username  # Return username for representation
