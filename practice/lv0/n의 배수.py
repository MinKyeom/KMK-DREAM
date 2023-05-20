# 내 풀이
def solution(num, n):
    if num%n==0:
        return 1
    else:return 0


# 다른 사람 풀이
def solution(num, n):
    return int(not(num % n))