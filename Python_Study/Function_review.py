#기본적인 함수

def print_2_times():
    print("안녕하세요")
    print("안녕하세요")

print_2_times() #들여쓰기 위치 확인!!

# 매개변수의 기본

def print_n_times(value,n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요",6)

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

def sum_all2(s=0,e=100,step=1):
    output=0
    for i in range(s,e+1,step):
        output+=i
    return output


print(sum_all2(0,100,10))
print(sum_all2(e=100))
print(sum_all2(e=100,step=2))

