"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/42892
"""
# 내 풀이_ 개선 중
from collections import defaultdict, deque
import copy


def root_parent(root_num, graph, xy_to_point):
    for p, son in graph.items():
        if root_num in son:
            return xy_to_point[p]


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
    xy_to_point = defaultdict(tuple)

    start = set()

    for num, node in enumerate(nodeinfo):
        point_number
        x, y = node[0], node[1]
        point_number[(x, y)] = num + 1
        xy_to_point[num + 1] = (x, y)

        # (x,y) and 해당 좌표 번호
        level[y].append(x)
        start.add(y)

    for s in start:
        level[s].sort()

    # 위상에 따라 구분
    start = list(start)
    start.sort(reverse=True)

    start = deque(start)
    visit = set()

    # 진행도
    progress = 0
    finish = len(start)

    # 탑 노드
    now = start.popleft()

    while start:
        k = start.popleft()
        new = deque(copy.deepcopy(level[k]))

        while new:
            x = new.popleft()
            node_num = point_number[(x, k)]
            for c in range(len(level[now])):
                p_x = level[now][c]
                num = point_number[(p_x, now)]
                if x < p_x:
                    graph[num].append(node_num)
                    break

                elif x > p_x:
                    if len(level[now]) > c + 1:
                        if level[now][c + 1] < x:
                            continue
                        elif level[now][c + 1] < x and len(graph[num]) < 2:
                            graph[num].append(node_num)

                        break
                    # 맨 오른쪽
                    else:
                        graph[num].append(node_num)
                        break
                break

        print(graph)

        # 위상 변경
        now = k
        # break

    return 0
# 내 풀이_ 개선 중
from collections import defaultdict, deque


def solution(nodeinfo):
    point_number = defaultdict(int)
    level = set()

    for n, node in enumerate(nodeinfo):
        x, y = node[0], node[1]
        level.add(y)
        point_number[(x, y)] = n + 1

    # 크기 재배열
    node_x = sorted(nodeinfo, key=lambda x: x[0])
    node_y = sorted(node_x, key=lambda x: -x[1])

    # 그래프 구성
    graph = defaultdict(list)

    # 위상 구분
    level = list(level)
    level.sort(reverse=True)
    level = deque(level)

    level.popleft()

    # 노드 구분
    node = deque(node_y)
    count = 0

    while node:
        # 현재 위상
        point = level.popleft()
        x, y = node.popleft()
        number = point_number[((x, y))]

        for i, j in node:
            if j < point:
                break
            else:

    answer = [[]]
    return answer
# 내 풀이_ 개선 중
"""
전위순회:dfs
후위순회:자식 노드 없을 경우에 추가
"""
from collections import defaultdict, deque
import heapq


def root_parent(root_num, graph, xy_to_point):
    for p, son in graph.items():
        if root_num in son:
            return xy_to_point[p]


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
    xy_to_point = defaultdict(tuple)

    start = set()

    for num, node in enumerate(nodeinfo):
        point_number
        x, y = node[0], node[1]
        point_number[(x, y)] = num + 1
        xy_to_point[num + 1] = (x, y)

        # (x,y) and 해당 좌표 번호
        level[y].append(x)
        start.add(y)

    for s in start:
        level[s].sort()

    # 위상에 따라 구분
    start = list(start)
    start.sort(reverse=True)

    start = deque(start)
    visit = set()

    # 진행도
    progress = 0
    finish = len(start)

    while start:
        k = start.popleft()
        m = level[k]

        if len(visit) == 0:
            # 현재 위상
            now_level = k
            # 해당 좌표 번호
            root_num = point_number[(m[0], k)]
            visit.add(k)
            progress += 1
            continue

        for i in m:
            j, num = k, point_number[(i, k)]

            if progress == 1:
                graph[root_num].append(num)

            else:
                for node in level[root_now]:
                    root_x, root_y, root_num = node, root_now, point_number[(node, root_now)]

                    # 맨 왼쪽
                    if node == 0 and i < root_x:
                        graph[root_num].append(num)
                        break

                    # 맨 오른쪽
                    elif node == len(level[root_now]) - 1 and i > root_x:
                        graph[root_num].append(num)
                        break

                    else:
                        check = root_parent(root_num, graph, xy_to_point)
                        root_parent_x, root_parent_y = check[0], check[1]

                        # root_parent_x,root_parent_y=root_parent(root_num,graph,xy_to_point)
                        # print(root_parent_x,root_parent_y,"check")

                        # left에 배치될 경우 확인
                        if i < root_x and i > root_parent_x:
                            graph[root_num].append(num)
                            break
                        elif i < root_x and i < root_parent_x:
                            graph[root_num].append(num)
                            break

                        # right
                        elif i > root_x and i < root_parent_x:
                            graph[root_num].append(num)

                    elif i > root_x and i < root_parent_x:
                    continue
                    else:
                    print(i, root_x, root_parent_x)
                    return 10000
                    continue


# 현재 위상 변경
root_now = k

progress += 1

if progress == finish:
    break

print(graph, "last")

return 0

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


# 다른 사람 풀이
import sys
sys.setrecursionlimit(10 ** 7)

L, R = 1, 2

def insert(tree, node, parent_idx):
    idx, x, y = node
    (p_x, p_y), left, right = tree[parent_idx]
    if p_x < x:
        if right != 0:
            insert(tree, node, right)
        else:
            tree[parent_idx][R] = idx
            tree[idx] = [(x, y), 0, 0]
    else:
        if left != 0:
            insert(tree, node, left)
        else:
            tree[parent_idx][L] = idx
            tree[idx] = [(x, y), 0, 0]


def pre_order(tree, node_idx):
    path = []
    if node_idx == 0:
        return path
    path.append(node_idx)
    path += pre_order(tree, tree[node_idx][L])
    path += pre_order(tree, tree[node_idx][R])
    return path


def post_order(tree, node_idx):
    path = []
    if node_idx == 0:
        return path
    path += post_order(tree, tree[node_idx][L])
    path += post_order(tree, tree[node_idx][R])
    path.append(node_idx)
    return path


def solution(nodeinfo):
    sorted_node_info = [] # 원소 : [idx, x, y]
    for idx, [x, y] in enumerate(nodeinfo, 1):
        sorted_node_info.append([idx, x, y])
    sorted_node_info.sort(key=lambda x: x[2])

    tree = dict() # [(x, y), left_idx, right_idx]
    root_idx, root_x, root_y = sorted_node_info.pop()
    tree[root_idx] = [(root_x, root_y), 0, 0]

    while sorted_node_info:
        node = sorted_node_info.pop()
        insert(tree, node, root_idx)

    answer = [pre_order(tree, root_idx), post_order(tree, root_idx)]
    return answer
