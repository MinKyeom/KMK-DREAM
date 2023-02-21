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