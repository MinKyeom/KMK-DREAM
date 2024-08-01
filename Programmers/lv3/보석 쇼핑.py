"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/67258
"""

# 내 풀이(개선 중)
"""
이진탐색 
"""

import heapq
from collections import defaultdict
from collections import deque


def solution(gems):
    j = set(gems)
    check = defaultdict(int)

    for i in j:
        check[i] = 0

    heap = []

    new = deque([])
    start, end = 0, 0

    new.append(gems[start])

    while start < len(gems) - 1 and end <= len(gems) - 1:

        if len(j - set(new)) == 0:
            heapq.heappush(heap, (end - start, start, end))

            if start == end:
                end += 1
                new.append(gems[end])

            else:
                start += 1
                new.popleft()

        else:
            end += 1
            if end >= len(gems):
                break
            new.append(gems[end])

    return [heap[0][1] + 1, heap[0][2] + 1]

