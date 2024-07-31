"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/67259
"""
# 내 풀이
"""
0:비어있음 1:벽이 있음
start:(0,0) destination:(n-1,n-1)

목표: 최소 비용으로 건설하기 

생각 방향: 게임 보드를 활용 > bfs or dfs

"""
from collections import deque
import copy
import heapq


# 수직 확인
def check(direction, direc):
    # 수직 여부
    P = False

    if direction == "up" or direction == "down":
        one = True
    else:
        one = False

    if direc == "up" or direc == "down":
        two = True
    else:
        two = False

    if one == two:
        return P
    else:
        return True


def solution(board):
    result = float("inf")

    b = board

    # 행,열
    m = len(board)
    n = len(board[0])

    # [[0, 1], [1, 0], [-1, 0], [0, -1]];
    # 방향성 확인
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    d = ["right", "left", "down", "up"]

    # {"right":float("inf"),"left":float("inf"),"down":float("inf"),"up":float("inf")}
    cost_table = [[0] * len(board[0]) for i in range(len(board))]

    for i in range(len(b)):
        for j in range(len(b)):
            cost_table[i][j] = {"right": float("inf"), "left": float("inf"), "down": float("inf"), "up": float("inf")}

    # 현 위치(x,y), 방향,비용
    q = [(0, (0, 0), "stop")]

    while q:
        cost, location, direction = heapq.heappop(q)

        # 위치
        x, y = location[0], location[1]

        if x == m - 1 and y == n - 1:
            cost_table[x][y][direction] = min(cost, cost_table[x][y][direction])
            continue

        # # 방문처리
        # if cost_table[x][y]<cost-600:
        #     continue
        # else:
        #     cost_table[x][y]=cost

        for nx, ny, direc in zip(dx, dy, d):
            # 해당판 내부 확인
            if 0 <= x + nx < m and 0 <= y + ny < n:
                if board[x + nx][y + ny] == 0:

                    # 방향성 체크
                    if direction == "stop":
                        heapq.heappush(q, (cost + 100, (x + nx, y + ny), direc))
                        cost_table[x + nx][y + ny][direc] = cost + 100
                    else:
                        p = check(direction, direc)

                        if p == True:
                            if cost_table[x + nx][y + ny][direc] < cost + 600:
                                continue
                            # 수직 + 직선 거리도 이동
                            heapq.heappush(q, (cost + 600, (x + nx, y + ny), direc))
                            cost_table[x + nx][y + ny][direc] = cost + 600

                        else:
                            if cost_table[x + nx][y + ny][direc] < cost + 100:
                                continue
                            heapq.heappush(q, (cost + 100, (x + nx, y + ny), direc))
                            cost_table[x + nx][y + ny][direc] = cost + 100

    result = float("inf")
    for i in cost_table[len(b) - 1][len(b) - 1].values():
        result = min(result, i)

    return result

# 내 풀이(개선 중)
"""
0:비어있음 1:벽이 있음
start:(0,0) destination:(n-1,n-1)

목표: 최소 비용으로 건설하기 

생각 방향: 게임 보드를 활용 > bfs or dfs
"""
from collections import deque
import copy
import heapq


# 수직 확인
def check(direction, direc):
    # 수직 여부
    P = False

    if direction == "up" or direction == "down":
        one = True
    else:
        one = False

    if direc == "up" or direc == "down":
        two = True
    else:
        two = False

    if one == two:
        return P
    else:
        return True


def solution(board):
    result = float("inf")

    b = board

    # 행,열
    m = len(board)
    n = len(board[0])

    # [[0, 1], [1, 0], [-1, 0], [0, -1]];
    # 방향성 확인
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    d = ["right", "left", "down", "up"]

    cost_table = [[float("inf")] * len(board[0]) for i in range(len(board))]

    # 현 위치(x,y), 방향,비용
    q = [(0, (0, 0), "stop")]

    while q:
        cost, location, direction = heapq.heappop(q)

        # 새로운 방문판 생성
        # new_v=copy.deepcopy(v)

        # 위치
        x, y = location[0], location[1]

        # if x==m-1 and y==n-1:
        #     continue

        # # 방문처리
        # new[x][y]=True
        if cost_table[x][y] < cost:
            continue
        else:
            cost_table[x][y] = cost

        for nx, ny, direc in zip(dx, dy, d):
            # 해당판 내부 확인
            if 0 <= x + nx < m and 0 <= y + ny < n:
                if board[x + nx][y + ny] == 0:

                    # 방향성 체크
                    if direction == "stop":
                        num = min(cost_table[x + nx][y + ny], cost + 100)
                        heapq.heappush(q, (num, (x + nx, y + ny), direc))
                    else:
                        p = check(direction, direc)

                        if p == True:
                            # 수직 + 직선 거리도 이동
                            heapq.heappush(q, (cost + 600, (x + nx, y + ny), direc))

                        else:
                            heapq.heappush(q, (cost + 100, (x + nx, y + ny), direc))

    return cost_table[len(b) - 1][len(b) - 1]

# 내 풀이(개선 중)
"""
0:비어있음 1:벽이 있음
start:(0,0) destination:(n-1,n-1)

