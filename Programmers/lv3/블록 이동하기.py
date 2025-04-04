"""
프로그래머스
출처:https://school.programmers.co.kr/learn/courses/30/lessons/60063
"""

# 풀이 과정
"""
bfs 
"""
from collections import deque


def arround(x, y, check_x, check_y):
    check = [[(x + 1, y), (x - 1, y)], [(x, y + 1), (x, y - 1)]]

    for i in check:
        if (check_x, check_y) in i:
            continue
        else:
            d = i

    k = []

    for nx, ny in d:
        if nx != x:
            k.append((nx, ny, nx, check_y))
        elif ny != y:
            k.append((nx, ny, check_x, ny))

    return k


def solution(board):
    m = len(board)
    n = len(board[0])
    # 이동
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 회전8,이동4

    robot = ((0, 0), (0, 1))

    q = deque([((0, 0), (0, 1), 0)])

    visit = set([])

    result = float("inf")

    while q:
        z = q.popleft()

        if (m - 1, n - 1) in z:
            result = min(result, z[2])
            continue

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
                    # visit.add(((nx+x1,ny+x2),(nx+y1,ny+y2)))
                    # visit.add(((nx+y1,ny+y2),(nx+x1,ny+x2)))

        check = arround(x1, x2, y1, y2)

        for nx, ny, mx, my in check:
            if 0 <= nx < m and 0 <= ny < n:
                if board[nx][ny] == 0 and board[mx][my] == 0 and not ((nx, ny), (x1, x2)) in visit and not ((nx, ny), (
                x1, x2)) in visit:
                    q.append(((x1, x2), (nx, ny), count + 1))
                    # visit.add(((x1,x2),(nx,ny)))
                    # visit.add(((nx,ny),(x1,x2)))

        check = arround(y1, y2, x1, x2)

        for nx, ny, mx, my in check:
            if 0 <= nx < m and 0 <= ny < n:
                if board[nx][ny] == 0 and board[mx][my] == 0 and not ((nx, ny), (y1, y2)) in visit and not ((nx, ny), (
                y1, y2)) in visit:
                    q.append(((y1, y2), (nx, ny), count + 1))
                    # visit.add(((y1,y2),(nx,ny)))
                    # visit.add(((nx,ny),(y1,y2)))
    return result

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

    result = float("inf")
    while q:
        z = q.popleft()

        if (m - 1, n - 1) in z:
            result = min(result, z[2])
            continue

        x1, x2 = z[0][0], z[0][1]
        y1, y2 = z[1][0], z[1][1]
        count = z[2]

        #         if not ((z[0]),(z[1])) in visit or not ((z[1]),(z[0])) in visit:
        #             visit.add(((z[0]),(z[1])))
        #             visit.add(((z[1]),(z[0])))

        #         else:
        #             continue

        # 이동
        for nx, ny in zip(dx, dy):
            if 0 <= nx + x1 < m and 0 <= ny + x2 < n and 0 <= nx + y1 < m and 0 <= ny + y2 < n:
                if board[nx + x1][ny + x2] == 0 and board[nx + y1][ny + y2] == 0 and not ((nx + x1, ny + x2), (
                nx + y1, ny + y2)) in visit and not ((nx + y1, ny + y2), (nx + x1, ny + x2)) in visit:
                    q.append(((nx + x1, ny + x2), (nx + y1, ny + y2), count + 1))
                    visit.add(((nx + x1, ny + x2), (nx + y1, ny + y2)))
                    visit.add(((nx + y1, ny + y2), (nx + x1, ny + x2)))
        # 회전
        for nx, ny in zip(dx, dy):
            if 0 <= nx + x1 < m and 0 <= ny + x2 < n and 0 <= nx + y1 < m and 0 <= ny + y2 < n:
                if board[nx + x1][ny + x2] == 0 and board[nx + y1][ny + y2] == 0 and not ((nx + x1, ny + x2),
                                                                                          (y1, y2)) in visit and not ((
                                                                                                                      y1,
                                                                                                                      y2),
                                                                                                                      (
                                                                                                                      nx + x1,
                                                                                                                      ny + x2)) in visit:
                    q.append(((nx + x1, ny + x2), (y1, y2), count + 1))
                    visit.add(((nx + x1, ny + x2), (y1, y2)))
                    visit.add(((y1, y2), (nx + x1, ny + x2)))

                if board[nx + x1][ny + x2] == 0 and board[nx + y1][ny + y2] == 0 and not ((x1, x2), (
                nx + y1, ny + y2)) in visit and not ((nx + y1, ny + y2), (x1, x2)) in visit:
                    q.append(((x1, x2), (nx + y1, ny + y2), count + 1))
                    visit.add(((x1, x2), (nx + y1, ny + y2)))
                    visit.add(((nx + y1, ny + y2), (x1, x2)))

    return result

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

# 다른 사람 풀이
from collections import deque

