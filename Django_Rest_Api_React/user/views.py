from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from rest_framework import generics

# 회원 등록 시리얼라이저 가져오기
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

