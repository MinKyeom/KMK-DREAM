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
print()

# 리스트 중간에 요소 추가하기
print("# 리스트 중간에 요소 추가하기")
list_3.insert(0,10)
print(list_3)

# 한번에  여러 개를 추가
list_4=[1,2,3]
print(list_4)
list_4.extend([4,5,6])
print(list_4)
print(list_1+list_2)

#extend 활용
list_5=[1,2,3]
list_6=[4,5,6]
print(list_5)
list_5.extend(list_6) # print(list_5.extend(list_6)은 참고로 인식을 못했다.
print(list_5)

#인데스로 제거하기:del,pop

#리스트 연결 연산자와 요소 추가의 차이
list_7=[0,1,2,3,4,5]
print("# 리스트의 요소 하나 제거하기")
print(list_7)
# 제거 방법[1]
del list_7[1]
print("del list_7[1]",list_7)

#제거 방법[2]
list_7.pop(2)
print("pop(2)",list_7)

#범위로 제거하기
list_8=[0,1,2,3,4,5,6,7,8,9]
del list_8[3:6]
print(list_8)

#범위 한쪽을 지우기
list_9=[1,2,3,4,5,6,7,8,9]
print("지우기전 ",list_9)
del list_9[:3]
print("지운 후",list_9)

list_10=[1,2,3,4,5,6,7,8,9]
print("지우기 전")
del list_10[3:]
print("지운 후",list_10)
