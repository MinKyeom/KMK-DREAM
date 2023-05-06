# 내 풀이
def solution(board):
    result = []
    dx = [1, 0, -1, -1, -1, 0, 1, 1]
    dy = [1, 1, 1, 0, -1, -1, -1, 0]
    for a in range(len(board)):
        for b in range(len(board)):
            if board[a][b] == 1:
                for c, d in zip(dx, dy):
                    if 0 <= a + c < len(board) and 0 <= b + d < len(board):
                        if board[a + c][b + d] == 0: #### 이 줄
                            board[a + c][b + d] = 3
                            continue

    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 0:
                result.append(0)

    answer = len(result)

    return answer
# 내 풀이

def solution(board):
    result = []
    dx = [1, 0, -1, -1, -1, 0, 1, 1]
    dy = [1, 1, 1, 0, -1, -1, -1, 0]
    for a in range(len(board)):
        for b in range(len(board)):
            if board[a][b] == 1:
                for c, d in zip(dx, dy):
                    if 0 <= a + c <= len(board) - 1 and 0 <= b + d <= len(board) - 1:  #### 이 줄
                        if board[a + c][b + d] == 0:
                            board[a + c][b + d] = 3
                            continue

    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 0:
                result.append(0)

    answer = len(result)

    return answer

# 다른 사람 풀이

def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)