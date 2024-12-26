# notifications/models.py

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from accounts.models import CustomUser  # Import your CustomUser model

class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, related_name='notifications', on_delete=models.CASCADE)
    actor = models.ForeignKey(CustomUser, related_name='actor_notifications', on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)  # Description of the action (e.g., "liked your post")
    
    # Generic relation to target any model (like Post or Comment)
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    target_object_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_content_type', 'target_object_id')

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.actor} {self.verb} {self.target} at {self.timestamp}"


