# 생각의 포인트
"""
생각의 전제: 트리 내 전체 등대는 모두 켜져야 한다
자식 노드와 부모 노드와의 관계성에서
부모노드가 켜지면 자식노드는 켜지든 꺼지는 상관없다
부모노드가 꺼지면 자식노드는 무조건 켜져야 부모 노드 또한 밝음 유지

# 전체 등대가 켜져야한다는 생각을 지닌채로 dfs 실행 후 맨 아래 리프 노드부터 맨 위의 루트노드까지의 생각을 이어나가야 풀 수 있다.

코드의 흐름은 전체 내려가면서 모두가 켜지는 상황을 구현 그리고 맨 아래로 리프노드로 내려 갈 시 그 맨 위의 등대가 어떻게해야 최소로 등대를 켤 수 있는지를 고려해야한다

dfs는 맨 아래 리프 노드에 대한 생각을 맨 위로 끌어올리는게 포인트!

최대 깊이 설정에 대한 것도 생각
import sys
sys.setrecursionlimit(10 ** 6)

위의 라이브러리를 사용 안할시 깊이 문제로 오류 발생
"""

# 내 풀이(오답 및 생각 정리 후 재풀이)
# dfs 깊이 설정
from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)

m = defaultdict(list)


def dfs(k, check):
    check[k] = True  # 해당 노드는 on

    light, black = 1, 0  # 해당 노드가 켜질 때 꺼질 때

    for next_node in [n for n in m[k] if check[n] != True]:
        next_node_light, next_node_black = dfs(next_node, check)

        light += min(next_node_light, next_node_black) # 다 켜지는 상황에서의 next 노드의 light,black 생각 밑바탕!
        black += next_node_light

    return light, black


def solution(n, lighthouse):
    l = lighthouse
    check = [False] * (n + 1)  # 등대 번호

    for start, arrive in l:
        m[start].append(arrive)
        m[arrive].append(start)

    light, black = dfs(1, check)

    return min(light, black)


# 이해가 안된 부분 해결 이해 과정:
"""
dfs로 재귀 구현 시 on, off를 구성할 시 사고를 맨 위의 노드를 중심으로 사고하는게 아닌 맨 아래 노드를 중심으로 생각 후 위의 노드로 하나씩 올려 생각해야 재귀 사고 과정에 맞다는 걸 인지하는 것이 중요
"""
# 내 풀이(추가 이해 필요 및 효율성을 위한 체크 라이브러리)
# 등대: n개 뱃길:n-1개
# 목표: 켜 두어야하는 최소한의 등대 개수
# 한 붓 그리기인줄 알았으나 그 부분에서는 벗어나있다
# 애매하게 기억나는 포인트: 딕셔너리 생성시 리스트 생성으로 하는 라이브러리 체크 (시간복잡도 감소)
# dfs로 한 후 중간에 그것보다 적은 등대 개수로 한 경우가 발생하던가 했을 경우 돌아가 백트래킹 생각해보기

# -------------------#

# dp로 접근해보기!:부모 노드가 켜져있을때 자식 노드가 켜진다는 상황을 생각 후 접근


import heapq
from collections import deque
from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)


def dfs(x, r, check):
    check[x] = True

    if not r[x]:
        return 1, 0

    on, off = 1, 0

    for i in [j for j in r[x] if not check[j]]:
        son_on, son_off = dfs(i, r, check)
        on += min(son_on, son_off)
        off += son_on

    return on, off


def solution(n, lighthouse):
    #    m={}
    r = defaultdict(list)

    l = lighthouse  # 축약

    # 딕션너리 활용해 그래프 형태로 만들기

    # 기존 내 풀이 풀이방향
    """
    for i,j in l:

        if not i in m:
            m[i]=[j]
        else:
            heapq.heappush(m[i],j)
        if not j in m:
            m[j]=[i]
        else:
            heapq.heappush(m[j],i)
    """
    # 새로운 효율성 접근 개선
    for i, j in l:
        r[i].append(j)
        r[j].append(i)

    check = [False] * (n + 1)

    on, off = dfs(1, r, check)

    return min(on, off)

# 내 풀이(개선 중)
# 등대: n개 뱃길:n-1개
# 목표: 켜 두어야하는 최소한의 등대 개수
# 한 붓 그리기인줄 알았으나 그 부분에서는 벗어나있다
# 애매하게 기억나는 포인트: 딕셔너리 생성시 리스트 생성으로 하는 라이브러리 체크 (시간복잡도 감소)
# dfs로 한 후 중간에 그것보다 적은 등대 개수로 한 경우가 발생하던가 했을 경우 돌아가 백트래킹 생각해보기

# -------------------#

# dp로 접근해보기!:부모 노드가 켜져있을때 자식 노드가 켜진다는 상황을 생각 후 접근

import heapq
from collections import deque


def solution(n, lighthouse):
    m = {}

    l = lighthouse  # 축약

    # 딕션너리 활용해 그래프 형태로 만들기

    for i, j in l:

        if not i in m:
            m[i] = [j]
        else:
            heapq.heappush(m[i], j)
        if not j in m:
            m[j] = [i]
        else:
            heapq.heappush(m[j], i)

    dp = [["off", "dark"] for _ in range(n)]

    return 0


