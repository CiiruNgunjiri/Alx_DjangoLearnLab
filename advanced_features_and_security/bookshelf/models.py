from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission
from .managers import CustomUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    # Override groups field
    groups = models.ManyToManyField(Group,related_name='custom_user_bookshelf',  # Unique related name for accounts app
        blank=True,)

    # Override user_permissions field
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_bookshelf_permissions',  # Unique related name for accounts app
        blank=True,
    )

    objects = CustomUserManager()

    class Meta:
        permissions = [
            ("can_create", "Can create content"),
            ("can_delete", "Can delete content"),
        ]

    def __str__(self):
        return self.username 

class SomeModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookshelf_some_models')

