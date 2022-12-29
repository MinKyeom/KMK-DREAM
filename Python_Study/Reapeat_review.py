# list review

list_a=[273,32,103,"문자열",True,False]
print(list_a[0])

list_a[0]="변경" #리스트 변경

print(list_a[0])

print(list_a[3][0])

#리스트 연산자 연결 반복 len

list_1=[1,2,3]

list_2=[4,5,6]

print("#리스트 ")
print("list_1=",list_1)
print("list_2=",list_2)

print()

#기본 연산자
print("#리스트 기본 연산자")
print("list_1 + lost_2=",list_1+list_2)
print("list_1*3=",list_1*3)

print()

#함수

print("#길이 구하기")
print("len(list_1)=",len(list_1))

#리스트에 요소 추가하기

list_3=[1,2,3]

print("리스트 뒤에 요소 추가하기")
list_3.append(4)
list_3.append(5)

print(list_3)