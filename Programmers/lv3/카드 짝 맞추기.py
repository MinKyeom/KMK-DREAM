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
만약, 해당 방향에 카드가 하나도 없다면 그 방향의 가장 마지막 칸으로 이동합니다. < 중요한 생각의 포인트 기점

"""

import copy
from itertools import combinations
from itertools import permutations
from collections import defaultdict
from collections import deque


# 두 점 사이의 거리재기
def gap(now, board, destination, card_num, another):
    # 이미 뽑힌지 여부에 관한 체크 set으로 O(1)으로 검색할 떄 시간 감소
    check = set(card_num)

    # 현 위치에 대한 정리
    x = now[0]
    y = now[1]

    # 목적지
    v = destination[0]
    w = destination[1]

    # 현위치 = 목적지
    if now == destination:
        return 0

    q = deque([[x, y]])

    turn = 1
    new = []

    while q:
        dx, dy = q.popleft()

        # 상
        count = 0
        while True:
            # 벽에 부딪침
            if dx - count < 0:
                new.append([0, dy])
                break

            # 카드가 존재하여 멈춤
            elif board[dx - count][dy] in check or [dx - count, dy] == another:
                new.append([dx - count, dy])
                break

            # 목적지에 도착
            elif [dx - count, dy] == destination:
                return turn

            count += 1
        # 하
        count = 0
        while True:
            # 벽에 부딪침
            if dx + count > 3:
                new.append([3, dy])
                break

            # 카드가 존재하여 멈춤
            elif board[dx + count][dy] in check or [dx + count, dy] == another:
                new.append([dx + count, dy])
                break

            # 목적지에 도착
            elif [dx + count, dy] == destination:
                return turn

            count += 1

        # 좌
        count = 0
        while True:
            # 벽에 부딪침
            if dy - count < 0:
                new.append([dx, 0])
                break

            # 카드가 존재하여 멈춤
            elif board[dx][dy - count] in check or [dx, dy - count] == another:
                new.append([dx, dy - count])
                break

            # 목적지에 도착
            elif [dx, dy - count] == destination:
                return turn

            count += 1

        # 우
        count = 0
        while True:
            # 벽에 부딪침
            if dy + count > 3:
                new.append([dx, 3])
                break

            # 카드가 존재하여 멈춤
            elif board[dx][dy + count] in check or [dx, dy + count] == another:
                new.append([dx, dy + count])
                break

            # 목적지에 도착
            elif [dx, dy + count] == destination:
                return turn

            count += 1

        # 재조사
        if len(q) == 0:
            q = list(q)
            q += new
            new = []
            q = deque(q)

            # 한턴씀
            turn += 1

    return turn


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

    for i in card:

        for v in range(4):
            for w in range(4):
                if board[v][w] == i:
                    distance[i].append([v, w])

    turn = list(permutations(card, len(card)))
    turn = list(map(list, turn))

    q = []

    # 카드 뽑는 순서, 현 위치, 총 움직인순서
    for i in turn:
        q.append([i, [r, c], 0])

    q = deque(q)

    while q:
        card_num, now, count = q.popleft()

        # 더이상 맞출 카드가 없을 때
        if len(card_num) == 0:
            result = min(result, count)
            continue

        # 의미 없는 q 거르기
        elif result < count:
            continue

        # 뽑을 카드 정하기
        k = card_num.pop()

        # 카드 2장의 위치
        one_x, one_y = distance[k][0]
        two_x, two_y = distance[k][1]
        point_one = [one_x, one_y]
        point_two = [two_x, two_y]

        # 각 카드에서 두 위치에 도달할때까지의 거리
        one = gap(now, board, point_one, card_num, point_two)

        print(one)
        break

        two = gap(now, baord, point_two, card_num, point_one)

        # 어느쪽 카드를 택해야 이득일지 정확히 알 수 없음

        # one을 거친 후 two
        o = copy.deepcopy(card_num)
        q.append([o, [two_x, two_y], count + one + 2 + distance[k][2]])  # +2 엔터키 누름

        # two를 거친 후 one
        t = copy.deepcopy(card_num)
        q.append([t, [one_x, one_y], count + two + 2 + distance[k][2]])  # +2 엔터키 누름

    return 0
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