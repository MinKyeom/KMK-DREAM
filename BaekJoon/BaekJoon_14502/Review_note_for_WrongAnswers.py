# 2차원 배열을 입력 받을때
"""
표현1: spot=[list(map(int,input().split())) for a in range(N)]

표현2:
    for x in range(N):
        list(map(int,input().split())
"""

#표현을 통해 배운 부분

"""N=int(input())

spot_1=[]  

# 주의사항 밑에 줄의 spot의 경우 그냥 리스트로 정의 할 시 오류 발생 spot_1만 리스트 선언 필요!

spot=[list(map(int,input().split())) for a in range(N)]

print("spot",spot)

print()

for x in range(N):
    spot_1.append(list(map(int,input().split())))

print("spot_1",spot_1)

"""

# def를 쓰는 의미

"""
같은 코딩을 반복적으로 칠 필요없이 쓸 수 있다..
"""

# zip 내장함수

"""
#zip
a=[1,2,3,4,5]
b=["사과","딸기","메론"]

for x in zip(a,b):
    print(x)
    
print()

# 비슷한 표현

for y in range(3):
    new=(a[y],b[y])
    print(new) #양측의 데이터를 하나씩 짝지어준다
      
"""
