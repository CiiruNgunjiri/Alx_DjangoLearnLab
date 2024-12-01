# Create your models here.
# accounts/models.py
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission, User
from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

# Define user types using TextChoices for better readability and maintainability
class UserTypes(models.TextChoices):
    ADMIN = "ADMIN", _("Admin")
    LIBRARIAN = "LIBRARIAN", _("Librarian")
    MEMBER = "MEMBER", _("Member")

class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)  # Optional field for date of birth
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)  # Optional field for profile photo
    email = models.EmailField(unique=True, max_length=50)  # Ensure email is unique
    type = models.CharField(
        max_length=20,
        choices=UserTypes.choices,
        default=UserTypes.MEMBER  # Default user type
    ) 
    def __str__(self):
        return self.username

# Profile model for additional user information
class OwnerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Link to CustomUser model
    company_name = models.CharField(max_length=50, default='Default Company')
    company_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Signal to create a profile automatically when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.type == UserTypes.ADMIN:
            OwnerProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.ownerprofile.save()  # Save the profile when the user is saved


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

# Custom User model extending AbstractUser
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)  # Optional field for date of birth
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)  # Optional field for profile photo
    email = models.EmailField(unique=True, max_length=50)  # Ensure email is unique
    type = models.CharField(
        max_length=20,
        choices=UserTypes.choices,
        default=UserTypes.MEMBER # Default user type
    ) 
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
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.username  # Return username for representation
 

    
class SomeModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='account_some_models')
