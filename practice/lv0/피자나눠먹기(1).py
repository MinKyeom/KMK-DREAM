# 내 풀이
def solution(n):
    count=1
    while True:
        if (7*count)/n>=1:
            return count
        else:count+=1
# 다른 사람 풀이
def solution(n):
    return (n - 1) // 7 + 1