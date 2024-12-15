"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/340211
"""
# 풀이과정 _ 개선 중
"""
로봇별로 현 위치 딕셔너리 구현
출발하는 순간 마다 매 로봇 위치 변화 및 현 위치 운송 도착 여부 확인 후 다음 위치 있나 다시 체크

그리고 그 후 로봇 위치 별로 for 문 구현 후 충돌한 위치를 set 문에 넣은 후 중복 제거 및 여러 대 충돌 여부 따로 처리할 필요 없게 제거
"""
from collections import deque, defaultdict


def solution(points, routes):
    routes = list(map(deque, routes))
    arrive = [False] * len(routes)

    crush = 0

    robot = defaultdict(int)
    check = dict([])

    # 로봇 번호, 로봇이 갈 포인트
    for i, j in enumerate(routes):
        # 포인트 번호
        start = (j[0] - 1)

        # 시작 위치
        x, y = points[start][0], points[start][1]
        robot[i] = [x, y]

        # 현 위치 도달과 동시에 포인트 제거
        j.popleft()

    while True:

        k = set([])

        # 첫 포인트 충돌 확인 작업 실시
        for r, now in robot.items():
            for x, y in robot.items():
                if r == x:
                    continue
                else:
                    if now == y and now != [-1, -1]:
                        k.add(tuple(now))

        crush += len(k)

        # 이동
        for r, p in enumerate(routes):

            if len(p) == 0:
                arrive[r] = True
                robot[r] = [-1, -1]


            # 이동
            else:
                # return "check"
                num = p[0] - 1
                x, y = robot[r][0], robot[r][1]
                n, m = points[num][0], points[num][1]

                if robot[r] == [n, m]:
                    p.popleft()

                    robot[r] = [-1, -1]

                else:
                    if x > n:
                        robot[r][0] -= 1
                    elif x < n:
                        robot[r][0] += 1
                    elif y > m:
                        robot[r][1] -= 1
                    elif y < m:
                        robot[r][1] += 1

            if arrive.count(True) == len(arrive):
                return crush

    return 0

# 풀이과정 _ 개선 중
"""
로봇별로 현 위치 딕셔너리 구현
출발하는 순간 마다 매 로봇 위치 변화 및 현 위치 운송 도착 여부 확인 후 다음 위치 있나 다시 체크

그리고 그 후 로봇 위치 별로 for 문 구현 후 충돌한 위치를 set 문에 넣은 후 중복 제거 및 여러 대 충돌 여부 따로 처리할 필요 없게 제거
"""
from collections import deque, defaultdict


def solution(points, routes):
    routes = list(map(deque, routes))
    arrive = [False] * len(routes)

    crush = 0

    robot = defaultdict(int)
    check = dict([])

    # 로봇 번호, 로봇이 갈 포인트
    for i, j in enumerate(routes):
        # 포인트 번호
        start = (j[0] - 1)

        # 시작 위치
        x, y = points[start][0], points[start][1]
        robot[i] = [x, y]

        # 현 위치 도달과 동시에 포인트 제거
        j.popleft()

    while True:

        k = set([])

        # 첫 포인트 충돌 확인 작업 실시
        for r, now in robot.items():
            for x, y in robot.items():
                if r == x:
                    continue
                else:
                    if now == y and now != [-1, -1]:
                        k.add(tuple(now))

        crush += len(k)

        # 이동
        for r, p in enumerate(routes):

            if len(p) == 0:
                arrive[r] = True
                robot[r] = [-1, -1]


            # 이동
            else:
                # return "check"
                num = p[0] - 1
                x, y = robot[r][0], robot[r][1]
                n, m = points[num][0], points[num][1]

                if robot[r] == [n, m]:
                    p.popleft()

                    robot[r] = [-1, -1]

                else:
                    if x > n:
                        robot[r][0] -= 1
                    elif x < n:
                        robot[r][0] += 1
                    elif y > m:
                        robot[r][1] -= 1
                    elif y < m:
                        robot[r][1] += 1

            if arrive.count(True) == len(arrive):
                return crush

    return 0

# 풀이 과정_ 개선 중

"""
로봇별로 현 위치 딕셔너리 구현
출발하는 순간 마다 매 로봇 위치 변화 및 현 위치 운송 도착 여부 확인 후 다음 위치 있나 다시 체크

