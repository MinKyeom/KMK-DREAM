#풀이1
def solution(a, b):
    if b%2==0 or b%5==0:
        while True:
            if b%2==0:
                b=b/2
            else:break
        while True:
            if b%5==0:
                b=b/5
            else:break
        if b==1:
            return 1
        else:
            if a%b==0:
                return 1
            else:
                return 2
    else:return 2

#풀이2

from math import gcd
def solution(a, b):
    b //= gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2