# 내 풀이
def solution(board):
    from collections import deque

    check = deque()
    finish = []

    m, n = len(board), len(board[0])

    check_board = [[" "] * n for k in range(m)]  # 최소 거리를 담는 보드

    for x in range(len(board)):  # 출발 및 목적지 위치 확인
        for y in range(len(board[0])):
            if board[x][y] == "R":
                check.append([x, y, 0])
            if board[x][y] == "G":
                finish.append([x, y])

        if check and finish:
            break

    f_x, f_y = finish[0][0], finish[0][1]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while check:
        a, b, c = check.popleft()

        for v, w in zip(dx, dy):
            new_a = a
            new_b = b
            while True:
                if 0 <= new_a + v < len(board) and 0 <= new_b + w < len(board[0]) and board[new_a + v][
                    new_b + w] != "D":
                    new_a += v
                    new_b += w

                else:
                    if check_board[new_a][new_b] == " ":
                        check.append([new_a, new_b, c + 1])
                        check_board[new_a][new_b] = c + 1
                        break
                    else:
                        if check_board[new_a][new_b] > c + 1:
                            check.append([new_a, new_b, c + 1])
                            check_board[new_a][new_b] = c + 1
                        break

    return -1 if check_board[f_x][f_y] == " " else check_board[f_x][f_y]

# 다른 사람 풀이
def solution(board):
    
    que = []
    for x, row in enumerate(board):
        for y, each in enumerate(row):
            if board[x][y] == 'R':
                que.append((x, y, 0))
    visited = set()
    while que:
        x, y, length = que.pop(0)
        if (x, y) in visited:
            continue
        if board[x][y] == 'G':
            return length
        visited.add((x, y))
        for diff_x, diff_y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            now_x, now_y = x, y
            while True:
                next_x, next_y = now_x + diff_x, now_y + diff_y
                if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]) and board[next_x][next_y] != 'D':
                    now_x, now_y = next_x, next_y
                    continue
                que.append((now_x, now_y, length + 1))
                break
    return -1
