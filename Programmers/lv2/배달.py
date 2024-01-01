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

# 내 풀이(개선 중)
# dfs start
# d={} # 연결된 마을
# d_time={} # 연결된 마을마다 걸리는 시간
# dfs start

def another(i, d_time, d, visit, count, check):
    for a in d[i]:
        if 1 in d[a]:
            for t in d_time[str(a) + "-" + str(1)]:
                check.append(count + t)

        elif a in visit:
            continue

        else:
            visit.append(a)
            for k in d_time[str(a) + "-" + str(i)]:
                new_count = count + k
                another(a, d_time, d, visit, new_count, check)

    return check


def solution(N, road, K):
    # 1번 마을에서 배달 가능한 마을의 개수
    # dfs
    # 도달 가능한지 여부

    result = 0  # 마을의 개수
    d = {}  # 연결된 마을
    d_time = {}  # 연결된 마을마다 걸리는 시간
    del_list = [k for k in range(2, N + 1)]  # 배달 받을 마을
    visit = []

    for a, b, c in road:
        if not a in d:
            d[a] = [b]
        else:
            d[a].append(b)

        if not b in d:
            d[b] = [a]
        else:
            d[b].append(a)
        if not str(a) + "-" + str(b) in d_time:
            d_time[str(a) + "-" + str(b)] = [c]
        else:
            d_time[str(a) + "-" + str(b)].append(c)
        if not str(b) + "-" + str(a) in d_time:
            d_time[str(b) + "-" + str(a)] = [c]
        else:
            d_time[str(a) + "-" + str(b)].append(c)

    # print(d,d_time)

    for i in del_list:
        count = 0  # 거리
        visit = []
        if i in d[1]:
            for t in d_time[str(a) + "-" + str(b)]:
                if t <= K:
                    result += 1
                else:
                    continue
        else:
            check = []
            visit.append(i)
            check = another(i, d_time, d, visit, count, check)
            if len(check) == 0:
                continue
            else:
                count = min(check)

            if count <= K:
                result += 1
            else:
                continue

    return result

# 다른 사람 풀이
