"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/12979
"""

# 내 풀이
def solution(n, stations, w):
    net = [False] * n
    check = set(stations)
    for s in stations:
        s = s - 1
        min_num = max(0, s - w - 1)
        max_num = min(n - 1, s + w + 1)

        for n in range(min_num, max_num + 1):
            net[n] = True

    result = 0

    for t in range(w + 1, n, 2 * w + 1):
        if not ((t - 1) // 2) + 1 + 1 in check:
            result += 1

    return result + len(check)

