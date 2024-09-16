"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/42884
"""
# 내 풀이
from collections import defaultdict
from collections import deque
import heapq


def solution(routes):
    check = []
    car_start = defaultdict(set)
    car_end = defaultdict(set)
    for c in range(len(routes)):
        check.append(routes[c][0])
        check.append(routes[c][1])

        car_start[routes[c][0]].add(c)
        car_end[routes[c][1]].add(c)

    start = min(check)
    end = max(check)
    check.sort()

    now = set([])

    result = 0

    check_car = set([])

    # 이전에 발견되던게 지금 발견 안되면 그 지점은 무조건 카메라 설치 필수
    for time in check:
        now = now | car_start[time]

        # 빠지는 차량 발생
        if len(car_end[time]) > 0:
            if len(car_end[time] - check_car) > 0:
                result += 1
                check_car = check_car | car_end[time] | now

    return result

# 내 풀이(개선 중)
from collections import defaultdict
from collections import deque
import heapq


def solution(routes):
    check = []

    for start, end in routes:
        check.append(start)
        check.append(end)

    check.sort()

    car = defaultdict(set)

    for i in check:
        for j in range(len(routes)):
            if routes[j][0] <= i <= routes[j][1]:
                car[i].add(j)

    q = [(0, set([]))]

    result = float("inf")
    check = deque(check)

    while check:
        k = check.pop()
        new = []
        while q:
            n, car_num = q.pop()

            if len(car_num) == len(routes):
                result = min(result, n)
            if n >= result:
                continue
            if len(car_num) == len(car_num | car[k]):
                new.append((n, car_num))
            else:
                new.append((n, car_num))
                new.append((n + 1, car_num | car[k]))

        q += new

    return result

# 내 풀이(개선 중)
from collections import defaultdict
from collections import deque


def solution(routes):
    s = []
    e = []

    for start, end in routes:
        s.append(start)
        e.append(end)

    start = min(s)
    end = max(e)

    car = defaultdict(set)

    for i in range(start, end + 1):
        for j in range(len(routes)):
            if routes[j][0] <= i <= routes[j][1]:
                car[i].add(j)

    q = [(0, set([]))]

    count = start
    result = float("inf")

    while count < end:
        new = []

        while q:
            n, car_num = q.pop()

            if len(car_num) == len(routes):
                result = min(result, n)

            new.append((n, car_num))
            new.append((n + 1, car_num | car[count]))

        q += new
        count += 1

    return result

# 다른 사람 풀이
