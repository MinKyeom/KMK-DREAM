# 내 풀이
def solution(n):
    k=list(str(n))
    k.sort(reverse=True)
    return int("".join(k))


# 다른 사람 풀이
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))