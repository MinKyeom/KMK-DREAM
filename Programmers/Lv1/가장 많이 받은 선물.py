"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/258712
"""

# 풀이 과정
from collections import defaultdict
from itertools import combinations


def solution(friends, gifts):
    f = friends
    g = gifts

    # 주고받은 선물 관계
    person = defaultdict(int)

    # 선물 지수
    point = defaultdict(int)

    next_month = defaultdict(int)

    for check in gifts:
        c = check.split(" ")
        give, receive = c[0], c[1]

        # 포인트
        point[give] += 1
        point[receive] -= 1

        # 둘 사이의 관계
        person[check] += 1

        next_month[give] = 0
        next_month[receive] = 0

    rotations = list(combinations(f, 2))

    for one, two in rotations:
        if person[one + " " + two] > person[two + " " + one]:
            next_month[one] += 1
        elif person[one + " " + two] < person[two + " " + one]:
            next_month[two] += 1
        else:
            if point[one] > point[two]:
                next_month[one] += 1
            elif point[one] < point[two]:
                next_month[two] += 1
            else:
                continue

    result = 0

    for i, j in next_month.items():
        result = max(result, j)

    return result


# 다른 사람 풀이

def solution(friends, gifts):
    answer = 0
    n = len(friends)

    friend_dict = dict()
    for i in range(n):
        friend_dict[friends[i]] = i

    table = [[0] * n for _ in range(n)]

    # 주고 받은 선물 내역 표(table)에 저장
    # 선물 지수(gift_indices) 저장
    gift_indices = [0] * n

    for gift in gifts:
        a, b = gift.split()  # a : 준 사람 b : 받은 사람
        idx1, idx2 = friend_dict[a], friend_dict[b]
        gift_indices[idx1] += 1
        gift_indices[idx2] -= 1
        table[idx1][idx2] += 1

    get_gift = [0] * n
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if table[i][j] > table[j][i]:  # 준 게 더 많을 때
                get_gift[i] += 1
            elif table[i][j] == table[j][i]:  # 주고 받은게 같을 때 or 둘 다 안주고 받았을 때
                if gift_indices[i] > gift_indices[j]:  # 선물 지수 크면 선물 받기
                    get_gift[i] += 1

    answer = max(get_gift)
    return answer

