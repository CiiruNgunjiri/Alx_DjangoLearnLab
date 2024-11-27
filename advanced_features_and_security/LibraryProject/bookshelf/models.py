from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    id = models.AutoField(primary_key=True)

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_delete", "Can delete book"),
            ("can_edit", "Can edit book"),
        ]

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    # Override groups field
    groups = models.ManyToManyField(Group,related_name='custom_user_bookshelf',  # Unique related name for bookshelf app
        blank=True,)

    # Override user_permissions field
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_bookshelf_permissions',  # Unique related name for accounts app
        blank=True,
    )
    objects = CustomUserManager()

    def __str__(self):
        return self.username 

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)

class SomeModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookshelf_some_models')

