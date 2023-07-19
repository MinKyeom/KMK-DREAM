# 내 풀이
def solution(n, m):
    a = int(n ** (1 / 2))
    a_list = []
    b = int(m ** (1 / 2))
    b_list = []

    for x in range(1, a + 1):
        if n % x == 0:
            x_1 = int(n / x)
            if x_1 != x:
                a_list.append(x)
                a_list.append(x_1)
            else:
                a_list.append(x)
    for y in range(1, b + 1):
        if m % y == 0:
            y_1 = int(m / y)
            if y_1 != y:
                b_list.append(y)
                b_list.append(y_1)
            else:
                b_list.append(y)

    c = list(set(a_list) & set(b_list))
    c.sort(reverse=True)
    v = c[0]

    if n % m == 0:
        w = n
    elif m % n == 0:
        w = m
    else:
        d_1 = [n * k for k in range(1, m + 1)]
        d_2 = [m * k for k in range(1, n + 1)]
        d_3 = min(list(set(d_1) & set(d_2)))
        w = d_3
    return [v, w]

# 다른 사람 풀이
def gcdlcm(a, b):
    c,d = max(a, b), min(a, b)
    t = 1
    while t>0:
        t = c%d
        c, d = d, t
    answer = [ c, int (a*b/c)]
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))