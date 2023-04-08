from django.db import models
import datetime

# Create your models here.

class Post(models.Model):
    category = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    content = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return self.title