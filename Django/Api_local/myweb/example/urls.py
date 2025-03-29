from django.urls import path,include
from .views import HelloAPI,bookAPI,booksapi

urlpatterns=[
    path("hello/",HelloAPI),
    path("fbv/books/",booksapi),
    path("fbv/book/<int:bid>/",bookAPI),

]