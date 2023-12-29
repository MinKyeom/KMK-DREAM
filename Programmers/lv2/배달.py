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
def another(i, d_time, d, count, visit, K, new):
    flag = False

    for a in d[i]:
        if not [a, i] in visit:
            if 1 in d[a]:
                count += d_time[a, i]
                count += d_time[a, 1]
                new.append(count)
            else:
                count += d_time[a, i]
                visit.append([a, i])
                if count > K:
                    flag = True
                    break

                else:
                    count, flag = another(a, d_time, d, count, visit, K, new)

        else:
            continue

    # print(new,"new")
    c = min(new)
    return flag, c


def solution(N, road, K):
    # 1번 마을에서 배달 가능한 마을의 개수
    # dfs
    # 도달 가능한지 여부

    result = 0  # 마을의 개수
    d = {}  # 연결된 마을
    d_time = {}
    del_list = [k for k in range(2, N + 1)]  # 배달 받을 마을
    visit = []

    for a, b, c in road:
        if not a in d:
            d[a] = [b]
            d_time[a, b] = c
        else:
            d[a].append(b)
            d_time[a, b] = c
        if not b in d:
            d[b] = [a]
            d_time[b, a] = c
        else:
            d[b].append(a)
            d_time[b, a] = c

    for i in del_list:
        count = 0  # 거리
        visit = []
        if i in d[1]:
            count += d_time[i, 1]
            if count <= K:
                result += 1
            else:
                continue

        else:
            new = []
            flag, c = another(i, d_time, d, count, visit, K, new)
            # print(flag,"flag",count,visit)
            if c <= K and flag == False:
                print("check")
                result += 1

    return result

# 다른 사람 풀이