그리고 그 후 로봇 위치 별로 for 문 구현 후 충돌한 위치를 set 문에 넣은 후 중복 제거 및 여러 대 충돌 여부 따로 처리할 필요 없게 제거
"""
from collections import deque, defaultdict


def solution(points, routes):
    routes = list(map(deque, routes))
    arrive = [False] * len(routes)

    crush = 0

    robot = defaultdict(int)
    check = dict([])

    # 로봇 번호, 로봇이 갈 포인트
    for i, j in enumerate(routes):
        # 포인트 번호
        start = (j[0] - 1)

        # 시작 위치
        x, y = points[start][0], points[start][1]
        robot[i] = [x, y]

        # 현 위치 도달과 동시에 포인트 제거
        j.popleft()

    while True:

        k = set([])

        # 첫 포인트 충돌 확인 작업 실시
        for r, now in robot.items():
            for x, y in robot.items():
                if r == x:
                    continue
                else:
                    if now == y and now != [-1, -1]:
                        k.add(tuple(now))

        # 이동
        for r, p in enumerate(routes):

            if len(p) == 0:
                arrive[p] = True
                robot[r] = [-1, -1]


            # 이동
            else:
                # return "check"
                num = p[0] - 1
                x, y = robot[r][0], robot[r][1]
                n, m = points[num][0], points[num][1]

                if robot[r] == [n, m]:
                    p.popleft()

                    robot[r] = [-1, -1]

                else:
                    if x > n:
                        robot[r][0] -= 1
                    elif x < n:
                        robot[r][0] += 1
                    elif y > m:
                        robot[r][1] -= 1
                    elif y < m:
                        robot[r][1] += 1

            if arrive.count(True) == len(arrive):
                return "check"

    return 0

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


# 다른 사람 풀이
from collections import Counter
def solution(points, routes):
    conflict = 0
    robot_cnt = len(routes)
    max_robot_move_routes = 0

    robot_move_routes = [[] for _ in range(robot_cnt)]

    for i in range(robot_cnt):
        for j in range(len(routes[i])-1):
            start_x, start_y = points[routes[i][j]-1]
            end_x, end_y = points[routes[i][j+1]-1]

            robot_move_x, robot_move_y = end_x - start_x, end_y - start_y

            if j == 0:
                robot_move_routes[i].append([start_x, start_y])

            for k in range(abs(robot_move_x) + abs(robot_move_y)):
                if robot_move_x > 0:
                    robot_move_routes[i].append([start_x+1, start_y])
                    start_x += 1
                    robot_move_x -= 1
                elif robot_move_x < 0:
                    robot_move_routes[i].append([start_x-1, start_y])
                    start_x -= 1
                    robot_move_x += 1
                else:
                    if robot_move_y > 0:
                        robot_move_routes[i].append([start_x, start_y+1])
                        start_y += 1
                        robot_move_y -= 1
                    elif robot_move_y < 0:
                        robot_move_routes[i].append([start_x, start_y-1])
                        start_y -= 1
                        robot_move_y += 1

            max_robot_move_routes = max(max_robot_move_routes, len(robot_move_routes[i]))

    for i in range(max_robot_move_routes):
        current_time_robot_pos = []

        for j in range(robot_cnt):
            if i <= len(robot_move_routes[j])-1:
                current_time_robot_pos.append(tuple(robot_move_routes[j][i]))

        validate_current_pos = Counter(current_time_robot_pos)
        for pos in validate_current_pos.values():
            if pos >= 2:
                conflict += 1

    return conflict