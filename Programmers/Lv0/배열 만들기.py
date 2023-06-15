# 내 풀이
def solution(n, k):
    result = []
    for x in range(1, n + 1):
        if x % k == 0:
            result.append(x)

    return result

# 다른 사람 풀이
def solution(n, k):
    return [i for i in range(k,n+1,k)]