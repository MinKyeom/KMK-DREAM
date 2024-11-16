from django.shortcuts import render
# 새로 추가한 import 한 부분 11.12
from django.shortcuts import render,redirect
from blog.models import Post,Comment
from collections import defaultdict
from blog.forms import LoginForm
from django.contrib.auth import authenticate,login,logout

def index(request):
    keyword=request.GET.get("search")
    posts=Post.objects.all()
    #최신 소식
    Code_ps=[posts[len(posts)-1]]

    if keyword is None:
        context={
            "posts":Code_ps,
            "check":keyword,
        }
        return render(request,"index.html",context)
    else:
        if keyword=="":
            keyword=None
            context={
                "posts":Code_ps,
                "check":keyword,
            }
            return render(request,"index.html",context)

        new=[]
        for post in posts:
            if keyword in post.title or keyword in post.content:
                new.append(post)

        context={
            "posts": new,
            "check": keyword,
        }

        return render(request, "index.html",context)

