# 내 풀이(개선 중)
import math
import math


def solution(n, k):
    p = [a for a in range(1, n + 1)]
    result = []

    while p:
        t = (k - 1) // math.factorial(n - 1)
        result.append(p.pop(t))

        k = (k) % math.factorial(n - 1)
        n -= 1

    return result


import math


def solution(n, k):
    p = [a for a in range(1, n + 1)]
    result = []

    while p:
        t = (k) // (math.factorial(n - 1))
        k = (k) % math.factorial(n - 1)

        if k != 0:
            result.append(p.pop(t))
        else:
            result.append(p.pop(t - 1))

        n -= 1

    return result


"""
def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)

def solution(n, k):
    # 총 n!의 경우의 수를 갖고있음
    # 맨 앞의 수가 정해지면 (n - 1)! 의 경우의 수를 가짐
    # k에서 (n - 1)!을 나눴을 때의 몫이 첫번째 오는 자리
    # k에서 (n - 1)!을 나눴을 때의 나머지가 다시 k로 오는 자리
    result = []
    num_list = [i for i in range(1, n + 1)]
    while(n != 0):
        num_case = factorial(n - 1)
        idx = k // num_case
        k = k % num_case
        if k == 0:
            result.append(num_list.pop(idx - 1))
        else:
            result.append(num_list.pop(idx))
        n -= 1
    return result
"""

