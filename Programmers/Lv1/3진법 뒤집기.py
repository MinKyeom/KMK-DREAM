# 내 풀이
def solution(n):
    a = ""
    while True:
        if n < 3:
            a = str(n) + a
            break
        n, x = int(n / 3), n % 3
        a = str(x) + a
    a = a[::-1]
    k = list(a)

    result = 0
    count = len(k) - 1
    for x in range(len(k)):
        result += (3 ** count) * int(k[x])
        count -= 1

    return result

# 다른 사람 풀이
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer