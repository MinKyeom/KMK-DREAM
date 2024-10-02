from django.shortcuts import render
from blog.models import Post
# Create your views here.

def post_list(request):
    posts=Post.objects.all()
    print(posts)
    context={
        "posts": posts,
    }
    print(context)

    return render(request, "post_list.html",context)