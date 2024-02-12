# 내 풀이(개선 중)
from collections import deque
from itertools import combinations
# bfs
# 두 수레를 동시에 사방위로 이동시킨 후의 위치를 조합하여 그 위치를 동시에 다시 bfs를 실행하여 최솟값을 구하기

def solution(maze):
    m = len(maze)  # 세로
    n = len(maze[0])  # 가로
    v_r = [[False for _ in range(n)] for _ in range(m)]
    v_b = [[False for _ in range(n)] for _ in range(m)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    # 장애물 및 현 위치 및 도착지점 확인
    for i in range(m):
        for j in range(n):
            if maze[i][j] == 5:
                v_r[i][j] = True
                v_b[i][j] = True
            elif maze[i][j] == 1:
                r_s = [i, j]
                v_r[i][j] = True
            elif maze[i][j] == 2:
                b_s = [i, j]
                v_b[i][j] = True
            elif maze[i][j] == 3:
                v_r[i][j] = "red"
            elif maze[i][j] == 4:
                v_b[i][j] = "blue"

    q = deque([[r_s, b_s]])
    new = []  # q가 끝났을 때 더해줄 큐

    while q:
        r, b = q.popleft()
        r_x, r_y = r[0], r[1]
        b_x, b_y = b[0], b[1]
        new_r = []
        new_b = []

        for x, y in zip(dx, dy):
            if 0 <= r_x + x < m and 0 <= r_y + y < n and v_r[r_x + x][r_y + y] == False:
                new_r.append([r_x + x, r_y + y])
            if 0 <= b_x + x < m and 0 <= b_y + y < n and v_b[b_x + x][b_y + y] == False:
                new_b.append([b_x + x, b_y + y])

        # 새로운 큐 제한 조건에 따른 분류
        for i in new_r:
            for j in new_b:
                if i != j:
                    if j == r and i == b:
                        continue
                    else:
                        new.append([i, j])
        print(new)
        break
    answer = 0
    return answer