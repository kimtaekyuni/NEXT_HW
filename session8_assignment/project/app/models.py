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
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

    def __str__(self):
        return self.content
    
class double_Comment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='double_comments')
    content = models.TextField()

    def __str__(self):
        return self.content