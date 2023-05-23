# 내 풀이
def solution(ineq, eq, n, m):
    if eq=="=":
        x=str(n)+ineq+eq+str(m)
        if eval(x):
            return 1
        else:return 0
    else:
        x=str(n)+ineq+str(m)
        if eval(x):
            return 1
        else:return 0

# 다른 사람 풀이
def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))

