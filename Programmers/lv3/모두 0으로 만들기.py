"""
출처: 프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/76503
"""
# 풀이 과정
"""

생각방향:
리프노드를 모두 0으로 만든 후의 생각 접근 
핵심 접근 생각 방향 시작:한 곳으로 모으기 생각
#각 점이 간선의 개수가 많은 곳으로 옮기기
#각 점이 간선의 개수가 같다면 가중치가 많은 쪽으로 이동 
#위의 두 개 조차 같다면 번호가 작은쪽으로 

# 모든 점들이 서로 연결되지 않은 경우 생각해서 체크 필요 
# 한 곳으로 모으기 vs 여러 곳으로 나눠모으기 

목표:모든 점들의 가중치를 0으로 만들기 

"""
from collections import defaultdict
from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

# 간선 연결 확인
m = defaultdict(list)
result = 0


def dfs(c, p, a):
    global m, result

    for up in m[c]:
        if up != p:
            dfs(up, c, a)

    a[p] += a[c]
    result += abs(a[c])

    return result


def solution(a, edges):
    global m, result

    for i, j in edges:
        m[i].append(j)
        m[j].append(i)

    # a: 각 점의 가중치를 의미 edges: 간선
    n = len(a)

    if sum(a) != 0:
        return -1

    dfs(0, 0, a)

    return result


# 내 풀이(개선 중)
"""

생각방향:
리프노드를 모두 0으로 만든 후의 생각 접근 
핵심 접근 생각 방향 시작:한 곳으로 모으기 생각
#각 점이 간선의 개수가 많은 곳으로 옮기기
#각 점이 간선의 개수가 같다면 가중치가 많은 쪽으로 이동 
#위의 두 개 조차 같다면 번호가 작은쪽으로 

# 모든 점들이 서로 연결되지 않은 경우 생각해서 체크 필요 
# 한 곳으로 모으기 vs 여러 곳으로 나눠모으기 

목표:모든 점들의 가중치를 0으로 만들기 

"""
from collections import defaultdict
from collections import deque
import copy

# 간선 연결 확인
m = defaultdict(list)


def bfs(n):
    global m

    v = [False] * n
    q = [0]

    while q:
        k = q.pop()

        if v[k] == False:
            v[k] = True
            q += m[k]

    if v.count(True) == n:
        return 1

    else:
        return -1


def solution(a, edges):
    for i, j in edges:
        m[i].append(j)
        m[j].append(i)

    # a: 각 점의 가중치를 의미 edges: 간선
    n = len(a)
    line = bfs(n)

    if line == -1:
        return -1

    if sum(a) != 0:
        return -1

    else:
        result = 0
        check = copy.deepcopy(edges)

        while check:
            v, w = check.pop()

            # a에서 b로 가중치 옮기기
            if len(m[v]) <= len(m[w]):
                if a[v] >= 0:
                    a[w] -= a[v]
                    result += abs(a[v])
                    a[v] = 0

                else:
                    a[w] += a[v]
                    result += abs(a[v])
                    a[v] = 0
            else:
                if a[w] >= 0:
                    a[v] -= a[w]
                    result += abs(a[w])
                    a[w] = 0

                else:
                    a[v] += a[w]
                    result += abs(a[w])
                    a[w] = 0

            # if a[v]!=0 or a[w]!=0:
            #     check.append([v,w])

        return result


# 내 풀이(개선 중)
"""

생각방향:
리프노드를 모두 0으로 만든 후의 생각 접근 
핵심 접근 생각 방향 시작:한 곳으로 모으기 생각
#각 점이 간선의 개수가 많은 곳으로 옮기기
#각 점이 간선의 개수가 같다면 가중치가 많은 쪽으로 이동 
#위의 두 개 조차 같다면 번호가 작은쪽으로 

# 모든 점들이 서로 연결되지 않은 경우 생각해서 체크 필요 
# 한 곳으로 모으기 vs 여러 곳으로 나눠모으기 

목표:모든 점들의 가중치를 0으로 만들기 

"""
from collections import defaultdict
from collections import deque
import copy


