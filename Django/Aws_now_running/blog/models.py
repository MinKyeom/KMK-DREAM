from django.db import models

# 블로그 내 유저 로그인 모델 형성
from django.contrib.auth.models import AbstractUser

class Post(models.Model):
    title=models.CharField("포스트 제목",max_length=100)
    link=models.TextField("포스트 관련 링크",null=True,default="")
    content=models.TextField("포스트 내용")
    thumbnail=models.ImageField("썸네일 이미지", upload_to="post", blank=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    content=models.TextField("댓글 내용")

    def __str__(self):
        return f"{self.post.title}의 댓글 (ID: {self.id})"

# login 모델 (10_21)
class Blog_User(models.Model):
    name=models.CharField("이름,name",max_length=100,null=True,default='')
    password=models.CharField("비밀번호,password",max_length=20,null=True,default='')
    email=models.TextField("이메일,email",null=True,default='')
    def __str__(self):
        return f"{self.name,self.password,self.email}"
# Create your models here.
