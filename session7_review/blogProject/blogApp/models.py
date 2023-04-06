from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=10)
    address = models.TextField()

class Article(models.Model):
    category = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    content = models.TextField()
    time = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
    
