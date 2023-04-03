#for 반복문과 리스트
array=[273,32,103,57,52]

#리스트에 반복문을 적용합니다.

for element in array:
    print(element)
#주의 여기서 내림으로 잘못쓸 때 코딩이 이상한 결과가 나옴!
    #예시2
for a in "안녕하세요":
    print("-",a)
print()
print("다른결과 예시")
print()
for element in array:
    print(element)
#주의 여기서 내림으로 잘못쓸 때 코딩이 이상한 결과가 나옴!
    #예시2
    for a in "안녕하세요":
        print("-",a)

#2차원 행렬 for문

#방법1
n=int(input())
list_1=[]
for x in range(n):
    list_1.append(list(map(int,input().split()))) #list를 씌운 상태로 넣어야한다!

print(list_1)

list_2=[list(map(int,input().split())) for _ in range(n)]

print(list_2)



