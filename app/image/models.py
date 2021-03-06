from __future__ import unicode_literals
from django.conf import settings
from django.db import models


# Image model
class Image(models.Model):
    title = models.TextField(max_length=512)
    description = models.TextField(max_length=512, blank=True, null=True)
    src = models.TextField(max_length=1024, unique=True)
    created = models.DateTimeField('date created', auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField('date updated', auto_now=True, blank=True, null=True)
    created_user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
