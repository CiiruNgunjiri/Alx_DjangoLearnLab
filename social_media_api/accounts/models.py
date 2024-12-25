from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    phone_number = models.CharField(max_length=15)
    designation = models.CharField(max_length=100)

    # Add related_name to avoid clash with default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Change this name as needed
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Change this name as needed
        blank=True,
    )

