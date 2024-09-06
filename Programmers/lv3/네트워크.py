"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/43162
"""
# 내 풀이
from collections import defaultdict
from collections import deque
import copy


def solution(n, computers):
    network = defaultdict(set)
    result = []

    for i in range(len(computers)):
        network[i].add(i)
        for j in range(len(computers[0])):
            if computers[i][j] == 1:
                network[i].add(j)
                network[j].add(i)

    check = deque([i for i in range(n)])

    visit = set([])

    new = set([])

    while check:
        start = check.popleft()

        if start in visit:
            continue

        q = deque([start])

        while q:
            v = q.popleft()
            visit.add(v)
            new.add(v)

            for end in network[v]:
                if not end in visit and not end in new:
                    q.append(end)

        net = copy.deepcopy(new)

        result.append(net)

    return len(result)