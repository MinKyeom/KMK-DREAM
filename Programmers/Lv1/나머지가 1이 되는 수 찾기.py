# 내 풀이
def solution(n):
    for x in range(1,n):
        if n%x==1:
            return x


# 다른 사람 풀이
def solution(n):
    return [x for x in range(1,n+1) if n%x==1][0]