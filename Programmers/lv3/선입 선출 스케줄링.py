"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/12920
"""
# 내 풀이
import heapq
from collections import deque


def solution(n, cores):
    c = cores
    first = n

    if len(c) >= n:
        return n

    elif len(c) == 1:
        return 1

    work = []
    count = 0

    # sol heapq: 정확도 100 효율성 부족
    # 주어진 코어 사용
    # for w in range(len(cores)):
    #     heapq.heappush(work,(c[w],w+1,c[w]))
    #     count+=1

    # 시간 초과 발생
    # while count<n:
    #     time,core_num,work_time=heapq.heappop(work)
    #     heapq.heappush(work,(time+(work_time),core_num,work_time))
    #     count+=1

    # sol2 이진탐색(이분탐색)

    left = 1
    right = max(cores) * (n - len(c))
    n -= len(c)

    while left < right:
        mid = (left + right) // 2
        capacity = 0
        for d in cores:
            capacity += mid // d
        if capacity >= n:
            right = mid
        else:
            left = mid + 1

    check = []

    for i in range(len(c)):
        if right % c[i] != 0:
            n -= right // c[i]

        else:
            check.append(i + 1)
            n -= ((right // c[i]) - 1)

    # 끝 부분에는 모두 나머지가 0이더라도 먼저 들어가는 순서에 따라 모든 사이클이 돌기전에 끝날 수 있다
    return check[n - 1]

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