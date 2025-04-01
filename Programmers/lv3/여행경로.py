"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/43164
"""

# 풀이 과정
from collections import deque


def solution(tickets):
    t = list(map(tuple, tickets))

    trip = len(tickets)

    q = deque([])

    for start, arrive in t:
        if start == "ICN":
            q.append([(start, arrive)])

    result = []

    while q:
        check = q.popleft()

        if len(check) == trip:
            result.append(check)
            continue

        for start, arrive in t:
            if check[-1][1] == start and check.count((start, arrive)) != t.count((start, arrive)):
                q.append(check + [(start, arrive)])

    result = deque(result)

    answer = []
    new = []

    while result:
        r = result.popleft()
        new = []

        for i in range(trip):
            new.append(r[i][0])

        new.append(r[-1][1])

        answer += [new]

        new = []

    answer.sort()

    return answer[0]