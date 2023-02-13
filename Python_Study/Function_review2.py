def factorial(n):

    output=1

    for i in range(1,n+1):
        output *=i
    return output

print("factorial(1):",factorial(1))
print("factorial(2):",factorial(2))

#재귀 함수를 사용해 팩토리얼 구하기
print()
print()
def factorial_1(n):

    if n==0:
        return 1
    else:
        return n*factorial_1(n-1)

print(factorial_1(1))
print(factorial_1(2))
print()
print()

#재귀 함수로 구현한 피보나치 수열

def fibonacci(n):

    if n==1:
        return 1
    if n==2:
        return 2

    else:
        return fibonacci(n-1) +fibonacci(n-2)

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))

print()
print()

#재귀 함수로 구현한 피보나치 수열(2)

a=0

def fibo(n):
    print("fibo{}".format(n))
    global a
    a +=1

    if n==1:
        return 1

    if n==2:
        return 1

    else:
        return fibo(n-1)+fibo(n-2)
fibo(10)

print("---")
print("덧셈 횟수는{}".format(a))


#메모화

dic={
    1:1,
    2:1
}

def fibo_2(n):
    if n in dic:
        return dic[n]
    else:
        output=fibo(n-1)+fibo(n-2)
        dic[n]=output
        return output
print(fibo(10))

