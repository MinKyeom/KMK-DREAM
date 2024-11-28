"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/181858
"""

# 내 풀이
def solution(arr, k):
    result = []
    for x in arr:
        if x not in result and len(result) < k:
            result.append(x)
        else:
            continue

    if len(result) < k:
        g = k - len(result)
        for l in range(g):
            result.append(-1)

    return result

# 다른 사람 풀이
def solution(arr, k):
    ret = []
    for i in arr:
        if i not in ret:
            ret.append(i)
        if len(ret) == k:
            break

    return ret + [-1] * (k - len(ret))
