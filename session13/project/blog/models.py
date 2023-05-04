from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#	Create	your	models	here.
class Post(models.Model):
#	모델 속성 : 데이터베이스 테이블의 컬럼 = 모델 클래스의 속성 = 모델 클래스의 필드 (ORM)
    title	= models.CharField(verbose_name='TITLE',	max_length=50)
#	CharField는 max_length가 필수. form에서 input tag
    content	= models.TextField()
#	TextField는 form에서 textarea tag
    create_dt = models.DateTimeField(auto_now_add=True)
#	auto_now_add는 생성 시각 기준으로 자동 생성
    update_dt = models.DateTimeField(auto_now=True)
#	auto_now는 저장 시각 기준으로 자동 생성
    author	= models.ForeignKey(User,	on_delete=models.CASCADE,	related_name="my_posts", null=True)

    class Meta:

        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering	= ('-create_dt',	'author')
    
def __str__(self):
    return f'{self.title}입니다.'

def get_absolute_url(self):
    return reverse(f'blog:post_detail',	args=[self.id])

def get_previous(self):
    return self.get_previous_by_create_dt()

def get_next(self):
    return self.get_next_by_create_dt()

class Comment(models.Model):
    post	= models.ForeignKey(Post,	on_delete=models.CASCADE,	related_name='comments')
    author	= models.ForeignKey(User,	on_delete=models.CASCADE,	
    related_name="my_comments")
    content	= models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering	= ('-create_dt',	'post',	'author')
    
    def __str__(self):
        return f'{self.author}-{self.content}'