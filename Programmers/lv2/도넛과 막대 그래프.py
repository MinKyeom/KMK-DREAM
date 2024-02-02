# 내 풀이(개선 중)
# 정점을 없애고 그래프 모양을 판별 후 갯수 추가
# 정점을 제외한 부분에서 나머지 점에서 출발 후 모양 판별
from collections import deque


def donut_check(visit, map):
    count = 0
    check = []
    check += visit
    check = deque(visit)
    flag = False
    while check:
        q = deque([check.popleft()])
        start = []  # 출발
        arrive = []  # 도착
        while q:
            i = q.popleft()
            if not i in start:
                start.append(i)
            for j in map[i]:
                if not j in arrive:
                    arrive.append(j)
                    q.append(j)

        if len(set(start) - set(arrive)) == 0:
            count += 1
            if count >= 2:
                break
            continue
        else:
            flag = True
            break

    return 1 if flag == False else 2


def solution(edges):
    result = [0] * 4
    map = {}  # 단방향성 그래프
    g = {}  # 양방향 연결 그래프 체크
    num = []  # 정점모음
    arrive = []
    for a, b in edges:
        if not a in map:
            map[a] = [b]
        else:
            map[a].append(b)
        if not b in map:
            map[b] = []
        if not a in g:
            g[a] = [b]
        else:
            g[a].append(b)
        if not b in g:
            g[b] = [a]
        else:
            g[b].append(a)

        num.append(a)
        num.append(b)
        arrive.append(b)

    num = list(set(num))
    arrive = list(set(num) - set(arrive))

    # 정점 찾기
    for c in arrive:
        if len(map[c]) >= 2:
            stop = c
            result[0] = stop
            break

    del map[stop]  # 정점제거
    del g[stop]

    num = list(set(num) - set([stop]))
    num = deque(num)

    while num:
        t = num.popleft()
        q = deque([t])
        visit = []

        # 연결된 정점 확인
        while q:
            n = q.popleft()
            if not n in visit:
                visit.append(n)
            for i in g[n]:
                if not i in visit and i != stop:
                    q.append(i)

        # 연결된 모양 판별
        # 8자모양 판별
        line = 0
        for j in visit:
            line += len(map[j])

        if line == len(visit) + 1:
            result[3] += 1

        else:
            count = donut_check(visit, map)
            result[count] += 1

        # 체크된 그래프 정점 제거
        num = deque(list(set(num) - set(visit)))

    return result

# 내 풀이 (개선중)
# 정점을 없애고 그래프 모양을 판별 후 갯수 추가
# 정점을 제외한 부분에서 나머지 점에서 출발 후 모양 판별
from collections import deque


def solution(edges):
    result = [0] * 4
    map = {}  # 단방향성 그래프
    g = {}  # 양방향 연결 그래프 체크
    num = []  # 정점모음
    arrive = []

    for a, b in edges:
        if not a in map:
            map[a] = [b]
        else:
            map[a].append(b)
        if not b in map:
            map[b] = []
        if not a in g:
            g[a] = [b]
        else:
            g[a].append(b)
        if not b in g:
            g[b] = [a]
        else:
            g[b].append(a)

        num.append(a)
        num.append(b)
        arrive.append(b)

    num = list(set(num))

    # 정점 특징:도착하는 점에 없음,최소 2개의 그래프를 이어서 두 개의 간선 존재
    stop_check = list(set(num) - set(arrive))

    # 정점 찾기
    for c in stop_check:
        if len(map[c]) >= 2:
            stop = c
            result[0] = stop
            break

    graph_check = []
    graph_check += map[stop]

    del map[stop]  # 정점제거
    del g[stop]

    num = list(set(num) - set([stop]))
    num = deque(num)

    graph_check = deque(graph_check)

    while graph_check:
        t = graph_check.popleft()
        q = deque([t])
        visit = []
        line = 0

        # 연결된 정점 확인
        while q:
            n = q.popleft()
            if not n in visit and n != stop:
                visit.append(n)
                line += len(map[n])
                for i in g[n]:
                    if not i in visit and i != stop:
                        q.append(i)

        # 연결된 모양 판별
        if line == len(visit) + 1:
            result[3] += 1
        elif line == len(visit):
            result[1] += 1
        else:
            result[2] += 1

    return result


# 다른 사람 풀이

def solution(edges):
    input_count = [0 for _ in range(1000001)]
    output_count = [0 for _ in range(1000001)]
    created_node = -1
    doughnut_count = 0
    stick_count = 0
    eight_count = 0
    biggest_node_num = -1

    for a, b in edges:
        biggest_node_num = max(biggest_node_num, a, b)
        output_count[a] += 1
        input_count[b] += 1

    for i in range(1, biggest_node_num + 1):
        if input_count[i] == 0 and output_count[i] >= 2:
            created_node = i
        elif input_count[i] >= 1 and output_count[i] == 0:
            stick_count += 1
        elif input_count[i] >= 2 and output_count[i] == 2:
            eight_count += 1

    doughnut_count = output_count[created_node] - stick_count - eight_count
    return [created_node, doughnut_count, stick_count, eight_count]

