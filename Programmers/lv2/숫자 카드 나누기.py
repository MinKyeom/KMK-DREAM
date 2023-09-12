# 내 풀이
def solution(arrayA, arrayB):
    a = min(arrayA)
    b = min(arrayB)
    check_a_b = []
    check_b_a = []
    result = []

    for x in range(1, int(a ** 0.5) + 1):
        if a % x == 0:
            check_a_b.append(int(x))
            if x != (a / x):
                check_a_b.append(int(a / x))
    for y in range(1, int(b ** 0.5) + 1):
        if b % y == 0:
            check_b_a.append(int(y))
            if x != (b / y):
                check_b_a.append(int(b / y))

    for k in check_a_b:
        for t in range(len(arrayA)):
            if arrayA[t] % k == 0 and arrayB[t] % k != 0:
                if t == len(arrayA) - 1:
                    result.append(k)
            else:
                break

    for k in check_b_a:
        for t in range(len(arrayA)):
            if arrayB[t] % k == 0 and arrayA[t] % k != 0:
                if t == len(arrayB) - 1:
                    result.append(k)
            else:
                break

    return max(result) if len(result) > 0 else 0

# 다른 사람 풀이
from math import gcd
from functools import reduce

def check(arrayA, arrayB):
    gcd_A = reduce(gcd, arrayA, arrayA[0])
    factors = [i for i in range(1, gcd_A//2+1) if not gcd_A % i]
    factors.append(gcd_A)
    for factor in factors[::-1]:
        if all(i % factor for i in arrayB):
            return gcd_A
    return 0

def solution(arrayA, arrayB):
    return max(check(arrayA, arrayB), check(arrayB, arrayA))