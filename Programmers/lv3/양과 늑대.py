"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/92343
"""
# 풀이 과정
"""
양 모으기
# 조건
각 노드 방문시 양과 늑대가 따라옴 
늑대가 양보다 같거나 많을 경우 양이 다 잡아먹힘 

최대한 많은 양을 모아서 루트 노드로 돌아오기 
그래프 형태로 볼 때 dfs 생각 방향 


# info: i번 노드의 양 또는 늑대 여부
# edges: 연결된 두 노드를 나타냄

#생각방향

자식 노드를 거치려면 부모노드의 동물을 거쳐야한다
단순 생각 방향: 완탐 후 최대 양을 표현하면 된다
info를 숫자로 표현 후 순열로 한 후 모든 경우의 수를 표현가능
양을 최대로 모은 후 늑대가 있는 곳으로 가야한다 
모든 노드들의 양이 최대 늑대 최소 값들을 구해야한다
dfs로 풀었던 등대 문제 생각
# dfs 사용 시 원복 개념 등산로 찾기에서 쓰인 개념 일부분 아이디어 사용!!
"""

v = []
result = []


def dfs(sheep, wolf, info, edges):
    global v, result

    if sheep > wolf:
        result.append(sheep)

    else:
        return

    for i, j in edges:

        # 부모노드 방문 여부 확인
        if v[i] == 1 and v[j] == 0:
            v[j] = 1

            # 늑대인 경우
            if info[j] == 1:
                dfs(sheep, wolf + 1, info, edges)
            else:
                dfs(sheep + 1, wolf, info, edges)

            # 다른 부분 또한 방문 확인 위해 원복
            v[j] = 0


def solution(info, edges):
    global v

    v = [0 for _ in range(len(info))]
    # 첫번째 방문
    v[0] = 1

    # sheep, wolf
    dfs(1, 0, info, edges)

    return max(result)

# 내 풀이(개선 중)
"""
양 모으기
# 조건
각 노드 방문시 양과 늑대가 따라옴
늑대가 양보다 같거나 많을 경우 양이 다 잡아먹힘

최대한 많은 양을 모아서 루트 노드로 돌아오기
그래프 형태로 볼 때 dfs 생각 방향


# info: i번 노드의 양 또는 늑대 여부
# edges: 연결된 두 노드를 나타냄

#생각방향

자식 노드를 거치려면 부모노드의 동물을 거쳐야한다
단순 생각 방향: 완탐 후 최대 양을 표현하면 된다
info를 숫자로 표현 후 순열로 한 후 모든 경우의 수를 표현가능
양을 최대로 모은 후 늑대가 있는 곳으로 가야한다
모든 노드들의 양이 최대 늑대 최소 값들을 구해야한다
dfs로 풀었던 등대 문제 생각
"""

from collections import defaultdict
from itertools import permutations


def solution(info, edges):
    # 연결된 자식 노드 확인
    m = defaultdict(list)

    # 부모 노드 확인
    check = defaultdict(int)

    for i, j in edges:
        m[i].append(j)
        check[j] = i

    num = [False for k in range(len(info))]

    result = 0

    wolf = 0
    sheep = 0

    return 0

# 다른 사람 풀이

from collections import defaultdict

answer = -1


def solution(info, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    def dfs(cur, sheep, wolf, next_set):
        sheep += info[cur] ^ 1
        wolf += info[cur]

        if sheep <= wolf:
            return
        if sheep > wolf:
            global answer
            answer = max(answer, sheep)
            for next_ in next_set:
                temp = set(graph.get(next_, []))
                next_set |= temp
                next_set -= set([next_])
                dfs(next_, sheep, wolf, next_set)
                next_set |= set([next_])
                next_set -= temp


    dfs(0, 0, 0, set(graph.get(0)))
    print(answer)
    return answer