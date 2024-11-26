"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/12920
"""

# 내 풀이_개선 중
import heapq


def solution(n, cores):
    c = cores
    first = n

    if len(c) >= n:
        return n

    elif len(c) == 1:
        return 1

    work = []
    count = 0

    # 주어진 코어 사용
    for w in range(len(cores)):
        heapq.heappush(work, (c[w], w + 1, c[w]))
        count += 1

    while count < n:
        time, core_num, work_time = heapq.heappop(work)
        heapq.heappush(work, (time + (work_time), core_num, work_time))
        count += 1

    return core_num