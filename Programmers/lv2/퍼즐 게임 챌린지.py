"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/340212
"""

# 풀이 과정
# 이분 탐색(최솟값)
from collections import deque

def solution(diffs, times, limit):
    before = [0] * len(times)
    before[0] = times[0]

    for t in range(1, len(times)):
        before[t] = times[t - 1] + times[t]

    l = 1
    r = max(diffs) + 1
    result = float("inf")

    while l <= r:
        m = (l + r) // 2

        check = list(map(lambda x: max(0, x - m), diffs))
        t = 0

        for c in range(len(check)):
            if check[c] == 0:
                t += times[c]
            else:
                t += times[c]
                t += (before[c]) * (check[c])

        if t <= limit:
            r = m - 1
            result = min(result, m)
        else:
            l = m + 1

    return result

# 풀이 과정_ 개선 중
# 이분 탐색(최솟값)
from collections import deque


def solution(diffs, times, limit):
    left = 0
    right = max(diffs) + 1

    result = float("inf")

    while left < right:
        mid = (left + right) // 2

        # 걸린 시간
        t = 0

        k = list(map(lambda x: max(0, x - mid), diffs))

        while True:
            for n in range(len(times)):
                if k[n] > 1:
                    k[n] -= 1
                    t += times[n]
                    break
                else:
                    t += times[n]
            else:
                break

        if limit >= t:
            right = mid - 1
            result = min(mid, result)

        else:
            left = mid + 1

        print(t, mid)
    return result