"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/43238
"""

# 풀이 과정
def solution(n, times):
    times.sort()

    left = 0
    right = n * max(times)

    result = []

    while left <= right:
        count = 0
        mid = (left + right) // 2

        for t in times:
            count += (mid // t)
            if count > n:
                break

        if count >= n:
            right = mid - 1
            result.append(mid)

        else:
            left = mid + 1

    return min(result)