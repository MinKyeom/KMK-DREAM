# 내 풀이
def solution(n):
    k=list(str(n)[::-1])
    k=list(map(int,k))
    return k

# 다른 사람 풀이
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
