"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/43105
"""

#내 풀이
import copy


def solution(triangle):
    t = copy.deepcopy(triangle)

    for i in range(1, len(triangle)):
        triangle[i][0] += triangle[i - 1][0]
        triangle[i][len(triangle[i]) - 1] += triangle[i - 1][len(triangle[i - 1]) - 1]
        for j in range(1, len(triangle[i]) - 1):
            triangle[i][j] = max((triangle[i - 1][j - 1] + triangle[i][j]), (triangle[i - 1][j] + triangle[i][j]))

    return max(triangle[len(triangle) - 1])