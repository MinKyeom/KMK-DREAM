"""
출처: 프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/49189
"""

# 내 풀이
"""
다익스트라 알고리즘
"""

from collections import defaultdict
from collections import deque


def solution(n, edge):
    m = defaultdict(list)

    distance = [float("inf")] * (n + 1)
    distance[0], distance[1] = 0, 0

    for x, y in edge:
        m[x].append(y)
        m[y].append(x)

    q = deque([(1, 0)])

    while q:
        # 목적지, 거리
        end, k = q.popleft()

        for i in m[end]:
            if distance[i] > (k + 1):
                q.append((i, k + 1))
                distance[i] = (k + 1)

    r = max(distance)

    return distance.count(r)