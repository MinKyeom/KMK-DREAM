"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/42892
"""
# 내 풀이_ 개선 중
"""
전위순회:dfs
후위순회:자식 노드 없을 경우에 추가
"""
from collections import defaultdict, deque
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

    start = deque(start)
    top_point = start.popleft()

    visit = set()
    visit.add(point_number[(level[top_point][0], top_point)])

    now_point = point_number[(level[top_point][0], top_point)]
    now_x = level[top_point][0]
    now_y = top_point

    #     while start:
    #         y=start.popleft()
    #         for x in level[y]:
    #             num=point_number[(x,y)]

    return 0

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

# 다른 사람 풀이
from collections import defaultdict
import sys

sys.setrecursionlimit(1005)
MAX = 100001
MIN = -1
TREE_DEPTH = 0


def solution(nodeinfo):
    global TREE_DEPTH

    pre_tree = defaultdict(list)
    post_tree = defaultdict(list)
    level = set()

    for i in range(len(nodeinfo)):
        x, y = nodeinfo[i]
        pre_tree[y].append((x, i + 1))
        post_tree[y].append((x, i + 1))
        level.add(y)

    for i in level:
        pre_tree[i].sort(reverse=True)
        post_tree[i].sort(reverse=True)

    level = sorted(list(level), reverse=True)
    TREE_DEPTH = len(level)

    preorder = []
    pre_order(MIN, MAX, 0, preorder, pre_tree, level)
    postorder = []
    post_order(MIN, MAX, 0, postorder, post_tree, level)

    return [preorder, postorder]


def pre_order(left, right, depth, result, tree, level):
    if depth == TREE_DEPTH:
        return
    if len(tree[level[depth]]) <= 0:
        return
    if not (left < tree[level[depth]][-1][0] < right):
        return

    x, index = tree[level[depth]].pop()
    result.append(index)
    pre_order(left, x, depth + 1, result, tree, level)
    pre_order(x, right, depth + 1, result, tree, level)


def post_order(left, right, depth, result, tree, level):
    if depth == TREE_DEPTH:
        return
    if len(tree[level[depth]]) <= 0:
        return
    if not (left < tree[level[depth]][-1][0] < right):
        return

    x, index = tree[level[depth]].pop()
    post_order(left, x, depth + 1, result, tree, level)
    post_order(x, right, depth + 1, result, tree, level)
    result.append(index)