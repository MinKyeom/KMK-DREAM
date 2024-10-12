"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/42627
"""

# 나의 풀이
# 대기 시간을 줄이기,[요청시점, 소요시간]

import heapq
from collections import deque


def solution(jobs):
    all_work = len(jobs)
    operation = []
    jobs.sort()
    j = deque(jobs)

    time = 0

    # 진행중인 작업
    now = []
    finish = len(jobs)
    result = []

    while finish > 0:

        # 현재 시간에 따른 들어온 작업 구분
        while j:
            w = j.popleft()
            if w[0] <= time:
                now.append(w)
            else:
                j.appendleft(w)
                break

        # 들어온 작업이 없을 경우 시간 추가
        if len(now) == 0:
            time += 1
            continue

        # 새로운 작업 구성
        new = []

        for work in now:
            heapq.heappush(new, [time + work[1], work])

        while new:
            a, b = heapq.heappop(new)
            command, command_finish = b[0], b[1]
            time += b[1]
            result.append(time - b[0])

            # 완료된 작업 제거
            k = now.index(b)
            del now[k]
            finish -= 1

            if len(j) > 0:
                if time >= j[0][0]:
                    break

    return sum(result) // all_work