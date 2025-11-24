from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    language = models.CharField(max_length=10, default="en")
    chat_id = models.BigIntegerField(unique=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