def solution(a, edges):
    # a: 각 점의 가중치를 의미 edges: 간선

    if sum(a) != 0:
        return -1


    else:
        m = defaultdict(list)

        for i, j in edges:
            m[i].append(j)
            m[j].append(i)

        result = 0

        check = copy.deepcopy(edges)

        while check:
            v, w = check.pop()

            # a에서 b로 가중치 옮기기
            if len(m[v]) <= len(m[w]):
                if a[v] >= 0:
                    a[w] -= a[v]
                    result += abs(a[v])
                    a[v] = 0

                else:
                    a[w] += a[v]
                    result += abs(a[v])
                    a[v] = 0
            else:
                if a[w] >= 0:
                    a[v] -= a[w]
                    result += abs(a[w])
                    a[w] = 0

                else:
                    a[v] += a[w]
                    result += abs(a[w])
                    a[w] = 0

            if a[v] != 0 or a[w] != 0:
                check.append([v, w])

        return result


# 내 풀이(개선 중)
"""

생각방향:
리프노드를 모두 0으로 만든 후의 생각 접근 
핵심 접근 생각 방향 시작:한 곳으로 모으기 생각
#각 점이 간선의 개수가 많은 곳으로 옮기기
#각 점이 간선의 개수가 같다면 가중치가 많은 쪽으로 이동 
#위의 두 개 조차 같다면 번호가 작은쪽으로 

목표:모든 점들의 가중치를 0으로 만들기 

"""
from collections import defaultdict
from collections import deque
import copy


def solution(a, edges):
    # a: 각 점의 가중치를 의미 edges: 간선

    if sum(a) != 0:
        return -1


    else:
        m = defaultdict(list)

        for i, j in edges:
            m[i].append(j)
            m[j].append(i)

        result = 0

        check = copy.deepcopy(edges)

        while check:
            v, w = check.pop()

            # a에서 b로 가중치 옮기기
            if len(m[v]) <= len(m[w]):
                if a[v] >= 0:
                    a[w] -= a[v]
                    result += abs(a[v])
                    a[v] = 0

                else:
                    a[w] += a[v]
                    result += abs(a[v])
                    a[v] = 0
            else:
                if a[w] >= 0:
                    a[v] -= a[w]
                    result += abs(a[w])
                    a[w] = 0

                else:
                    a[v] += a[w]
                    result += abs(a[w])
                    a[w] = 0

            if a[v] != 0 or a[w] != 0:
                check.append([v, w])

        return result

# 다른 사람 풀이
from collections import deque

def solution(a, edges):
    answer = 0
    n = len(a)
    graph = [[] for _ in range(n)]

    # 간성정보 입력
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    # 루트 노드부터 리프 노드까지 이동경로
    route = []

    visit = [0]*n
    visit[0] = 1
    Q = deque([0])
    # route 찾기
    while Q:
        now = Q.popleft()
        route.append(now)

        for j in graph[now]:
            if visit[j] == 0:
                visit[j] = 1
                Q.append(j)

    # 리프노드를 0으로 만들고 부모노드에 더해감
    # 최종적으로 부모노드에 도착
    visit = [0]*n
    for i in range(n-1, -1, -1):
        node = route[i]
        visit[node] = 1

        # 현재 노드가 0이 아니라면 탐색, 0이면 넘어감
        if a[node]:

            for v in graph[node]:
                if visit[v] == 0 and a[node]:
                    a[v] += a[node]
                    answer += abs(a[node])
                    a[node] = 0

    return answer if a[0] == 0 else -1


import sys

sys.setrecursionlimit(10 ** 6)

result = 0


def solution(a, edges):
    if sum(a) != 0:
        return -1

    n = len(a)
    graph = [[] for i in range(n)]
    for node_a, node_b in edges:
        graph[node_a].append(node_b)
        graph[node_b].append(node_a)

    def dfs(child, parent, graph, a):
        global result
        for c in graph[child]:
            if c != parent:
                dfs(c, child, graph, a)
        a[parent] += a[child]
        result += abs(a[child])

    dfs(0, 0, graph, a)
    return result

