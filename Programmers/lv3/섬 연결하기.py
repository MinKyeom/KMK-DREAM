"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/42861
"""

from collections import defaultdict, deque
import copy


def solution(n, costs):
    # 비용
    c = defaultdict(int)
    # 연결 경로
    r = defaultdict(set)
    result = float("inf")
    check = []

    for a, b, cost in costs:
        r[a].add(b)
        r[b].add(a)
        c[(a, b)] = cost
        c[(b, a)] = cost

    island = [float("inf")] * (n)
    island_check = defaultdict(list)

    # 자기자신으로 돌아오는 길
    island[0] = 0

    check = deque([k for k in range(n)])

    while check:
        s = check.popleft()
        island = [float("inf")] * (n)
        island_check = defaultdict(list)

        # 자기자신으로 돌아오는 길
        island[s] = 0

        q = deque([])

        # (start,arrive,cost), 0에서 arrive로 가는 비용의 최솟값을 나열
        for i in r[s]:
            q.append((s, i, 0, []))

        while q:
            start, end, cost, road = q.popleft()

            if cost + c[(start, end)] <= island[end]:
                island[end] = cost + c[(start, end)]
                new = copy.deepcopy(road)
                island_check[end] = new + [(start, end)]

                for i in r[end]:
                    q.append((end, i, cost + c[(start, end)], road + [(start, end)]))

        road = set([])

        for road_num, path in island_check.items():
            for p in path:
                road.add(p)

        count = 0

        for i in road:
            count += c[i]

        result = min(result, count)

    return result