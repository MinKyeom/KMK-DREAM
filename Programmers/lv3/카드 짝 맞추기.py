"""
출처: 프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/72415
"""
# 내 풀이(개선 중)
"""
조작횟수: enter+방향키

목표:남은 카드를 모두 제거하는데 필요한 키 조작 횟수의 최솟값 

생각방향:
카드를 하나 고르면 무조건 그 짝을 무조건 찾아야한다
그 다음 카드를 선택하는 기준은?
배열 자체가 작기 때문에 크기가 중요하진 않다 모든 경우의 수 고려가능 
칸 16개이기 떄문에 카드 종류 최대 8개
뽑을 순서의 카드를 미리 정한 후 그 순서에 맞춰서 뽑은 후 순서 정하기


# 시간적으로 코드가 문제가 없으므로 논리의 틀린 부분이 없기에 수정 후 풀이가능
"""

import copy
from itertools import permutations
from collections import defaultdict
from collections import deque


def solution(board, r, c):
    result = float("inf")

    # 카드 사이의 거리
    distance = defaultdict(list)

    # 현재 위치
    d = [r, c]

    # 카드 종류
    card = []

    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                card.append(board[i][j])

    card = list(set(card))

    # 카드 사이의 위치 미리 계산

    for i in card:

        for v in range(4):
            for w in range(4):
                if board[v][w] == i:
                    distance[i].append([v, w])
        updown = min(1, abs(distance[i][0][0] - distance[i][1][0]))
        side = min(1, abs(distance[i][0][1] - distance[i][1][1]))

        distance[i].append(updown + side)

    turn = list(permutations(card, len(card)))

    turn = list(map(list, turn))

    q = []

    # 카드 뽑는 순서, 현 위치, 총 움직인순서
    for i in turn:
        q.append([i, [r, c], 0])

    q = deque(q)

    while q:
        card_num, now, count = q.popleft()

        if len(card_num) == 0:
            result = min(result, count)
            continue

        # 의미 없는 q 거르기
        elif result < count:
            continue

        # elif count>min(result):
        #     continue

        # 뽑을 카드
        k = card_num.pop()

        one_x, one_y = distance[k][0]
        two_x, two_y = distance[k][1]

        # 각 카드에서 두 위치에 도달할때까지의 거리
        one_updown = min(1, abs(one_x - now[0]))
        one_side = min(1, abs(one_y - now[1]))
        one = one_updown + one_side

        two_updown = min(1, abs(two_x - now[0]))
        two_side = min(1, abs(two_y - now[1]))
        two = two_updown + two_side

        # 어느쪽 카드를 택해야지 정확히 알 수 없음

        # one을 거친 후 two
        o = copy.deepcopy(card_num)
        q.append([o, [two_x, two_y], count + one + 2 + distance[k][2]])  # +2 엔터키 누름

        # two를 거친 후 one
        t = copy.deepcopy(card_num)
        q.append([t, [one_x, one_y], count + two + 2 + distance[k][2]])  # +2 엔터키 누름

    return result