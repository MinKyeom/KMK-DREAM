"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/250137
"""


# 풀이 과정
from collections import deque


def solution(bandage, health, attacks):
    # 초기 체력
    h = health

    heal = bandage[1]
    heal_time = bandage[2]
    sequence_time = bandage[0]

    demege = deque([])
    demege_time = deque([])

    for i, j in attacks:
        demege_time.append(i)
        demege.append(j)

    last = demege_time[-1]
    time = 0
    count = 0  # 연속된 시간

    while time < last:
        if time == demege_time[0] - 1:
            h -= demege[0]
            demege_time.popleft()
            demege.popleft()
            time += 1
            # 시간 초기화
            count = 0
            continue

        else:
            if h == health:
                time += 1
                count += 1
                continue
            else:
                h += heal
                count += 1
                time += 1
                if count % sequence_time == 0:
                    h += heal_time
                    h = min(h, health)

        if h <= 0:
            return -1
    if h <= 0:
        return -1

    return h