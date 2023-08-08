# 내 풀이
def solution(maps):
    from collections import deque
    m = len(maps)
    n = len(maps[0])

    board = [[" "] * n for k in range(m)]

    check = []

    for a in range(m):
        for b in range(n):
            if not maps[a][b] == "X":
                check.append([a, b])
    check = deque(check)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    finish = []

    if len(check) == 0:
        return [-1]


    else:
        while check:
            y = check[0][0]
            z = check[0][1]
            if board[y][z] == "check":
                check.popleft()
                continue

            start = deque([[check[0][0], check[0][1]]])
            visited = []
            while start:
                a, b = start.popleft()
                if board[a][b] == " ":
                    board[a][b] = "check"
                    visited.append([a, b])
                    for v, w in zip(dx, dy):
                        new_a = a + v
                        new_b = b + w
                        if 0 <= new_a < m and 0 <= new_b < n and not maps[new_a][new_b] == "X":
                            start.append([new_a, new_b])
                        elif 0 <= new_a < m and 0 <= new_b < n and maps[new_a][new_b] == "X":
                            board[new_a][new_b] = "check"


                else:
                    continue

            finish.append(visited)

    result = []

    for a in range(len(finish)):
        count = 0
        for b in range(len(finish[a])):
            c, d = finish[a][b]
            count += int(maps[c][d])
        result.append(count)

    result.sort()

    return result


# 다른 사람 풀이
from collections import deque
def solution(maps):
    N, M = len(maps), len(maps[0])
    visited = [[0]*M for _ in range(N)]

    answer = []
    for i in range(N):
        for j in range(M):
            if maps[i][j]=='X' or visited[i][j]:
                continue
            queue = deque()
            queue.append((i,j))
            visited[i][j]=1
            n_food = int(maps[i][j])
            while queue:
                i0, j0 = queue.popleft()
                for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                    ni, nj = i0+di, j0+dj
                    if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and maps[ni][nj]!='X':
                        queue.append((ni,nj))
                        visited[ni][nj] = 1
                        n_food += int(maps[ni][nj])
            answer.append(n_food)
    if not answer:
        answer.append(-1)
    else:
        answer.sort()
    return answer