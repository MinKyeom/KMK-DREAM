from django.shortcuts import render,redirect
from blog.models import Post,Comment,Update_note,IT_Diary,itdiary_Comment,Tag
from collections import defaultdict
from blog.forms import LoginForm,MyForm
from django.contrib.auth import authenticate,login,logout
#user 모델 사용
from django.contrib.auth.models import User
import markdown
from django.views.generic import CreateView

# 바로 쟝고 자바스크립트 표시 후 돌아가기 위해 실행 03_09
from django.http import HttpResponse

# 페이지 나누기 추가 12.01
from django.core.paginator import Paginator
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
    posts = Post.objects.all().order_by("-id")
    user = request.user
    login_check = user.is_authenticated

    """
    # 추가 페이지 나누기 항목
    #paginator = Paginator(데이터 목록, 한 페이지 당 원하는 데이터의 개수)
    paginator = Paginator(posts, 1)
    for p in paginator:
        print(list(p),"page")
        
    #Paginator.page(number) 원하는 number의 페이지를 가져오기
    page_posts = paginator.page(2)
    print(page_posts,"분석")
    # if page_posts is None:
    #     page_posts = 1
    #page = paginator.page(2)

    #print(page,"페이지 체크")
    #--------페이지 나누기 부분 끝 부분-------------#
    """

    new=[]
    if keyword is not None:
        for k in posts:
            if keyword in k.content or keyword in k.title:
                new.append(k)

        # 페이지 항목 추가
        # 페이지당 보여줄 목록 개수
        paginator = Paginator(new, 10)
        now_page_number = request.GET.get("page", 1)
        page_list = paginator.get_page(now_page_number)

        context = {
            "page" :paginator,
            "posts": new,
            "user": login_check,
            "page_list": page_list,
            "keyword": keyword,
        }

    else:
        # 페이지 항목 추가
        paginator = Paginator(posts, 10)
        now_page_number = request.GET.get("page", 1)
        page_list = paginator.get_page(now_page_number)


        context = {
            "page": paginator,
            "posts": posts,
            "user": login_check,
            "page_list": page_list,
            "keyword": keyword,
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
    """
    로그인 권한 설정 정리
    id
    유저 ID
    username
    유저명
    password
    패스워드(배쉬값)
    is_active
    액티브 유저（True or False）
    is_staff
    스탭 유저（True or False）
    is_superuser
    슈퍼 유저（True or False）
    first_name
    이름
    last_name
    성
    """
    print(user.is_superuser)

    flag=False

    # 글 작성 여부 로그인 확인 최고 권한일 경우에만 접근 가능
    if user.is_superuser==False:
        # 로그인은 되있으나 권한이 없는 경우
        if login_check==True:
            print("여기로 오나?")
            #return redirect("../")
            #페이지로 넘기는게 아닌 자바스크립트 alert 또한 view에서 처리 가능
            return HttpResponse("<script> alert('글쓰기 권한이 없습니다.\\n되돌아갑니다'); location.href='/posts/'; </script>")


        #로그인이 안되어있는 경우
        else:
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
        username = request.POST["username"]
        password=request.POST["password"]
        if form.is_valid():
            # username=form.cleaned_data["username"]
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


#업데이트 및 패치노트 추가

def update_list(request):
    keyword = request.GET.get("search")
    user = request.user
    login_check = user.is_authenticated
    update_lists=Update_note.objects.all().order_by("-id")

    new = []
    if keyword is not None:
        for k in update_lists:
            if keyword in k.content or keyword in k.title:
                new.append(k)

        # 페이지 항목 추가
        # 페이지당 보여줄 목록 개수
        paginator = Paginator(new, 10)
        now_page_number = request.GET.get("page", 1)
        page_list = paginator.get_page(now_page_number)

        context = {
            "page": paginator,
            "lists": page_list,
            "user": login_check,
            "page_list": page_list,
            "keyword": keyword,
        }

    else:
        # 페이지 항목 추가
        paginator = Paginator(update_lists, 10)
        now_page_number = request.GET.get("page", 1)
        page_list = paginator.get_page(now_page_number)

        context = {
            "page": paginator,
            "lists": page_list,
            "user": login_check,
            "page_list": page_list,
            "keyword": keyword,
        }

    return render(request,"update_list.html",context)


def update_detail(request,update_id):
    update=Update_note.objects.get(id=update_id)

    if request.method=="POST":
        comment_content=request.POST["comment"]
        Comment.objects.create(
            post=update,
            content=comment_content,
        )

    context={
        "lists" : update,
    }

    return render(request,"update_detail.html", context)

#IT 다이어리 파트 개발
def itdiary_list(request):

    keyword = request.GET.get("search")
    diary = IT_Diary.objects.all().order_by("-id")
    user = request.user
    login_check = user.is_authenticated

    new = []
    # 검색 키워드가 존재할 떄
    if keyword is not None:
        for k in diary:
            if keyword in k.content or keyword in k.title:
                new.append(k)

        # 페이지 항목 추가
        # 페이지당 보여줄 목록 개수
        paginator = Paginator(new, 10)
        now_page_number = request.GET.get("page", 1)
        page_list = paginator.get_page(now_page_number)
        tags=new.tags.all()


        context = {
            "page": paginator,
            "diary": new,
            "user": login_check,
            "page_list": page_list,
            "keyword": keyword,
        }
    # 검색 키워드가 없을때
    else:
        # 페이지 항목 추가
        paginator = Paginator(diary, 10)
        now_page_number = request.GET.get("page", 1)
        page_list = paginator.get_page(now_page_number)

        context = {
            "page": paginator,
            "posts": diary,
            "user": login_check,
            "page_list": page_list,
            "keyword": keyword,
        }

    return render(request, "ITDiary_list.html", context)



# 다이어리 페이지 더하기
def ITDiary_add(request):
    if request.method=="POST":
        title=request.POST["title"]
        content=request.POST["content"]

        diary=IT_Diary.objects.create(
            title=title,
            content=content,
        )
        return redirect("../../")
    else:
        pass

    context={
        "form":MyForm,
    }

    return render(request,"ITDiary_add.html",context)


def ITDiary_detail(request,itdiary_id):

    diary=IT_Diary.objects.get(id=itdiary_id)
    print(diary.author)
    print(diary.updated_at)
    print(diary.tags.all(),"tag")
    tags=diary.tags.all()

    #로그인 확인
    user=request.user
    login_check=user.is_authenticated
    print(user.id,"id")
    print(user.username,"이름")
    # 댓글 분류
    diary_comment=itdiary_Comment.objects.all()
    comment=[]

    for i in diary_comment:
        if i.diary.title==diary.title:
            comment.append([i.author,i.content])

    """
    if request.method=="POST":
        comment_content=request.POST["comment"]
        Comment.objects.create(
            diary=diary,
            content=comment_content,
        )
    """
    context={
        "diary" : diary,
        "tags" : tags,
        "comments" : comment, # 저자, 댓글 확인
        "login_check":login_check, #로그인 여부 확인
        "user_name":user.username, # 현재 로그인 사용자
    }

    """
    a=IT_Diary.objects.all()
    diary = a[len(a)-1]
    print(diary.content)
    print(diary.category)
    print(diary.tags.all)
    for i in diary.tags.all():
        print(i)

    context={
        "check":diary,

    }
    """

    return render(request,"ITDiary_detail.html",context)

#------------------------------------교체페이지 구성 부분--------------------------------------------------#
# 임시 페이지
# test world

def check(request):
    if request.user.is_authenticated:
        return redirect("../../users/login/feeds")
        # 피드 페이지 차후 재구성
        #return render(request, "users/feeds.html")

    if request.method== "POST":
        form =LoginForm(data=request.POST)
        username=request.POST["username"]
        password=request.POST["password"]

        if form.is_valid():
            #username=form.cleaned_data["username"]
            # 비밀번호를 숨기는 구조를 만들기 위해 재구성
            #password=form.cleaned_data["password"]

            user=authenticate(username=username,password=password)

            if user:
                login(request,user)
                # 처음 페이지로 돌아가기!
                return redirect("../../")

        context={"form": form}
        return render(request,"check.html",context)

    else:
        form=LoginForm()
        context={"form":form}
        return render(request,"check.html",context)

    #---- 이 이후는 항상 제거 금지 --->
    #return render(request,"check.html", context)