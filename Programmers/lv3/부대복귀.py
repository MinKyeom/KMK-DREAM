# lv3 부대 복귀
# 내 풀이
# 조건
# 각 부대 지역 고유번호 지정
# 임무 완료 후 최단 시간으로 부대 복귀
# 적군의 방해로 지역이 막혀 부대 복귀 불가능한 대원 발생 가능

# 접근 사고 방향
# 최단 거리를 구하는 조건이라 다익스트라 알고리즘 떠올려야 하나 익숙하지 않아 dfs로 1차 접근
# dfs 방문 여부로 인한 최단거리 구성의 어려움으로 인한 bfs로 선회 후 재구성:
# >1차: 시간초과 발생

# 2차 생각 전환
# 방향전환: 꼭 출발점에서 목적지를 찾아가야하나? 목적지에서 시작점까지를 돌면 source마다 할 필요 없이 반복 필요 없음
# 도착점에서 갈 수 없는 곳 모두 -1로 생각!
# 목표:최단 시간을 담은 값을 리턴


# 총 지역수: n , 길 정보 roads , 부대원 위치: sources 강철부대 지역:destination

from collections import deque
from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)  # 최대 깊이 설정

m = defaultdict(list)


def solution(n, roads, sources, destination):
    check = [-1 for _ in range(n + 1)]  # 각 부대별 최단 거리 정리 # 도착점으로부터 시작으로 사고 전환! 도착 못하면 -1
    result = []

    r = roads
    s = sources
    d = destination

    # 위치별 정리
    for i, j in r:
        m[i].append(j)
        m[j].append(i)

    v = [False for _ in range(n + 1)]  # 방문 여부

    q = deque([[d, 0]])

    new = []  # 거리에 따라 추가할 부분

    while q:
        x, t = q.popleft()

        v[x] = True  # 방문

        check[x] = t

        new += m[x]

        if len(q) == 0:
            new = list(set(new))  # 중복 제거

            if len(new) == 0:
                break

            for u in [y for y in new if v[y] == False]:
                q.append([u, t + 1])

            if len(q) == 0:
                break

            new = []  # 그 다음 순서를 담기 위해서 초기화!!

    for z in s:
        result.append(check[z])

    """
    for k in s:
        v=[False for _ in range(n+1)]
        q=deque([[k,0]])

        # dfs로 접근 후 구현시 방문 여부 체크로 인해 bfs로 선회 후 다시 구성 
        new=[]

        if check[k]!=False:
            result.append(check[k])
            continue

        while q:
            w,t=q.popleft()

            v[w]=True

            if w==d:
                result.append(t)
                check[k]=t
                break

            else:
                # for u in [x for x in m[k] if v[x]==False]:
                #     new.append([u,t+1])

                new+=m[w]

            if len(q)==0:
                new=list(set(new)) # 중복 제거

                if len(new)==0:
                    result.append(-1)
                    check[k]=-1
                    break 

                for u in [x for x in new if v[x]==False]: # 1차로 선회 후 체크해야 방문 한 곳 다시 확인 제거
                    q.append([u,t+1])

                if len(q)==0: # 전부 방문하여 더 이상 갈 곳이 없을 경우도 존재!
                    result.append(-1)
                    check[k]=-1
                    break

                new=[]

    """

    return result


# 내 풀이(개선 중)
# 조건
# 각 부대 지역 고유번호 지정
# 임무 완료 후 최단 시간으로 부대 복귀
# 적군의 방해로 지역이 막혀 부대 복귀 불가능한 대원 발생 가능

# 접근 사고 방향
# 최단 거리를 구하는 조건이라 다익스트라 알고리즘 떠올려야 하나 익숙하지 않아 dfs로 1차 접근
# dfs 방문 여부로 인한 최단거리 구성의 어려움으로 인한 bfs로 선회 후 재구성:
# >1차: 시간초과 발생

# 2차 생각 전환
# 방향전환: 꼭 출발점에서 목적지를 찾아가야하나? 목적지에서 시작점까지를 돌면 source마다 할 필요 없이 반복 필요 없음
# 도착점에서 갈 수 없는 곳 모두 -1로 생각!
# 목표:최단 시간을 담은 값을 리턴


