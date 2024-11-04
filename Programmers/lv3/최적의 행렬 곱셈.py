"""
출처 프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/12942
"""
# 내 풀이_개선 중
"""
큰 수를 여러 번 안쓰게 소거
"""
from collections import defaultdict, deque
import copy


def solution(matrix_sizes):
    m = matrix_sizes

    front = copy.deepcopy(m)
    back = copy.deepcopy(m)

    front = deque(sorted(front, key=lambda x: (-x[0])))
    back = deque(sorted(back, key=lambda x: (-x[1])))

    m = deque(m)

    result = []

    while len(front) > 1 and len(back) > 1:
        x, y = back.popleft()
        v, w = front.popleft()

        i = front.index([x, y])
        del front[i]
        j = back.index([v, w])
        del back[j]

        result.append(x * y * w)

        front.append([x, w])
        back.append([x, w])
        front = deque(sorted(front, key=lambda x: (-x[0])))
        back = deque(sorted(back, key=lambda x: (-x[1])))

        print(front, back)

    return sum(result)
