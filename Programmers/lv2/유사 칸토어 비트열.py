# 내 풀이 (아직 개선중)
def solution(n, l, r):
    k = "11011"
    count = 1
    count_l = 0
    count_r = 0
    while len(k) <= r:
        count += 1
        k = k * 2 + "0" * (5 ** (count - 1)) + k * 2

    result = k[l - 1:r].count("1")

    return result

# 풀이2
def solution(n, l, r):
    if n == 0:
        return 1
    if l > 1:
        return solution(n, 0, r) - solution(n, 0, l - 1)

    if r <= 5 ** (n - 1):
        return solution(n - 1, 1, r)

    elif r <= 2 * 5 ** (n - 1):
        return 4 ** (n - 1) + solution(n - 1, 1, r - 5 ** (n - 1))

    elif r <= 3 * 5 ** (n - 1):
        return 4 ** (n - 1) * 2

    elif r <= 4 * 5 ** (n - 1):
        return 4 ** (n - 1) * 2 + solution(n - 1, 1, r - 5 ** (n - 1) * 3)

    elif r <= 5 * 5 ** (n - 1):
        return 4 ** (n - 1) * 3 + solution(n - 1, 1, r - 5 ** (n - 1) * 4)

    return 1

# 다른 사람 풀이
def solution(n, l, r):
    answer = r-l+1
    for num in range(l-1,r):
        while num>=1:
            a,b=divmod(num,5)
            if b==2 or a==2:
                answer-=1
                break
            num=a


    return answer


