"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/92335
"""
# 풀이과정
def solution(n, k):
    result = 0
    a = ""
    while True:
        if k == 10:
            break
        t = n % k
        a += str(t)
        n = int(n / k)
        if n < k:
            a += str(n)
            break

    a = a[::-1]

    if k == 10:
        a = str(n)

    # print(a)

    b = a.split("0")

    if k == 10:
        for c in b:
            count = 0
            if c.isdigit() == True and int(c) != 1:
                for d in range(1, int(int(c) ** 0.5) + 1):
                    if int(c) % d == 0:
                        count += 1
                        if count > 1:
                            break
                if count == 1:
                    result += 1

    else:
        print(b)
        for c in b:
            count = 0
            if c.isdigit() == True and int(c) != 1:
                for d in range(1, int(int(c) ** 0.5) + 1):
                    if int(c) % d == 0:
                        count += 1
                        if count > 1:
                            break
                if count == 1:
                    result += 1

    print(result)

    return result

# 다른 사람 풀이
def conv(n, k):
    s = ''
    while n:
        s += str(n%k)
        n //= k
    return s[::-1]

# n이 소수인지 판정
def isprime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

def solution(n, k):
    s = conv(n,k)
    cnt = 0
    for num in s.split('0'):
        if not num: continue # 빈 문자열에 대한 예외처리
        if isprime(int(num)): cnt += 1
    return cnt