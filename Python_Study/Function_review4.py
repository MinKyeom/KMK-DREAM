tuple_test=(10,20,30)

print(tuple_test[0])

#리스트와 튜플의 특이한 사용
[a,b]=[10,20]
(c,d)=(10,20)
print()
print()
print(a)
print(b)
print(c)
print(d)

#괄호가 없는 튜플

tuple_test2=10,20,30,40
print(tuple_test2)
print(type(tuple_test2))
print()
print()
#변수의 값을 교환하는 튜플

e,f=10,20

print("e:",e)
print("f:",f)

print("교환 후")

e,f=f,e

print("e:",e)
print("f:",f)

#여러 개의 값 리턴하기
def test():
    return(10,20)

g,h=test()

print(g,h)

#함수의 매개 변수로 함수 전달하기

def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("안녕하세요")

call_10_times(print_hello)

#map() filter()

def power(item):
    return item*item
def under_3(item):
    return item<3

list_a=[1,2,3,4,5]

output_a=map(power,list_a)
print()
print(output_a)
print(list(output_a))
print()

output_b=filter(under_3,list_a)
print(output_b)
print(list(output_b))
print()
print()
#람다

power_1=lambda x:x*x
under_4=lambda x:x<3

list_b=[1,2,3,4,5]

output_c=map(power,list_b)
output_d=filter(under_4,list_b)

print(list(output_c))
print(list(output_d))

#인라인 람다
list_c=[1,2,3,4,5]

output_e=map(lambda x:x*x,list_c)
output_f=filter(lambda x:x<3,list_c)
print()
print(list(output_e))
print(list(output_f))

#파일 열고 닫기

file =open("basic.txt","w")
file.write("Hello")
file.close()

#read() 함수로 텍스트 읽기

with open("basic.txt","r") as file:
    contents =file.read()
print(contents)

#랜덤하게 1000명의 키와 몸무게 만들기

import random

hanguls =list("가나다라마바사아자차카타파하")
with open("info.txt","w") as file:
    for i in range(1000):
        name =random.choice(hanguls)+random.choice(hanguls)
        weight=random.randrange(40,100)
        height=random.randrange(140,200)

        file.write("{},{},{}\n".format(name,weight,height))



#반복문으로 파일 한 줄씩 읽기
with open("info.txt","r") as file:
    for line in file: