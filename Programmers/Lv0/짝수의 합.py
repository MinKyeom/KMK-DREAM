# 내 풀이
def solution(n):
    count=0
    for x in range(n+1):
        if x%2==0:
            count+=x
    return count


# 다른 사람 풀이

def solution(n):
    return sum([i for i in range(2, n + 1, 2)])