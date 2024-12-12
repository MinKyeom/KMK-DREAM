"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/340211
"""

# 풀이 과정_개선 중 
"""
로봇별로 현 위치 딕셔너리 구현
출발하는 순간 마다 매 로봇 위치 변화 및 현 위치 운송 도착 여부 확인 후 다음 위치 있나 다시 체크

그리고 그 후 로봇 위치 별로 for 문 구현 후 충돌한 위치를 set 문에 넣은 후 중복 제거 및 여러 대 충돌 여부 따로 처리할 필요 없게 제거
"""
from collections import deque, defaultdict


def solution(points, routes):
    routes = list(map(deque, routes))

    crush = 0

    robot = defaultdict(int)
    check = dict([])

    return 0
    for i, j in enumerate(routes):
        start = (j[0] - 1)
        nextpoint = j[1]
        robot[i] = (points[start][0], points[start][1], nextpoint)

    while routes:
        # 경로 이동
        for number, now in robot.items():
            return 0
            # 운송 도착 여부
            p = routes[number]

            p_x, p_y = points[p - 1]

            if [now[0], now[1]] == [p_x, p_y]:
                break
            x, y, check = now[0], now[1], now[2]

        break
        # 충돌 확인

    return crush