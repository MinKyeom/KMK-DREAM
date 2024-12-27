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