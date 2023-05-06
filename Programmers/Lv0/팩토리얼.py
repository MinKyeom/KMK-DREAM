# 내 풀이

def solution(n):
    count=1
    x=1
    while True:
        for a in range(1,x+1):
            count*=a
        if count>n:
            return x-1
        elif count==n:
            return x
        elif count<n:
            x+=1
            count=1


# 다른 사람 풀이

from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k