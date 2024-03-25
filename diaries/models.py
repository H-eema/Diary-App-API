from django.db import models
from django.conf import settings


class Diary(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    update_date = models.DateTimeField(auto_now=True)
