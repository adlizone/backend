from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=100, 
        null=True,
        blank=True,
    )
    address = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    age = models.IntegerField(
        null=True,
        blank=True,
    )