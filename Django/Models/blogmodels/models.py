from django.db import models

# user model 사용 작성자 추가 25_03_02
from django.contrib.auth.models import User
import os

# 마크다운 사용하기 위해 사용 2_23
import markdown
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
from django.utils.safestring import mark_safe

#github api활용하기 위해
import requests

# 블로그 내 유저 로그인 모델 형성
from django.contrib.auth.models import AbstractUser

# github api를 빌려 글 형식 변환
def md_to_gfm(text):
    headers = {'Content-Type': 'text/plain'}
    data = text.encode('utf-8')
    r = requests.post('https://api.github.com/markdown/raw', headers=headers, data=data)

    return r.text.encode('utf-8')

# 카테고리 클래스 만들기 먼저 class를 선언해줘야 아래에서 카테고리 클래스 사용 가능!
class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=200,unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

# 태그 클래스 생성(m:n 관계)
class Tag(models.Model):
    """
    기존 작성 코드
    name = models.CharField(max_length=32,verbose_name="태그명")
    registered_dttm = models.DateField(auto_now_add=True, verbose_name="등록시간")
    """

    name=models.CharField(max_length=30)
    slug=models.SlugField(max_length=200,unique=True,allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}'

class Post(models.Model):
    title=models.CharField("포스트 제목",max_length=100)
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

# patch(update) 모델

class Update_note(models.Model):
    title=models.CharField("업데이트 제목",max_length=100)
    content=models.TextField("업데이트 내용")


    def __str__(self):
        return self.title

# 다이어리 파트 모델 개발 2_22
class IT_Diary(models.Model):
    title=models.CharField("제목",max_length=100)
    content=MarkdownxField("내용")
    author =models.ForeignKey(User,null=True ,on_delete=models.SET_NULL)
    category=models.ForeignKey(Category, null=True,blank=True ,on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)
    #tags = models.ManyToManyField('blog.Tag', verbose_name="태그", blank=True)
    thumbnail = models.ImageField("썸네일 이미지", upload_to="Diary", blank=True)

    #작성 시간,최종 수정 시간 저장
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    # 작성자 모델 추가
    """
    on_delete=models.CSASCADE:작성자 삭제 시 이 포스트 삭제
    on_delete=models.SET_NULL:작성자가 삭제 시 null로 변경
    """

    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.author}'

    def get_content_markdown(self): # 내용 띄우는 함수 추가
        return markdown(self.content)

    def gfm(self):
        return md_to_gfm(self.content)


# Create your models here.
