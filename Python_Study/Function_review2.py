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