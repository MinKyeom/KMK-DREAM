#14502_연구소_bfs_gold5

# 1
from itertools import combinations
from copy import deepcopy

# 0: 빈 칸, 1: 벽, 2: 바이러스, 2이상 10미만
dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]

# N: 세로, M: 가로
N, M = map(int, input().split())

W = 3  # 벽의 수

# 배열 입력
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))


def cnt_sf(_arr):
    _cnt = 0
    for _i in range(N):
        for _j in range(M):
            if _arr[_i][_j] == 0:
                _cnt += 1
    return _cnt
"""

내가 이해한 정도:안전지대 개수 찾기

"""

def virus_spread(x, y):
    # if virus then spread
    if arr[x][y] == 2:
        # spread recursively
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            # in range
            if 0 <= nx < N and 0 <= ny < M:
                # if not spread before and empty space
                if arr[nx][ny] == 0:
                    # spread
                    arr[nx][ny] = 2
                    virus_spread(nx, ny)


empty_space = []  # empty space
for i in range(N):
    for j in range(M):
        # possible wall space
        if arr[i][j] == 0:
            empty_space.append((i, j))

# possible wall zone
pos = combinations(empty_space, W)
answer = 0
tmp = deepcopy(arr)

for state in pos:
    arr = deepcopy(tmp)
    # build new wall
    for x, y in state:
        arr[x][y] = 1

    # virus spread
    for i in range(N):
        for j in range(M):
            virus_spread(i, j)
    answer = max(answer, cnt_sf(arr))

print(answer)