# 총 지역수: n , 길 정보 roads , 부대원 위치: sources 강철부대 지역:destination

from collections import deque
from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)  # 최대 깊이 설정

m = defaultdict(list)


def solution(n, roads, sources, destination):
    check = [False for _ in range(n + 1)]  # 각 부대별 최단 거리 정리 # source가 중복된 경우 바로 스킵하기 위해
    result = []

    r = roads
    s = sources
    d = destination

    for i, j in r:
        m[i].append(j)
        m[j].append(i)

    for k in s:
        v = [False for _ in range(n + 1)]
        q = deque([[k, 0]])

        # dfs로 접근 후 구현시 방문 여부 체크로 인해 bfs로 선회 후 다시 구성
        new = []

        if check[k] != False:
            result.append(check[k])
            continue

        while q:
            w, t = q.popleft()

            v[w] = True

            if w == d:
                result.append(t)
                check[k] = t
                break

            else:
                # for u in [x for x in m[k] if v[x]==False]:
                #     new.append([u,t+1])

                new += m[w]

            if len(q) == 0:
                new = list(set(new))  # 중복 제거

                if len(new) == 0:
                    result.append(-1)
                    check[k] = -1
                    break

                for u in [x for x in new if v[x] == False]:  # 1차로 선회 후 체크해야 방문 한 곳 다시 확인 제거
                    q.append([u, t + 1])

                if len(q) == 0:  # 전부 방문하여 더 이상 갈 곳이 없을 경우도 존재!
                    result.append(-1)
                    check[k] = -1
                    break

                new = []

    return result


# 내 풀이(개선 중)
# 조건
# 각 부대 지역 고유번호 지정
# 임무 완료 후 최단 시간으로 부대 복귀
# 적군의 방해로 지역이 막혀 부대 복귀 불가능한 대원 발생 가능

# 접근 사고 방향
# 최단 거리를 구하는 조건이라 다익스트라 알고리즘 떠올려야 하나 익숙하지 않아 dfs로 1차 접근
# dfs 방문 여부로 인한 최단거리 구성의 어려움으로 인한 bfs로 선회 후 재구성:
# >1차: 시간초과 발생

# 목표:최단 시간을 담은 값을 리턴

# 총 지역수: n , 길 정보 roads , 부대원 위치: sources 강철부대 지역:destination

from collections import deque
from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)  # 최대 깊이 설정

m = defaultdict(list)


def solution(n, roads, sources, destination):
    result = []

    r = roads
    s = sources
    d = destination

    for i, j in r:
        m[i].append(j)
        m[j].append(i)

    for k in s:
        v = [False for _ in range(n + 1)]
        q = deque([[k, 0]])

        # dfs로 접근 후 구현시 방문 여부 체크로 인해 bfs로 선회 후 다시 구성
        new = []
        while q:
            k, t = q.popleft()
            v[k] = True
            if k == d:
                result.append(t)
                break

            else:
                for u in [x for x in m[k] if v[x] == False]:
                    new.append([u, t + 1])

            if len(q) == 0:
                q += new
                if len(new) == 0:
                    result.append(-1)
                    break

                new = []

    return result

# 다른 사람 풀이 모음
from collections import deque

def solution(n, roads, sources, destination):
    paths = [[] for _ in range(n+1)]
    for s,t in roads:
        paths[s].append(t)
        paths[t].append(s)
    dist = [-1 for _ in range(n+1)]
    dist[destination] = 0
    s = deque([destination])
    while s:
        v = s.popleft()
        d = dist[v]
        for u in paths[v]:
            if dist[u] == -1:
                dist[u] = d+1
                s.append(u)

    return [dist[i] for i in sources]


def solution(n, roads, sources, destination):
    maps = [[] for _ in range(n+1)]
    for p1, p2 in roads:
        maps[p1].append(p2)
        maps[p2].append(p1)

    times = [-1] * (n+1)
    queue = [(destination, 0)]
    times[destination] = 0
    while queue:
        q = queue.pop(0)
        for j in maps[q[0]]:
            if times[j] == -1:
                queue.append((j, q[1]+1))
                times[j] = q[1]+1

    return [times[i] for i in sources]


