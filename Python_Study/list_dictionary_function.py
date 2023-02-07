a=[10,15,20]
print(min(a))
print(max(a))
print(sum(a))

#reversed

a_reversed =reversed(a)
print("reversed:",a_reversed)
print("list(reversed([10,15,20]:",list(a_reversed))

#[::-1]

print("[::-1]:",a[::-1])
print()
print()

#enumerate

b=["요소1","요소2","요소3"]
print("기본 출력")
print(b)
print()

print(" enumerate 적용")
print(enumerate(b))
print()

print("list로 다시 강제 변환")
print(list(enumerate(b)))
print()

print("반복문 추가")
for i,value in enumerate(a):
    print("{}번째 요소는 {} 입니다".format(i,value))

#dictionary items() 반복문 조합

dictionary={
    "key1":"a",
    "key2":"b",
    "key3":"c"
}

print(dictionary.items())

for key,element in dictionary.items():
    print("dictionary[{}]={}".format(key,element))

#list 내포
array=[]
for e in range(0,20,2):
    array.append(e*e)
print(array)#for문에 안걸리게 하는거 주의하기!

array_2=[f*f for f in range(0,20,2)]

print(array_2)

array_3=["사과","자두","초콜릿","바나나","체리"]
output=[fruit for fruit in array_3 if fruit !="초콜릿"]
print(output)


#괄호로 문자열 연결하기

test=(
    "이렇게 입력해도 "
    "하나의 문자열로 연결되어"
    "생성 됩니다."
)

#출력합니다.
print("test: ",test)

# 쉼표로 연결하기

test_2=(
    "이렇게 입력하면",
    "하나의 문자열로 연결되지",
    "않습니다."
)
print("test_2:",test_2)

#여러 줄 문자열과 if 구문을 조합 했을 때의 문제해결

#n= int(input("정수 입력:"))

#if n%2 ==0:
#    print(("{}은(는) 짝수 입니다").format(n))

#else:
#    print(("{}은 짝수가 아닙니다.").format(n))


# 문자열의 join() 함수

print("::".join(["1","2","3","4","5","6"])) # 문자열이라는 사실!!

#여러 줄 문자열과 if 구문을 조합했을 떄의 문제 해결
#n_2=int(input("정수 입력:"))
#if n_2%2 ==0:
#    print("\n".join([
#        "입력한 문자열은 {} 입니다.",
#        "{}는(은) 짝수입니다."
#    ]).format(n_2,n_2))
#else:
#    print("\n".join([
#        "입력한 문자열은 {}입니다.",
#        "{}는(은) 홀수 입니다."
#    ]).format(n_2,n_2))

#reversed() 함수와 이터레이터

n_3=[1,2,3,4,5,6]
r_n=reversed(n_3)
print(r_n)
print(next(r_n))
print(next(r_n))
print(next(r_n))
print(next(r_n))
print(next(r_n))

#가변 매개변수 함수
def print_s_times(n,*values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_s_times(3,"안녕하세요","즐거운","파이썬")

# 기본 매개변수

def print_r_times(value,n=2):
    for i in range(n):
        print(value)
print_r_times("안녕하세요")

#print_s_times(3,"안녕하세요","즐거운","파이썬") # 함수를 한 번 작성해놓으면 리턴 값은 언제든 다시 불러오는거 가능

#키워드 매개변수

def print_t_times(*values,n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()
print_t_times("안녕하세요","즐거운","파이썬",n=3)

#여러 함수 호출 형태

def test(a,b=10,c=100):
    print(a+b+c)
test(10,20,30)

test(a=10,b=100,c=200)

test(c=10,a=100,b=200)

#리턴값의 정의 탐구
#value= input(">")
#print(value)

#자료 업이 리턴하기

def return_test():
    print("A 위치입니다.")
    return
    print("B 위치입니다.")
return_test() #리턴을 중간에 썼기에 B는 나오지 않는다.

#자료와 함께 리턴하기

def return_test_2():
    return 100
print()
value=return_test_2()
print(value)
print()
#아무것도 리턴하지 않았을 때

def return_test_3():
    return

value_2=return_test_3()
print(value_2)


#범위 내부의 정수를 모두 더하는 함수

def sum_all(start,end):

    output=0

    for i in range(start,end+1):
        output+=i

    return output
print(sum_all(0,10))


#기본 매개변수와 키워드 매개변수를 활용해 범위의 정수를 더하는 함수





