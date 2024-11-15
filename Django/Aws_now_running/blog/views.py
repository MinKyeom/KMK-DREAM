from django.shortcuts import render,redirect
from blog.models import Post,Comment
from collections import defaultdict
from blog.forms import LoginForm
from django.contrib.auth import authenticate,login,logout

def post_list(request):
    """
    posts=Post.objects.all()
    user=request.user
    login_check=user.is_authenticated
    context={
        "posts":posts,
        "user":login_check,
    }
    """
    keyword=request.GET.get("search")
    posts = Post.objects.all()
    user = request.user
    login_check = user.is_authenticated

    new=[]
    if keyword is not None:
        for k in posts:
            if keyword in k.content or keyword in k.title:
                new.append(k)
        context = {
            "posts": new,
            "user": login_check,
        }

    else:
        context = {
            "posts": posts,
            "user": login_check,
        }

    return render(request,"post_list.html",context)
# Create your views here.

def post_detail(request,post_id):
    post=Post.objects.get(id=post_id)
    if request.method=="POST":
        comment_content=request.POST["comment"]
        Comment.objects.create(
            post=post,
            content=comment_content,
        )
    context={
        "post" : post,
    }

    return render(request, "post_detail.html",context)

def post_add(request):
    user=request.user
    login_check=user.is_authenticated

    # 글 작성 여부 로그인 확인
    if login_check==False:
        return redirect("../../users/login")

    if request.method=="POST":
        title=request.POST["title"]
        content=request.POST["content"]

        # 변경 전 코드 목록(사진 없이 업로드 가능하게 변경)
        """
        # thumbnail = request.FILES["thumbnail"]
        # post=Post.objects.create(
        #     title=title,
        #     content=content,
        #     thumbnail=thumbnail,
        # )
        """

        if "thumbnail" in request.FILES:
            thumbnail=request.FILES["thumbnail"]

            post=Post.objects.create(
                title=title,
                content=content,
                thumbnail=thumbnail,
            )
        else:
            post=Post.objects.create(
                title=title,
                content=content,
            )
        return redirect(f"/posts/{post.id}")
    else:
        pass

    return render(request,"post_add.html")

#post search 추가 11_06 > 의미 없어서 사용안함
"""
def post_search_list(request):
    keyword=request.GET.get("keyword")
    if len(keyword)==0:
        posts=Post.objects.all()
        user=request.user
        login_check=user.is_authenticated
        context={
            "posts":posts,
            "user":login_check,
        }
    else:
        posts=Post.objects.filter(name__contain=keyword)
        user=request.user
        login_check=user.is_authenticated
        context={
            "posts":posts,
            "user":login_check,
        }
    return render(request,"post_search_list.html",context)
"""

def login_view(request):
    if request.user.is_authenticated:
        return redirect("../../users/login/feeds")
        # 피드 페이지 차후 재구성
        #return render(request, "users/feeds.html")

    if request.method== "POST":
        form =LoginForm(data=request.POST)
        password=request.POST["password"]
        if form.is_valid():
            username=form.cleaned_data["username"]
            # 비밀번호를 숨기는 구조를 만들기 위해 재구성
            #password=form.cleaned_data["password"]

            user=authenticate(username=username,password=password)

            if user:
                login(request,user)
                # 처음 페이지로 돌아가기!
                return redirect("../../")

        context={"form": form}
        return render(request,"users/login.html",context)

    else:
        form=LoginForm()
        context={"form":form}
        return render(request,"users/login.html",context)

# 로그인 피드백
def login_feeds(request):
    user=request.user
    login_check=user.is_authenticated

    if login_check==False:
        return redirect("../")

    return render(request, "users/feeds.html")

# 로그아웃

def loginout_view(request):
    logout(request)

    return redirect("../login")

# 임시 페이지
def check(request):
    return render(request,"check.html")