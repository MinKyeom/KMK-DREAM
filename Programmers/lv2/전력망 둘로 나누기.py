# 내 풀이 (개선 중)
# 네트워크 2개로 분활 (나누어진 송전탑 개수 거의 비슷하게!)
# 목표 나누어진 송전탑들의 차이를  return

def solution(n, wires):
    from collections import deque
    result = 100  # 송전탑의 최대갯수로 설정
    wires.sort()
    root_dic = {}
    all_node = []  # 전체 노드 확인

    for v, w in wires:
        if v not in root_dic:
            root_dic[v] = [w]
        else:
            root_dic[v] += [w]
        if w not in root_dic:
            root_dic[w] = [v]
        else:
            root_dic[w] += [v]

        if v not in all_node:
            all_node.append(v)
        elif w not in all_node:
            all_node.append(w)

    print(all_node)
    print(root_dic, "모집단")

    # 선 하나씩 제거 후 나누어진 여부 체크 후 송전탑 개수 체크
    for a in range(len(wires)):
        k = wires.copy()
        new_root = root_dic.copy()
        print(new_root)
        check_1 = k[a][0]
        check_2 = k[a][1]

        del k[a]
        """    
        for b,c in k: #지워야 할 루트 제거
            if c in new_root[b]:
                new_root[b].remove(c)
            if b in new_root[c]:
                new_root[c].remove(b)
        """
        new_root[check_1].remove(check_2)
        new_root[check_2].remove(check_1)

        print(new_root)
        # print(new_root[check_1],"확인")
        # print(new_root[check_2],"확인")

        root_1 = []

        for d in new_root[check_1]:
            root_1 += new_root[d]

        root_2 = []

        for e in new_root[check_2]:
            root_2 += new_root[e]

        print(root_1, "root_1")
        print(root_2, "root_2")

        if len(set(root_1) | set(root_2)) == len(set(all_node)) and len(set(root_1) & set(root_2)) == 0:
            num = abs(len(set(root_1)) - len(set(root_2)))
            if num <= result:
                result = num
                print(result)

    answer = -1
    return answer
## 개선중

def solution(n, wires):
    # 탑의 갯수
    top = [k for k in range(1, n + 1)]

    graph_all = {}  # 양방향
    graph = {}  # 단방향
    result = n + 1  # 송전탑 최대 개수 +1

    # 그래프 모양 체크
    for a, b in wires:
        if not a in graph_all:
            graph_all[a] = [b]
            # graph[a]=[b]
        else:
            graph_all[a] += [b]
            # graph[a]+=[b]

        if not b in graph_all:
            graph_all[b] = [a]
        else:
            graph_all[b] += [a]

    t = wires.copy()

    for c in range(len(t)):
        del_1 = t[c][0]
        del_2 = t[c][1]

        root_1 = []  # 첫번째 새로운 송전탑 그룹

        for d in graph_all[del_1]:
            if d != del_2:
                root_1 += graph_all[d]
                root_1.append(d)

        root_2 = []  # 두번째 새로운 송전탑 그룹

        for e in graph_all[del_2]:
            if e != del_1:
                root_2 += graph_all[e]
                root_2.append(e)

        if len(set(root_1) & set(root_2)) == 0 and set(root_1) | set(root_2) == set(top):
            check = abs(len(set(root_1)) - len(set(root_2)))
            if check <= result:
                result = check

    return result

# 다른 사람 풀이
from collections import deque

def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    cnt = 0
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        #print(v, end=' ')
        cnt += 1
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return cnt


def solution(n, wires):
    answer = n - 2 #  두 전력망이 갖게 되는 송전탑의 개수 차이의 절댓값 중 최댓값 (만약 n이 9일때 최대 절댓값은 두 전력망이 1과 8일때 즉 7이된다.)
    for i in range(len(wires)):
        tmps = wires.copy()
        graph = [[] for i in range(n+1)]
        visited = [False] * (n+1)
        tmps.pop(i) # i번째 전선 제거
        for wire in tmps:
            x, y = wire
            graph[x].append(y)
            graph[y].append(x)
        for idx,g in enumerate(graph):
            if g != []: # n개의 송전탑 중 다른 송전탑과 연결된 송전탑을 시작점으로 지정
                start = idx
                break
        cnts = bfs(graph, start, visited) # bfs를 이용하여 시작점에서 다른 송전탑 탐색함. 이때 탐색 가능한 송전탑 개수를 cnts에 담음(이는 즉 연결된 송전탑의 개수임)
        other_cnts = n - cnts # 전력망을 둘로 나눌 때 첫번째 전력망 개수는 cnts이므로 나머지 전력망 개수는 n - cnts로 구한다.
        if abs(cnts - other_cnts) < answer:
            answer = abs(cnts - other_cnts)
    return answer


# 다른 사람 풀이
import sys

input = sys.stdin.readline
INF = sys.maxsize


def find(x, parent):
    if parent[x] < 0:
        return x

    parent[x] = find(parent[x], parent)
    return parent[x]


def union(a, b, parent):
    root_a = find(a, parent)
    root_b = find(b, parent)

    if root_a == root_b:
        return False

    if parent[root_a] < parent[root_b]:
        # 루트 노드의 parent 값의 절댓값은 트리의 크기를 의미
        parent[root_a] += parent[root_b]
        parent[root_b] = root_a
    elif parent[root_a] > parent[root_b]:
        parent[root_b] += parent[root_a]
        parent[root_a] = root_b
    else:
        parent[root_b] += parent[root_a]
        parent[root_a] = root_b

    return True


def solution(n, wires):
    answer = INF
    for exclude in range(len(wires)):
        parent = [-1] * (n + 1)

        # 간선을 차례대로 제외해보면서, 이외의 간선들로 유니온 파인드
        for a, b in (wires[:exclude] + wires[exclude + 1:]):
            union(a, b, parent)

        # 제외한 간선의 양 끝 점은 서로 독립된 트리의 어느 한 점이므로,
        # 그 두 점의 루트 노드의 parent 값의 차의 절댓값이 두 트리
        # 사이의 노드 개수 차이이다.
        sub_cnt1 = parent[find(wires[exclude][0], parent)]
        sub_cnt2 = parent[find(wires[exclude][1], parent)]
        answer = min(answer, abs(sub_cnt1 - sub_cnt2))

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
