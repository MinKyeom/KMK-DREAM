"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/42579
"""


# 내 풀이
from collections import defaultdict


def solution(genres, plays):
    g = defaultdict(int)
    g_num = defaultdict(list)

    for i in range(len(genres)):
        g[genres[i]] += plays[i]
        g_num[genres[i]].append((plays[i], i))

    check = []

    for k in g_num.keys():
        g_num[k].sort(key=lambda x: (-x[0], x[1]))
        check.append((g[k], k))

    check.sort(reverse=True)

    result = []

    for i, j in check:
        n = 0
        for count, num in g_num[j]:
            result.append(num)
            n += 1
            if n == 2:
                break

    return result