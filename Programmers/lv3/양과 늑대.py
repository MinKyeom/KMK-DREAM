"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/92343
"""
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