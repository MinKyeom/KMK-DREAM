"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/72413
"""

# 내 풀이
"""
생각방향: 다익스트라 알고리즘 
각각으로 구하는것과 개별로 구하는 것 중 최소값으로 구하기
두 명 요금의 합이 최소가 되는 조건
"""

from collections import defaultdict
from collections import deque
import heapq

# 요금
f = defaultdict(list)
# 연결된 경로
d = defaultdict(list)


def diikstra_road(start, n):
    # 최소 경로 갱신
    v = [float("inf")] * (n + 1)

    # 경로를 저장
    order = [[]] * (n + 1)

    # 처음 부분 0
    v[start] = 0

    q = []

    heapq.heappush(q, [0, start, []])

    while q:
        now_fare, now_dir, o = heapq.heappop(q)

        if v[now_dir] < now_fare:
            continue

        for end in d[now_dir]:
            if v[end] > now_fare + f[(now_dir, end)]:
                v[end] = now_fare + f[(now_dir, end)]
                new = o[:]
                new.append(end)
                order[end] = new
                heapq.heappush(q, [now_fare + f[(now_dir, end)], end, new])

    return v, order


def diikstra(start, n):
    # 최소 경로 갱신
    v = [float("inf")] * (n + 1)

    # 처음 부분 0
    v[start] = 0

    q = []

    heapq.heappush(q, [0, start])

    while q:
        now_fare, now_dir = heapq.heappop(q)

        if v[now_dir] < now_fare:
            continue

        for end in d[now_dir]:
            if v[end] > now_fare + f[(now_dir, end)]:
                v[end] = now_fare + f[(now_dir, end)]
                heapq.heappush(q, [now_fare + f[(now_dir, end)], end])

    return v


def solution(n, s, a, b, fares):
    global f, d

    for i, j, k in fares:
        f[(i, j)] = k
        f[(j, i)] = k
        d[i].append(j)
        d[j].append(i)

    # s>a,s>b
    v, order = diikstra_road(s, n)
    v = diikstra(s, n)

    result = float("inf")

    # 어느 지점까지 동승 후 재 배열
    for i in range(1, n + 1):
        count = 0
        count += v[i]

        v_new = diikstra(i, n)

        # a 목적지
        count += v_new[a]

        # b 목적지
        count += v_new[b]

        result = min(count, result)

    return result

# 다른 사람 풀이
import heapq

def solution(n, s, a, b, fares):
    d = [ [ 20000001 for _ in range(n) ] for _ in range(n) ]
    for x in range(n):
        d[x][x] = 0
    for x, y, c in fares:
        d[x-1][y-1] = c
        d[y-1][x-1] = c

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if d[j][k] > d[j][i] + d[i][k]:
                    d[j][k] = d[j][i] + d[i][k]

    minv = 40000002
    for i in range(n):
        minv = min(minv, d[s-1][i]+d[i][a-1]+d[i][b-1])
    return minv