def solution(board):
    SIZE = len(board)
    ROW_WISE, COLUMN_WISE = range(2)
    OPEN, WALL = range(2)
    START = (0, 0, ROW_WISE)
    END_POINT = (SIZE-1, SIZE-1)
    DELTAS = ((0, 1), (1, 0), (0, -1), (-1, 0))

    queue = deque([START])
    visited = set()
    visited.add(START)
    moves_count = 0

    def _is_in_range(r, c):
        return 0 <= r < SIZE and 0 <= c < SIZE

    def _is_open(r, c):
        return board[r][c] == OPEN

    def _is_ok(r, c):
        return _is_in_range(r, c) and _is_open(r, c)

    def _yield_moves_rowwise(r, c):
        for dr, dc in DELTAS:
            new_r, new_c = r + dr, c + dc
            if _is_ok(new_r, new_c) and _is_ok(new_r, new_c+1):
                yield (new_r, new_c, ROW_WISE)

        if _is_ok(r+1, c) and _is_ok(r+1, c+1):
            yield (r, c, COLUMN_WISE)
            yield (r, c+1, COLUMN_WISE)
        if _is_ok(r-1, c) and _is_ok(r-1, c+1):
            yield (r-1, c, COLUMN_WISE)
            yield (r-1, c+1, COLUMN_WISE)

    def _yield_moves_columnwise(r, c):
        for dr, dc in DELTAS:
            new_r, new_c = r + dr, c + dc
            if _is_ok(new_r, new_c) and _is_ok(new_r+1, new_c):
                yield (new_r, new_c, COLUMN_WISE)

        if _is_ok(r, c-1) and _is_ok(r+1, c-1):
            yield (r, c-1, ROW_WISE)
            yield (r+1, c-1, ROW_WISE)
        if _is_ok(r, c+1) and _is_ok(r+1, c+1):
            yield (r, c, ROW_WISE)
            yield (r+1, c, ROW_WISE)

    while queue:
        moves_count += 1

        for _ in range(len(queue)):
            r, c, direction = queue.popleft()

            if direction == ROW_WISE:
                yield_func = _yield_moves_rowwise
            else:
                yield_func = _yield_moves_columnwise

            for new_coord in yield_func(r, c):
                if new_coord not in visited:
                    queue.append(new_coord)
                    visited.add(new_coord)

                    r, c, direction = new_coord
                    if (r, c+1) == END_POINT or (r+1, c) == END_POINT:
                        return moves_count
# 다른 사람 풀이
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

MAX = float('inf')


def solution(board):
    N = len(board)
    answer = 0
    visited = set()
    q = deque([(0, 0, 0, 0)])

    while q:
        x, y, r, t = q.popleft()
        if (x, y) == (N - 1, N - 1) or (x + dx[r], y + dy[r]) == (N - 1, N - 1):
            answer = t
            break
        if (x, y, r) in visited or (x + dx[r], y + dy[r], (r + 2) % 4) in visited:
            continue
        visited.add((x, y, r))

        for i in range(4):
            ax, ay = x + dx[i], y + dy[i]
            if not -1 < ax < N or not -1 < ay < N or board[ay][ax] == 1:
                continue
            _ax, _ay = ax + dx[r], ay + dy[r]
            if not -1 < _ax < N or not -1 < _ay < N or board[_ay][_ax] == 1:
                continue
            q.append((ax, ay, r, t + 1))

        for i in [-1, 1]:
            _r = (r + i) % 4
            ax, ay = x + dx[_r], y + dy[_r]
            if not -1 < ax < N or not -1 < ay < N or board[ay][ax] == 1:
                continue
            cx, cy = ax + dx[r], ay + dy[r]
            if board[cy][cx] == 1:
                continue
            q.append((x, y, _r, t + 1))

        x, y, r = x + dx[r], y + dy[r], (r + 2) % 4
        for i in [-1, 1]:
            _r = (r + i) % 4
            ax, ay = x + dx[_r], y + dy[_r]
            if not -1 < ax < N or not -1 < ay < N or board[ay][ax] == 1:
                continue
            cx, cy = ax + dx[r], ay + dy[r]
            if board[cy][cx] == 1:
                continue
            q.append((x, y, _r, t + 1))

    return answer

# 다른 사람 풀이

