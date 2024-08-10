"""
프로그래머스
출처:https://school.programmers.co.kr/learn/courses/30/lessons/60063
"""

# 내 풀이(개선 중)
"""
bfs 
"""
from collections import deque


def solution(board):
    m = len(board)
    n = len(board)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 회전8,이동4

    robot = ((0, 0), (0, 1))

    q = deque([((0, 0), (0, 1), 0)])
    visit = set([])

    while q:
        z = q.popleft()

        if (m - 1, n - 1) in z:
            return z[2]

        x1, x2 = z[0][0], z[0][1]
        y1, y2 = z[1][0], z[1][1]
        count = z[2]

        if not ((z[0]), (z[1])) in visit or not ((z[1]), (z[0])) in visit:
            visit.add(((z[0]), (z[1])))
            visit.add(((z[1]), (z[0])))

        else:
            continue

        # 이동
        for nx, ny in zip(dx, dy):
            if 0 <= nx + x1 < m and 0 <= ny + x2 < n and 0 <= nx + y1 < m and 0 <= ny + y2 < n:
                if board[nx + x1][ny + x2] == 0 and board[nx + y1][ny + y2] == 0 and not ((nx + x1, ny + x2), (
                nx + y1, ny + y2)) in visit and not ((nx + y1, ny + y2), (nx + x1, ny + x2)) in visit:
                    q.append(((nx + x1, ny + x2), (nx + y1, ny + y2), count + 1))

            # # 회전
            # for nx,ny in zip(dx,dy):
            if 0 <= nx + x1 < m and 0 <= ny + x2 < n:
                if board[nx + x1][ny + x2] == 0 and not ((nx + x1, ny + x2), (y1, y2)) in visit and not ((y1, y2), (
                nx + x1, ny + x2)) in visit:
                    q.append(((nx + x1, ny + x2), (y1, y2), count + 1))

            if 0 <= nx + y1 < m and 0 <= ny + y2 < n:
                if board[nx + y1][ny + y2] == 0 and not ((x1, x2), (nx + y1, ny + y2)) in visit and not ((nx + y1,
                                                                                                          ny + y2), (x1,
                                                                                                                     x2)) in visit:
                    q.append(((x1, x2), (nx + y1, ny + y2), count + 1))

    return answer