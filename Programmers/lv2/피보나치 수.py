# 내 풀이
def solution(n):
    count = 2
    func_1 = 1
    func_0 = 0
    while count <= n:
        count += 1
        func_2 = func_1 + func_0
        result = func_2
        func_1, func_0 = func_2, func_1

    return result % 1234567

# 다른 사람 풀이

def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
    return a