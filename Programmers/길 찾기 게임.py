"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/42892
"""

# 내 풀이_개선 중
"""
전위순회:dfs
후위순회:자식 노드 없을 경우에 추가
"""
from collections import defaultdict
import heapq

def solution(nodeinfo):
    # 전위 순회
    before = []
    # 후위 순회
    after = []

    # point level
    level = defaultdict(list)

    # graph
    graph = defaultdict(list)

    # point search
    point_number = defaultdict(int)
    start = set()

    for num, node in enumerate(nodeinfo):
        point_number
        x, y = node[0], node[1]
        point_number[(x, y)] = num + 1
        level[y].append(x)
        start.add(y)

    start = list(start)
    start.sort(reverse=True)

    return 0