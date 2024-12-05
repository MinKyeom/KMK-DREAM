"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/340212
"""

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