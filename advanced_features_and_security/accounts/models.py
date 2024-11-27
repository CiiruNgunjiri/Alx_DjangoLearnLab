# Create your models here.
# accounts/models.py
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)  # Optional field for date of birth
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)  # Optional field for profile photo

    objects = CustomUserManager()
     
    # Override groups field
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_accounts',  # Unique related name for accounts app
        blank=True,
    )

    # Override user_permissions field
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_accounts_permissions',  # Unique related name for accounts app
        blank=True,
    )
     
    def __str__(self):
        return self.username # Return username for representation
 

class SomeModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='account_some_models')