# 내 풀이(개선 중)
# bfs,dfs 동시 활용 방안 고려: 시간 초과 및 순서에 따른 리스트 변경 관련 의문 사항 해결 필요
# 등대: n개 뱃길:n-1개
# 목표: 켜 두어야하는 최소한의 등대 개수
# 한 붓 그리기인줄 알았으나 그 부분에서는 벗어나있다
# 애매하게 기억나는 포인트: 딕셔너리 생성시 리스트 생성으로 하는 라이브러리 체크 (시간복잡도 감소)
# dfs로 한 후 중간에 그것보다 적은 등대 개수로 한 경우가 발생하던가 했을 경우 돌아가 백트래킹 생각해보기

import heapq
from collections import deque


def solution(n, lighthouse):
    m = {}

    l = lighthouse  # 축약

    island = [i + 1 for i in range(n)]

    # 딕션너리 활용해 그래프 형태로 만들기

    for i, j in l:

        if not i in m:
            m[i] = [j]
        else:
            heapq.heappush(m[i], j)
        if not j in m:
            m[j] = [i]
        else:
            heapq.heappush(m[j], i)

    # print(m, "first")

    # 키값내 values내부 정렬 정렬
    for v in m:
        m[v].sort(key=lambda x: -len(m[x]))

    # print(m,"second")

    # 키값을 values 길이에 따라 정렬
    new_m = sorted(m.items(), key=lambda x: -len(x[1]))

    # print(new_m,"third")

    start_len = 0

    result = []

    for start, arrive in new_m:
        q = deque([start])
        check = []
        visit = []
        count = 0

        while q:
            s = q.popleft()

            if len(set(m[s]) - set(check)) > 0:
                if not s in check:
                    visit.append(s)
                    check.append(s)

                check += m[s]
                q = list(q)
                q = deque(m[s])

            if len(set(island) - set(check)) == 0:
                result.append(visit)
                visit = [start]
                break

            count += 1

    print(result)

    return 0

# 내 풀이(개선 중)
# 등대: n개 뱃길:n-1개
# 목표: 켜 두어야하는 최소한의 등대 개수
# 한 붓 그리기인줄 알았으나 그 부분에서는 벗어나있다
# 애매하게 기억나는 포인트: 딕셔너리 생성시 리스트 생성으로 하는 라이브러리 체크 (시간복잡도 감소)

import heapq


def solution(n, lighthouse):
    m = {}

    l = lighthouse  # 축약

    count = 0

    for i, j in l:

        if not i in m:
            m[i] = [j]
        else:
            heapq.heappush(m[i], j)
        if not j in m:
            m[j] = [i]
        else:
            heapq.heappush(m[j], i)

    check = []

    for v in m:
        m[v].sort(key=lambda x: -len(m[x]))

    print(m)

    new_m = sorted(m.items(), key=lambda x: -len(x[1]))

    print(new_m)

    return 0

# 다른 사람 풀이
import sys
from collections import defaultdict

sys.setrecursionlimit(1000001)

A = defaultdict(list)
vis = [False] * 1000001


# 자신을 포함한 subtree에서, 내가 켜졌을 때의 최소 점등 등대 개수와
# 내가 꺼졌을 때의 최소 점등 등대 개수를 반환합니다.
def dfs(u):
    vis[u] = True
    if not A[u]:
        # u가 leaf라면 내가 켜졌을 떄의 최소 점등 등대 개수는 1
        # 내가 꺼졌을 때의 최소 점등 등대 개수는 0
        return 1, 0

    # u가 leaf가 아니라면
    on, off = 1, 0
    for v in [v for v in A[u] if not vis[v]]:
        # 내가 켜졌다면 child들은 켜지든 꺼지든 상관 없습니다. -> 킨 것과 끈 것중 최소값을 취함
        # 내가 꺼졌다면 child들은 무조건 켜져야 합니다.
        # 이 점을 생각해서 leaf들의 정보를 취합, 정리합니다.
        child_on, child_off = dfs(v)
        on += min(child_on, child_off)
        off += child_on
    return on, off


def solution(n, lighthouse):
    for u, v in lighthouse:
        A[u].append(v)
        A[v].append(u)

    on, off = dfs(1)
    return min(on, off)

# 다른 사람 풀이(bfs활용)
from collections import defaultdict, deque


def solution(n, lighthouse):
    graph = defaultdict(list)
    onoff = [0 for _ in range(n + 1)]

    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)

    q = deque()
    # 리프 노드 담기
    for i in range(1, n + 1):
        if len(graph[i]) == 1:
            q.append(i)

    # 리프 노드부터 루트까지 올라가기, 등대 켜지면 다음 노드와 연결 끊기
    while q:
        now_leaf = q.popleft()
        if graph[now_leaf] == []:
            break
        parent = graph[now_leaf][0]

        # 리프 노드 그래프에서 삭제
        del graph[now_leaf]
        # 부모 노드에서 리프 노드 연결 해제
        graph[parent].remove(now_leaf)
        # 부모 노드가 리프 노드가 되면 큐에 넣기
        if len(graph[parent]) == 1:
            q.append(parent)

        if onoff[now_leaf] == 1:
            continue
        onoff[parent] = 1

    return sum(onoff)