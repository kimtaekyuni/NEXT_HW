from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveBigIntegerField(help_text="User Age", null=True, blank=True)