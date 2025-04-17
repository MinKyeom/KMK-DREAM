"""
FastApi를 써야하는 이유?
> 빠른 속도 및 범용적으로 사용이 가능,비동기 사용 
"""

"""
개발 순서

1.입출력 스펙 정하기

2.기능 구현 

3.데스트 

4.입출력 값 검증

1~4까지 pydantic 모듈 사용 

"""

"""
5. 작성한 api는 자동으로 생성되는 api문서를 통해 손쉽게 테스트 가능

5번 과정은 python module을 활용하여 구현
"""

#Simple fastapi test

from fastapi import FastAPI

app=FastAPI()

@app.get("/") # GET 메소드로 가장 루트 url로 접속할 경우
async def root(): # root() 함수를 실행하고
    return {"message":"Hi FastApi"} # Hello World란 메시지 반환합니다.

"""
Tip 및 의미 이해

현업에서 간단하게 구현하는 이유 > 바로 서버로 보내는 것이 가능하고 빠른 일처리 가능

실행: uvicorn (현재 작성한 python 파일 이름):app --reload

async는 비동기(asynchronous)를 의미하는 키워드로, 다양한 프로그래밍 언어에서 사용됩니다. 

비동기란 작업이 완료되지 않아도 다음 코드를 실행하는 방식을 말합니다. 

"""

# test 2
@app.get("/check") ######## 1
async def check():
    return {"message":"check"}

"""
테스트 결과 > 1번의 경로와 동일한 경로가 존재한다면 해당 함수는 실행되지 않는다
함수는 이 메시지의 이름을 부여한 느낌이다.
Django는 crud가 강한 편이다.  
"""