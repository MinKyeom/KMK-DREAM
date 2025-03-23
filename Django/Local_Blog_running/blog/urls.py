from django.urls import path
from blog.views import login_view,login_feeds,loginout_view

urlpatterns=[
    path("login/",login_view),
    path("login/feeds/",login_feeds),
    path("logout/",loginout_view),
]