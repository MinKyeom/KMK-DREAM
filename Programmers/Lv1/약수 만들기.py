# 내 풀이
def solution(n):
    k = int(n ** (1 / 2))
    result = []
    for x in range(1, k + 1):
        if n % x == 0:
            a = n / x
            if a != x:
                result.append(x)
                result.append(a)
            else:
                result.append(x)

    return sum(result)


# 다른 사람 풀이
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
