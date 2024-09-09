"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/42898
"""
# 내 풀이
from collections import deque


def solution(m, n, puddles):
    puddles = set(list(map(tuple, puddles)))

    check = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(2, m + 1):
        if not (i, 1) in puddles:
            check[1][i] = 1
        else:
            break

    for j in range(2, n + 1):
        if not (1, j) in puddles:
            check[j][1] = 1
        else:
            break

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            if not (j, i) in puddles:
                check[i][j] = check[i - 1][j] + check[i][j - 1]
            else:
                check[i][j] = 0

    return check[n][m] % 1000000007