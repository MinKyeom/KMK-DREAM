"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/340198
"""


# 풀이 과정
def solution(mats, park):
    # 매트 가로,세로
    m = len(park[0])
    n = len(park)

    b = [[1 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if park[i][j] != "-1":
                b[i][j] = 0

    for i in range(1, n):
        for j in range(1, m):
            b[i][j] = min(b[i - 1][j], b[i - 1][j - 1], b[i][j - 1]) + 1
            if park[i][j] != "-1":
                b[i][j] = 0

    k = set([])

    for i in range(len(b)):
        for j in range(len(b[0])):
            k.add(b[i][j])

    mats.sort(reverse=True)

    for i in mats:
        if i in k:
            return i

    else:
        return -1