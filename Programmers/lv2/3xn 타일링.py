# 내 풀이(개선 중)
# bfs로 접근했으나 dp로 각 사각형을 쪼개서 계산하는 방향성 생각해보기!
from collections import deque

def solution(n):
    dx = [1, 0]
    dy = [0, 1]

    tri = [[0 for _ in range(n)] for _ in range(3)]

    result = 0

    if (n * 3) % 2 == 1:
        return 0
    else:
        for i in range(3):
            for j in range(n):
                if i == 2 and j == n - 1:
                    result = tri[i - 1][j] + tri[i][j - 1]
                if i + 1 < 3:
                    tri[i + 1][j] = max(tri[i + 1][j], tri[i][j]) + 1
                    result = max(tri[i + 1][j], result)
                if j + 1 < n:
                    tri[i][j + 1] = max(tri[i][j + 1], tri[i][j]) + 1
                    result = max(tri[i][j + 1], result)

    return result % 1000000007

# 다른 사람 풀이