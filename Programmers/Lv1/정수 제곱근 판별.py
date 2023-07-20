# 내 풀이
def solution(n):
    a=n**(1/2)
    if int(a)==a:
        return (a+1)**2
    else:
        return -1

# 다른 사람 풀이

def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'