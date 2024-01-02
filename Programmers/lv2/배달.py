# 다익스트라 알고리즘
import heapq  # 우선순위 큐 구현을 위함


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
    distances[start] = 0  # 시작 값은 0이어야 함
    queue = []
    heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

        if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
            if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입

    return distances
# 참고 dfs(리스트를 활용한 dfs 구현)
def dfs(graph, start_node):
    ## 기본은 항상 두개의 리스트를 별도로 관리해주는 것
    need_visited, visited = list(), list()

    ## 시작 노드를 시정하기
    need_visited.append(start_node)

    ## 만약 아직도 방문이 필요한 노드가 있다면,
    while need_visited:

        ## 그 중에서 가장 마지막 데이터를 추출 (스택 구조의 활용)
        node = need_visited.pop()

        ## 만약 그 노드가 방문한 목록에 없다면
        if node not in visited:
            ## 방문한 목록에 추가하기
            visited.append(node)

            ## 그 노드에 연결된 노드를
            need_visited.extend(graph[node])

    return visited

# que를 활용한 dfs 구현
def dfs2(graph, start_node):
    ## deque 패키지 불러오기
    from collections import deque
    visited = []
    need_visited = deque()

    ##시작 노드 설정해주기
    need_visited.append(start_node)

    ## 방문이 필요한 리스트가 아직 존재한다면
    while need_visited:
        ## 시작 노드를 지정하고
        node = need_visited.pop()

        ##만약 방문한 리스트에 없다면
        if node not in visited:
            ## 방문 리스트에 노드를 추가
            visited.append(node)
            ## 인접 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])

    return visited

# 내 풀이
# import heapq

def dijkstra(check, r):
    heap = []

    heap.append([0, 1])  ###

    # heapq.heappush(heap,[0,1])

    while heap:
        # cost,node=heapq.heappop(heap)
        cost, node = heap.pop()
        for c, n in r[node]:
            if cost + c < check[n]:
                check[n] = cost + c
                heap.append([cost + c, n])
                # heapq.heappush(heap,[cost+c,n])


def solution(N, road, K):
    check = [float("inf")] * (N + 1)

    check[1] = 0
    # print(check)

    r = [[] for _ in range(N + 1)]

    for k in road:
        r[k[0]].append([k[2], k[1]])
        r[k[1]].append([k[2], k[0]])
    print(r)
    dijkstra(check, r)

    return len([i for i in check if i <= K])

# 다른 사람 풀이
import sys
def solution(N, road, K):
    visited, D, r = [False]*(N+1), [sys.maxsize]*(N+1), [[(None, None)]] + [[] for _ in range(N)]
    for e in road:
        r[e[0]].append((e[1],e[2]))
        r[e[1]].append((e[0],e[2]))
    D[1] = 0
    for _ in range(1,N+1):
        min_ = sys.maxsize
        for i in range(1,N+1):
            if not visited[i] and D[i] < min_:
                min_ = D[i]
                m = i
        visited[m] = True
        for w, wt in r[m]:
            if D[m] + wt < D[w]:
                D[w] = D[m] + wt

    return len([d for d in D if d <= K])
