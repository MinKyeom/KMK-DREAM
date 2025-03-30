from django.urls import path,include
from .views import HelloAPI,bookAPI,booksapi,Booksapi,BookAPI,BooksAPIMixins,BookAPIMixins

urlpatterns=[
    path("hello/",HelloAPI),
    # 함수형 뷰
    path("fbv/books/",booksapi),
    path("fbv/book/<int:bid>/",bookAPI),

    # 클래스형 뷰
    path("cbv/books/",Booksapi.as_view()),
    path("cbv/book/<int:bid>/",BookAPI.as_view()),

    #mixin
    path("mixin/books/",BooksAPIMixins.as_view()),
    #book_id 랑 views.py에 있는 lookup_field와 일치하게 하기!!!
    path("mixin/book/<int:book_id>/",BookAPIMixins.as_view()),

]