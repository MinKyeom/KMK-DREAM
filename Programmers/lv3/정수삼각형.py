"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/43105
"""

# 풀이 과정
import copy


def solution(triangle):
    t = copy.deepcopy(triangle)

    for i in range(1, len(triangle)):
        triangle[i][0] += triangle[i - 1][0]
        triangle[i][len(triangle[i]) - 1] += triangle[i - 1][len(triangle[i - 1]) - 1]
        for j in range(1, len(triangle[i]) - 1):
            triangle[i][j] = max((triangle[i - 1][j - 1] + triangle[i][j]), (triangle[i - 1][j] + triangle[i][j]))

    return max(triangle[len(triangle) - 1])

# 다른 사람 풀이
def solution(triangle):
    dp = []
    for t in range(1, len(triangle)):
        for i in range(t+1):
            if i == 0:
                triangle[t][0] += triangle[t-1][0]
            elif i == t:
                triangle[t][-1] += triangle[t-1][-1]
            else:
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
    return max(triangle[-1])