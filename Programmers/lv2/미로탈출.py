# 내 풀이
def solution(maps):
    from collections import deque
    result = 0
    # 가로 길이
    m = len(maps[0])
    # 세로 길이
    n = len(maps)

    board = [[" "] * m for k in range(n)]

    check = deque()
    maps_key = []
    maps_door = []

    for a in range(n):
        for b in range(m):
            if maps[a][b] == "S":
                check.append([a, b, 0])
            if maps[a][b] == "E":
                maps_door.append([a, b])
            if maps[a][b] == "L":
                maps_key.append([a, b])
            if check and maps_key and maps_door:
                break

    o, p = maps_key[0]

    q, r = maps_door[0]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while check:
        c, d, e = check.popleft()
        for v, w in zip(dx, dy):
            new_c = c + v
            new_d = d + w
            if 0 <= new_c < n and 0 <= new_d < m and not maps[new_c][new_d] == "X":
                if board[new_c][new_d] == " ":
                    check.append([new_c, new_d, e + 1])
                    board[new_c][new_d] = e + 1
                else:
                    if board[new_c][new_d] > e + 1:
                        check.append([new_c, new_d, e + 1])
                        board[new_c][new_d] = e + 1

    if board[o][p] == " " or board[q][r] == " ":
        return -1

    else:
        new_board = [[" "] * m for k in range(n)]
        new_check = deque([[o, p, 0]])
        while new_check:
            f, g, h = new_check.popleft()
            for v, w in zip(dx, dy):
                new_f = f + v
                new_g = g + w
                if 0 <= new_f < n and 0 <= new_g < m and not maps[new_f][new_g] == "X":
                    if new_board[new_f][new_g] == " ":
                        new_check.append([new_f, new_g, h + 1])
                        new_board[new_f][new_g] = h + 1
                    else:
                        if new_board[new_f][new_g] > h + 1:
                            new_check.append([new_f, new_g, h + 1])
                            new_board[new_f][new_g] = h + 1

    return board[o][p] + new_board[q][r]

# 다른 사람 풀이
from collections import deque

def fast_way_bfs(maps, start, end):
    visited = [[0] * 1000 for _ in range(1000)]
    drs, dcs = [0, 0, 1, -1], [1, -1, 0, 0]
    queue = deque()
    queue.append(start)

    distance = 0
    while len(queue):
        r, c, dist = queue.popleft()
        if not(0 <= r < len(maps)) or not(0 <= c < len(maps[0])):
            continue
        if maps[r][c] == 'X' or visited[r][c] == True:
            continue
        if maps[r][c] == maps[end[0]][end[1]]:
            return dist
        # print(queue)
        # print(x, y, maps[x][y], dist)

        visited[r][c] = True

        for dr, dc in zip(drs, dcs):
            if 0 <= r+dr < len(maps) and 0 <= c+dc < len(maps[0]):
                if maps[r+dr][c+dc] != 'X' and visited[r+dr][c+dc] == False:
                    queue.append((r+dr, c+dc, dist+1))

    return -1


def solution(maps):
    start, lever, end = 0, 0, 0
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == 'S':
                start = r, c, 0
            if maps[r][c] == 'E':
                end = r, c, 0
            if maps[r][c] == 'L':
                lever = r, c, 0

    first, second = fast_way_bfs(maps, start, lever), fast_way_bfs(maps, lever, end)
    if -1 in [first, second]:
        return -1
    return first + second
