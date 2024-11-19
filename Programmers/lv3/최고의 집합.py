"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/12938
"""

# 내 풀이_개선 중
from collections import deque


def solution(n, s):
    if s == 1:
        return [-1]

    result = 0

    result_set = []

    num = int(s ** 0.5)
    print(num)

    for i in range(1, num + 1):
        if (s / i) == int(s / i):
            if int(s / i) * i > result:
                result = (s / i) * i
                result_set = {i, int(s / i)}

    print(result_set)

    return 0