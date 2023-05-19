# 내 풀이
def solution(a, b):
    x=str(a)+str(b)
    x=int(x)
    y=2*a*b
    if x>y:
        return x
    elif x<y:
        return y
    else:
        return x
#다른 사람 풀이
def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)