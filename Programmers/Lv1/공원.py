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


# 다른 사람 풀이
def can_place_mat(park, size):
    # 공원의 행(row)와 열(col) 길이
    rows, cols = len(park), len(park[0])

    # park에서 주어진 size의 돗자리를 놓을 수 있는지 확인
    for i in range(rows - size + 1):
        for j in range(cols - size + 1):
            # size x size 크기의 공간이 모두 '-1'인지 확인
            if all(park[x][y] == '-1' for x in range(i, i + size) for y in range(j, j + size)):
                return True
    return False

def solution(mats, park):
    # 돗자리 크기 내림차순으로 정렬
    mats.sort(reverse=True)

    # 각 돗자리 크기에 대해 놓을 수 있는지 확인
    for size in mats:
        if can_place_mat(park, size):
            return size

    return -1