목표: 최소 비용으로 건설하기 

생각 방향: 게임 보드를 활용 > bfs or dfs
"""
from collections import deque
import copy
import heapq


# 수직 확인
def check(direction, direc):
    # 수직 여부
    P = False

    if direction == "up" or direction == "down":
        one = True
    else:
        one = False

    if direc == "up" or direc == "down":
        two = True
    else:
        two = False

    if one == two:
        return P
    else:
        return True


def solution(board):
    result = float("inf")

    b = board

    # 행,열
    m = len(board)
    n = len(board[0])

    # [[0, 1], [1, 0], [-1, 0], [0, -1]];
    # 방향성 확인
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    d = ["right", "left", "down", "up"]

    cost_table = [[float("inf")] * len(board[0]) for i in range(len(board))]

    # 현 위치(x,y), 방향,비용
    q = [(0, (0, 0), "stop")]

    while q:
        cost, location, direction = heapq.heappop(q)

        # 새로운 방문판 생성
        # new_v=copy.deepcopy(v)

        # 위치
        x, y = location[0], location[1]

        # if x==m-1 and y==n-1:
        #     continue

        # # 방문처리
        # new[x][y]=True

        for nx, ny, direc in zip(dx, dy, d):

            # 해당판 내부 확인
            if 0 <= x + nx < m and 0 <= y + ny < n:
                if cost_table[x + nx][y + ny] >= cost and board[x + nx][y + ny] == 0:

                    # 방향성 체크
                    if direction == "stop":
                        heapq.heappush(q, (cost + 100, (x + nx, y + ny), direc))
                        cost_table[x + nx][y + ny] = min(cost_table[x + nx][y + ny], cost + 100)
                    else:
                        p = check(direction, direc)

                        if p == True:
                            # 수직 + 직선 거리도 이동
                            heapq.heappush(q, (cost + 600, (x + nx, y + ny), direc))
                            cost_table[x + nx][y + ny] = min(cost_table[x + nx][y + ny], cost + 600)
                        else:
                            heapq.heappush(q, (cost + 100, (x + nx, y + ny), direc))
                            cost_table[x + nx][y + ny] = min(cost_table[x + nx][y + ny], cost + 100)

    return cost_table[len(b) - 1][len(b) - 1]

# 다른 사람 풀이

from heapq import heappop, heappush
from sys import maxsize


def solution(board):
    N = len(board)
    costBoard = [[[maxsize] * N for _ in range(N)] for _ in range(4)]
    for i in range(4): costBoard[i][0][0] = 0

    # BFS
    heap = [(0, 0, 0, 0), (0, 0, 0, 2)]
    while heap:
        cost, x, y, d = heappop(heap)

        # 4방향 이동
        for dx, dy, dd in ((1, 0, 0), (-1, 0, 1), (0, 1, 2), (0, -1, 3)):
            nx, ny = x + dx, y + dy

            # 경계 침범 or 벽
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[ny][nx]: continue

            # 이동비용 갱신
            newCost = cost + (100 if d == dd else 600)

            # 최소비용 갱신
            if costBoard[dd][ny][nx] > newCost:
                costBoard[dd][ny][nx] = newCost
                heappush(heap, (newCost, nx, ny, dd))

    return min(costBoard[0][N - 1][N - 1], costBoard[1][N - 1][N - 1], costBoard[2][N - 1][N - 1],
               costBoard[3][N - 1][N - 1])