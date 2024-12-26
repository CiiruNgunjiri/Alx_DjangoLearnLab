# notifications/admin.py

from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'actor', 'verb', 'target', 'timestamp')
    list_filter = ('recipient', 'actor', 'verb')
    search_fields = ('verb',)

admin.site.register(Notification, NotificationAdmin)
