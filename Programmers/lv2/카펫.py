# 내 풀이
def solution(brown, yellow):
    result = []
    b = brown
    y = yellow

    k = b + y
    t = k
    while t >= k ** 0.5:
        a = k / t

        if a == int(a) and a > 2:
            if k - (2 * t + (a - 2) * 2) == y:
                return [int(t), int(a)]
            else:
                t -= 1

        else:
            t -= 1
    return 0

# 다른 사람 풀이

def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]