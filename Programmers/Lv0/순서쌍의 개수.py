# 내 풀이

def solution(n):
    from itertools import combinations
    num=[]
    for a in range(1,n+1):
        if n%a==0:
            num.append(a)
    return len(num)

# 다른 사람 풀이

def solution(n):
    return len(list(filter(lambda v: n % (v+1) == 0, range(n))))
