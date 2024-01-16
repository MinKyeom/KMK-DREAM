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


# 다른 사람 풀이 