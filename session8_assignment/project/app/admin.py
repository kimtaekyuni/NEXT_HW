from django.contrib import admin
from .models import Post, double_Comment, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(double_Comment)
admin.site.register(Comment)
