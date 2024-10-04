"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/42861
"""
# 내 풀이 개선 중
"""
중간에 빠진 사고 과정:중복된 도로를 제거 안함
"""
from collections import defaultdict, deque
import copy


def solution(n, costs):
    # 비용
    c = defaultdict(int)
    # 연결 경로
    r = defaultdict(set)
    result = float("inf")
    island = set([])
    all_road = set([])
    for a, b, cost in costs:
        all_road.add((a, b))
        all_road.add((b, a))
        r[a].add(b)
        r[b].add(a)
        c[(a, b)] = cost
        c[(b, a)] = cost
        island.add(a)
        island.add(b)

    # 각 섬의 최단 경로 재갱신 모두 비교
    island = deque(list(island))
    while island:
        is_ = island.popleft()
        q = deque([])
        visit = [float("inf")] * n
        # visit[is_]=0

        visit_navi = defaultdict(list)

        for i in r[is_]:
            q.append((is_, i, 0, []))

        while q:
            start, end, cost, navi = q.popleft()

            if cost + c[(start, end)] < visit[end]:
                visit[end] = cost + c[(start, end)]
                visit_navi[end] = navi + [(start, end), (end, start)]

                for new in r[end]:
                    q.append((end, new, cost + c[(start, end)], navi + [(start, end), (end, start)]))

        # 최종 경로 비용 산출
        count = 0
        check_road = set([])

        for end, navi in visit_navi.items():
            check_road = check_road | set(navi)

        all_road = all_road & check_road
        print(all_road)

    for build in all_road:
        count += c[build]

    # result=min(result,count//2)

    return count
# 내 풀이 개선 중
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

    q = deque([])

    # (start,arrive,cost), 0에서 arrive로 가는 비용의 최솟값을 나열
    for i in r[0]:
        q.append((0, i, 0, [0, i]))

    while q:
        start, end, cost, road = q.popleft()

        if cost > result:
            continue

        if len(set(road)) == n:
            check.append(cost)
            result = min(result, cost + c[(start, end)])

        for i in r[end]:
            q.append((end, i, cost + c[(start, end)], road + [i]))

    return result

# 내 풀이 개선중
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