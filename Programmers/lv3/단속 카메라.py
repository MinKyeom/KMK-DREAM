"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/42884
"""
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