from django.urls import path
from blog import views 

app_name = 'blog'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('new/', views.new,	name="new"),
    path('detail/<int:post_pk>/', views.detail,	name="detail"),
    path('update/<int:post_pk>/', views.update,	name="update"),
    path('delete/<int:post_pk>/', views.delete,	name="delete"),
    path('delete-comment/<int:post_pk>/<int:comment_pk>', views.delete_comment, name='delete_comment'),
    path('imageUpload/', views.write_task, name="imageUpload"),
    path('index/', views.index, name="index"),
]