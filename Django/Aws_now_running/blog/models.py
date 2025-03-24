from django.db import models

# user model 사용 작성자 추가 25_03_02
from django.contrib.auth.models import User
import os

# 마크다운 사용하기 위해 사용 2_23
import markdown
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
from django.utils.safestring import mark_safe

# 블로그 내 유저 로그인 모델 형성
from django.contrib.auth.models import AbstractUser

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

    """
    on_delete=models.CSASCADE:작성자 삭제 시 이 포스트 삭제
    on_delete=models.SET_NULL:작성자가 삭제 시 null로 변경
    """

    author =models.ForeignKey(User,null=True ,on_delete=models.SET_NULL)
    category=models.ForeignKey(Category, null=True,blank=True ,on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)
    thumbnail = models.ImageField("썸네일 이미지", upload_to="Diary", blank=True)

    #작성 시간,최종 수정 시간 저장
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    # 작성자 모델 추가

    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.author}'

    def get_content_markdown(self): # 내용 띄우는 함수 추가
        return markdown(self.content)

# 댓글 영역

# 포스트 댓글
class Comment(models.Model):
    # 댓글의 경우 사용자 삭제 시 댓글 삭제
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    content = models.TextField("댓글 내용")
    # 기존에 존재하던 댓글 떄문에 null=True를 설정안할시 오류 발생
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}::{self.post.title}의 댓글 {self.content}"

# it_diary 댓글
class itdiary_Comment(models.Model):
    # 댓글의 경우 사용자 삭제 시 댓글 삭제
    diary = models.ForeignKey(IT_Diary, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    content = models.TextField("댓글 내용",max_length=300)
    # 기존에 존재하던 댓글 떄문에 null=True를 설정안할시 오류 발생
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}::{self.diary.title}의 댓글 {self.content}"

# 코드 리뷰 모델 만들기
class code_review(models.Model):
    title=models.CharField("제목",max_length=100)
    content=MarkdownxField("내용")

    """
    on_delete=models.CSASCADE:작성자 삭제 시 이 포스트 삭제
    on_delete=models.SET_NULL:작성자가 삭제 시 null로 변경
    """

    author =models.ForeignKey(User,null=True ,on_delete=models.SET_NULL)
    category=models.ForeignKey(Category, null=True,blank=True ,on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)
    thumbnail = models.ImageField("썸네일 이미지", upload_to="Diary", blank=True)

    #작성 시간,최종 수정 시간 저장
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    # 작성자 모델 추가
    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.author}'

    def get_content_markdown(self): # 내용 띄우는 함수 추가
        return markdown(self.content)

# 코드 리뷰 페이지 댓글
class code_review_comment(models.Model):
    # 댓글의 경우 사용자 삭제 시 댓글 삭제
    code_title = models.ForeignKey(code_review, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    content = models.TextField("댓글 내용",max_length=300)
    # 기존에 존재하던 댓글 떄문에 null=True를 설정안할시 오류 발생
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}::{self.code_title.title}의 댓글 {self.content}"

# Create your models here.
