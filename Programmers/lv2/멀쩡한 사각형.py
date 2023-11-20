# 내 풀이

def solution(w, h):
    result = 0

    if w == 1 or h == 1:
        return 0

    if h < w:
        for k in range(h):
            result += int((k * w / h))
    elif h == w:
        for k in range(w):
            return w * h - w
    else:
        for k in range(w):
            result += int(k * h / w)

    return result * 2


# 다른 사람 풀이
def gcd(a,b): return b if (a==0) else gcd(b%a,a)
def solution(w,h): return w*h-w-h+gcd(w,h)

# 다른 사람 풀이
from math import gcd
def solution(w,h):
    return w * h - (w/gcd(w, h) + h/gcd(w, h) - 1) * gcd(w, h)