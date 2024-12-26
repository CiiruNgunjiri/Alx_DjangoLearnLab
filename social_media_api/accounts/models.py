from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    designation = models.CharField(max_length=100, blank=True)

    # Add related_name to avoid clash with default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='accounts_customuser_groups',  # Change this name as needed
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='accounts_customuser_permissions',  # Change this name as needed
        blank=True,
    )
    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'
    
    def __str__(self):
        return self.username  # or return f"{self.username} ({self.designation})"