def solution(board):
    N = len(board)
    mem = [[[100000 for _ in range(2)] for _ in range(N)] for _ in range(N)]
    st = [[0,0,0]]
    mem[0][0][0] = 0

    for s in st:
        if(s[2] == 0):
            if(s[0]+1 < N and board[s[0]+1][s[1]] == 0 and board[s[0]+1][s[1]+1] == 0):
                if(mem[s[0]+1][s[1]][s[2]] > mem[s[0]][s[1]][s[2]] + 1):
                    mem[s[0]+1][s[1]][s[2]] = mem[s[0]][s[1]][s[2]] + 1
                    st.append([s[0]+1,s[1],s[2]])
                if(mem[s[0]][s[1]][1] > mem[s[0]][s[1]][s[2]] + 1):
                    mem[s[0]][s[1]][1] = mem[s[0]][s[1]][s[2]] + 1
                    st.append([s[0],s[1],1])
                if(mem[s[0]][s[1]+1][1] > mem[s[0]][s[1]][s[2]] + 1):
                    mem[s[0]][s[1]+1][1] = mem[s[0]][s[1]][s[2]] + 1
                    st.append([s[0],s[1]+1,1])
            if(s[0] > 0 and board[s[0]-1][s[1]] == 0 and board[s[0]-1][s[1]+1] == 0):
                if(mem[s[0]-1][s[1]][s[2]] > mem[s[0]][s[1]][s[2]] + 1):
                    mem[s[0]-1][s[1]][s[2]] = mem[s[0]][s[1]][s[2]] + 1
                    st.append([s[0]-1,s[1],s[2]])
                if(mem[s[0]-1][s[1]][1] > mem[s[0]][s[1]][s[2]] + 1):
                    mem[s[0]-1][s[1]][1] = mem[s[0]][s[1]][s[2]] + 1
                    st.append([s[0]-1,s[1],1])
                if(mem[s[0]-1][s[1]+1][1] > mem[s[0]][s[1]][s[2]] + 1):
                    mem[s[0]-1][s[1]+1][1] = mem[s[0]][s[1]][s[2]] + 1
                    st.append([s[0]-1,s[1]+1,1])
            if(s[1]+2 < N and board[s[0]][s[1]+2] == 0):
                if(mem[s[0]][s[1]+1][s[2]] > mem[s[0]][s[1]][s[2]] + 1):
                    mem[s[0]][s[1]+1][s[2]] = mem[s[0]][s[1]][s[2]] + 1
                    st.append([s[0],s[1]+1,s[2]])
            if(s[1] > 0 and board[s[0]][s[1]-1] == 0):
                if(mem[s[0]][s[1]-1][s[2]] > mem[s[0]][s[1]][s[2]] + 1):
                    mem[s[0]][s[1]-1][s[2]] = mem[s[0]][s[1]][s[2]] + 1
                    st.append([s[0],s[1]-1,s[2]])

        else:
            if(s[1]+1 < N and board[s[0]][s[1]+1] == 0 and board[s[0]+1][s[1]+1] == 0):
                if(mem[s[0]][s[1]+1][s[2]] > mem[s[0]][s[1]][s[2]] + 1):
                    mem[s[0]][s[1]+1][s[2]] = mem[s[0]][s[1]][s[2]] + 1
                    st.append([s[0],s[1]+1,s[2]])
                if(mem[s[0]][s[1]][0] > mem[s[0]][s[1]][s[2]] + 1):
                    mem[s[0]][s[1]][0] = mem[s[0]][s[1]][s[2]] + 1
                    st.append([s[0],s[1],0])
                if(mem[s[0]+1][s[1]][0] > mem[s[0]][s[1]][s[2]] + 1):
                    mem[s[0]+1][s[1]][0] = mem[s[0]][s[1]][s[2]] + 1
                    st.append([s[0]+1,s[1],0])
            if(s[1] > 0 and board[s[0]][s[1]-1] == 0 and board[s[0]+1][s[1]-1] == 0):
                if(mem[s[0]][s[1]-1][s[2]] > mem[s[0]][s[1]][s[2]] + 1):
                    mem[s[0]][s[1]-1][s[2]] = mem[s[0]][s[1]][s[2]] + 1
                    st.append([s[0],s[1]-1,s[2]])
                if(mem[s[0]][s[1]-1][0] > mem[s[0]][s[1]][s[2]] + 1):
                    mem[s[0]][s[1]-1][0] = mem[s[0]][s[1]][s[2]] + 1
                    st.append([s[0],s[1]-1,0])
                if(mem[s[0]+1][s[1]-1][0] > mem[s[0]][s[1]][s[2]] + 1):
                    mem[s[0]+1][s[1]-1][0] = mem[s[0]][s[1]][s[2]] + 1
                    st.append([s[0]+1,s[1]-1,0])
            if(s[0]+2 < N and board[s[0]+2][s[1]] == 0):
                if(mem[s[0]+1][s[1]][s[2]] > mem[s[0]][s[1]][s[2]] + 1):
                    mem[s[0]+1][s[1]][s[2]] = mem[s[0]][s[1]][s[2]] + 1
                    st.append([s[0]+1,s[1],s[2]])
            if(s[0] > 0 and board[s[0]-1][s[1]] == 0):
                if(mem[s[0]-1][s[1]][s[2]] > mem[s[0]][s[1]][s[2]] + 1):
                    mem[s[0]-1][s[1]][s[2]] = mem[s[0]][s[1]][s[2]] + 1
                    st.append([s[0]-1,s[1],s[2]])


    re1 = mem[N-1][N-2][0]
    re2 = mem[N-2][N-1][1]
    if(re1>re2): return re2
    else: return re1
