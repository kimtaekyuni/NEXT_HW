from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from datetime import datetime
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(verbose_name = 'TITLE', max_length=50)
    content = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_posts", null=True)

    def __str__(self):
            return f'{self.title}입니다.'
        
    def get_absolute_url(self):
        return reverse(f'blog:post_detail', args=[self.id])
    
    def get_previous(self):
        return self.get_previous_by_create_dt()
    
    def get_next(self):
        return self.get_next_by_create_dt() 

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('-create_dt', 'author')

       

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name= 'comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'my_comments')
    content = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('create_dt', 'post', 'author')

    def __str__(self):
        return f'{self.author}-{self.content}'
    

class Posts(models.Model):
   file = models.URLField(max_length=2000)  # Consider the maximum length required for your URLs


   def __str__(self):
       return self.file