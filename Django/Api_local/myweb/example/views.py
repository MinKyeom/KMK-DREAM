# render 하는 부분은 이번 프로젝트에서 사용안함
# from django.shortcuts import render

# rest_framework 사용 모듈
from rest_framework import viewsets, permissions, generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET"])
def HelloAPI(request):
    return Response("hello")
