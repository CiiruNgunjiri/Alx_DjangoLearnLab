# Generated by Django 5.1.4 on 2024-12-26 15:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='followers',
        ),
        migrations.AddField(
            model_name='customuser',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]