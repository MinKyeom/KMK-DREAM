# render 하는 부분은 이번 프로젝트에서 사용안함
# from django.shortcuts import render

# rest_framework 사용 모듈
from rest_framework import viewsets, permissions, generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404

# model 가져오기
from .models import Book

#시리얼라이저 가져오기
from .serializers import BookSerializer

# Create your views here.

@api_view(["GET"])
def HelloAPI(request):
    return Response("hello")

"""
참고 사항

FBV vs CBV
위의 @api_view는 FBV 형태이다

class 형 ex)

class HelloAPI(APIView):
    def get(self,request):
        return Response("hello")
"""

# 책 정보 모델을 받는 api
@api_view(['GET','POST'])
def booksapi(request):  # /books/ url로 정보를 받았을 때
    if request.method=='GET': # 도서 모델 가져오기
        books=Book.objects.all()
        #시리얼라이저에 전체 데이터를 한번에 집어넣기(직렬화, many=True)
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data ,status=status.HTTP_200_OK) #return Response!

    elif request.method =="POST":
        # Post 요청으로 들어온 데이터를 시리얼라이저에 집어넣기
        serializer=BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            # 성공 > 메세지 보내기
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def bookAPI(request,bid): #url book/bid 요청왔을때
    book=get_object_or_404(Book,book_id=bid) # bid=id인 데이터를 Bookdptj 가져오고, 없으면 404에러
    serializer=BookSerializer(book) # 시리얼라이저 직렬화

    return Response(serializer.data , status=status.HTTP_200_OK)