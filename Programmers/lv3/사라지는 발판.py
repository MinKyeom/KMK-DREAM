"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/92345
"""
# 내 풀이

# 조건
# 발판 있는 곳 없는 곳 존재
# 밟던 발판 다른 곳으로 이동시 사라짐
# 양 플레이어 상하좌우로 움직임

# 움직일 발판이 없는 경우 or 밖으로 넘어가는거 포함 패배
# 같은 발판에 존재 가능
# 같은 발판에 있다 둘중 한 플레이어가 이동하여 해당 발판이 사라지면 다른 플레이어 패배
# 시작: 플레이어 a 시작
# 항상 이길 수 있는 플레이어 패배하는 플레이어가 정해져 있음
# 항상 이기는 플레이어는 실수하지 않고 항상 지는 플레이어는 최대한 버티는 방향으로 했을 때 최적값 구하기

# 목표: 양플레이어가 최적으로 움직였을 때 횟수의 합
# 생각 방향: 보드 게임 bfs or dfs 접근
# 각 플레이어가 최적으로 움직이는 부분을 구현 핵심 누가 항상 이기는 플레이어인지 확인하기
# 최적이란? 이기는 플레이는 이길 수 있는 방향으로 지는 플레이어는 무조건 버티도록 하는 방향성 고민
# 항상 이기는 플레이어의 조건
# min,max 알고리즘 및 dfs 활용

# board: 보드 상태 aloc:a의 위치 bloc:b의 위치

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

game = []  # 게임판 진행 상황


def start(ax, ay, bx, by, board, m, n):
    global game

    if game[ax][ay] == 1:
        return 0

    count = 0

    for x, y in zip(dx, dy):
        new_x = ax + x
        new_y = ay + y

        # 범위 밖 또는 해당판 존재x
        if not 0 <= new_x < m or not 0 <= new_y < n or board[new_x][new_y] == 0 or game[new_x][new_y] == 1:
            continue

        # 해당 말 움직였으므로 해당판 존재사라짐
        game[ax][ay] = 1

        # dfs 구현

        # a의 말이 움직인 후에 같은 방식으로 b의 말이 움직임
        enemy = start(bx, by, new_x, new_y, board, m, n) + 1

        # 그 다음 for문을 위해 원복
        game[ax][ay] = 0

        if count % 2 == 0 and enemy % 2 == 1:
            count = enemy

        elif count % 2 == 0 and enemy % 2 == 0:
            count = max(count, enemy)

        elif count % 2 == 1 and enemy % 2 == 1:
            count = min(count, enemy)

    return count


def solution(board, aloc, bloc):
    global game

    m = len(board)  # 열
    n = len(board[0])  # 행

    ax, ay = aloc[0], aloc[1]

    bx, by = bloc[0], bloc[1]

    # 게임판 진행 상황 체크
    game = [[0] * n for _ in range(m)]

    result = start(ax, ay, bx, by, board, m, n)

    return result


# 내 풀이(개선 중)
# 조건
# 발판 있는 곳 없는 곳 존재
# 밟던 발판 다른 곳으로 이동시 사라짐
# 양 플레이어 상하좌우로 움직임

# 움직일 발판이 없는 경우 or 밖으로 넘어가는거 포함 패배
# 같은 발판에 존재 가능
# 같은 발판에 있다 둘중 한 플레이어가 이동하여 해당 발판이 사라지면 다른 플레이어 패배
# 시작: 플레이어 a 시작
# 항상 이길 수 있는 플레이어 패배하는 플레이어가 정해져 있음
# 항상 이기는 플레이어는 실수하지 않고 항상 지는 플레이어는 최대한 버티는 방향으로 했을 때 최적값 구하기

# 목표: 양플레이어가 최적으로 움직였을 때 횟수의 합
# 생각 방향: 보드 게임 bfs or dfs 접근
# 각 플레이어가 최적으로 움직이는 부분을 구현 핵심 누가 항상 이기는 플레이어인지 확인하기
# 최적이란? 이기는 플레이는 이길 수 있는 방향으로 지는 플레이어는 무조건 버티도록 하는 방향성 고민
# 항상 이기는 플레이어의 조건

# board: 보드 상태 aloc:a의 위치 bloc:b의 위치

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

game = []  # 게임판 진행 상황


def start(ax, ay, bx, by, board, m, n):
    global game

    count = 0

    for x, y in zip(dx, dy):
        new_x = ax + x
        new_y = ay + y

        # 범위 밖 또는 해당판 존재x
        if not 0 <= new_x < m or not 0 <= new_y < n or board[new_x][new_y] == 0 or game[new_x][new_y] == 1:
            continue

        # 해당 말 움직였으므로 해당판 존재사라짐
        game[ax][ay] = 1

        # dfs 구현
        # a의 말이 움직인 후에 같은 방식으로 b의 말이 움직임
        enemy = start(bx, by, new_x, new_y, board, m, n) + 1

        # 그 다음 for문을 위해 원복
        game[ax][ay] = 0

        if count % 2 == 0 and enemy % 2 == 1:
            count = enemy

        elif count % 2 == 0 and enemy % 2 == 0:
            count = max(count, enemy)

        elif count % 2 == 1 and enemy % 2 == 1:
            count = min(count, enemy)

    return count


def solution(board, aloc, bloc):
    global game

    m = len(board)  # 열
    n = len(board[0])  # 행

    ax, ay = aloc[0], aloc[1]

    bx, by = bloc[0], bloc[1]

    # 게임판 진행 상황 체크
    game = [[0] * n for _ in range(m)]

    result = start(ax, ay, bx, by, board, m, n)

    return result

# 내 풀이(개선 중)
# 조건
# 발판 있는 곳 없는 곳 존재
# 밟던 발판 다른 곳으로 이동시 사라짐
# 양 플레이어 상하좌우로 움직임

# 움직일 발판이 없는 경우 or 밖으로 넘어가는거 포함 패배
# 같은 발판에 존재 가능
# 같은 발판에 있다 둘중 한 플레이어가 이동하여 해당 발판이 사라지면 다른 플레이어 패배
# 시작: 플레이어 a 시작
# 항상 이길 수 있는 플레이어 패배하는 플레이어가 정해져 있음
# 항상 이기는 플레이어는 실수하지 않고 항상 지는 플레이어는 최대한 버티는 방향으로 했을 때 최적값 구하기

# 목표: 양플레이어가 최적으로 움직였을 때 횟수의 합
# 생각 방향: 보드 게임 bfs or dfs 접근
# 각 플레이어가 최적으로 움직이는 부분을 구현 핵심 누가 항상 이기는 플레이어인지 확인하기
# 최적이란? 이기는 플레이는 이길 수 있는 방향으로 지는 플레이어는 무조건 버티도록 하는 방향성 고민
# 항상 이기는 플레이어의 조건

# board: 보드 상태 aloc:a의 위치 bloc:b의 위치

import copy


def solution(board, aloc, bloc):
    m = len(board)  # 열
    n = len(board[0])  # 행

    ax, ay = aloc[0], aloc[1]

    bx, by = bloc[0], bloc[1]

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    result = 0

    check = []

    q = [(0, ax, ay, bx, by, board)]

    flag = False

    while q:

        count, a_x, a_y, b_x, b_y, b = q.pop()

        for i, j in zip(dx, dy):

            # a 시작 및 이동경로 보드 내인지 확인
            if 0 <= a_x + i < m and 0 <= a_y + j < n:

                # 발판 존재 확인
                if b[a_x + i][a_y + j] != 0:

                    # 발판 저장 및 새롭게 구성
                    c = copy.deepcopy(b)

                    # 기존 발판 사라짐
                    c[a_x][a_y] = 0

                    # b가 거기 서있을경우
                    if c[b_x][b_y] == 0:
                        result = max(result, count + 1)
                        check.append(["A", count + 1])
                        flag = True
                        continue

                    # b 시작 및 이동경로 보드 내인지 확인
                    for v, w in zip(dx, dy):
                        if 0 <= b_x + v < m and 0 <= b_y + w < n:

                            # 발판 존재 확인
                            if c[b_x + v][b_y + w] != 0:

                                # 기존 발판 저장
                                e = copy.deepcopy(c)

                                # 기존 발판 사라짐
                                e[b_x][b_y] = 0

                                # a가 거기 서있었을 경우
                                if e[a_x + i][a_y + j] == 0:
                                    result = max(result, count + 2)
                                    check.append(["B", count + 2])
                                    continue

                                q.append((count + 2, a_x + i, a_y + j, b_x + v, b_y + w, e))

                            else:
                                result = max(count + 1, result)
                                check.append(["A", count + 1])
                                flag = True
                        else:
                            result = max(count + 1, result)
                            check.append(["A", count + 1])
                            flag = True
                else:
                    result = max(count, result)
                    check.append(["B", count])

            else:
                result = max(count, result)
                check.append(["B", count])

    print(flag)
    return result

# 내 풀이(개선중)
# 조건
# 발판 있는 곳 없는 곳 존재
# 밟던 발판 다른 곳으로 이동시 사라짐
# 양 플레이어 상하좌우로 움직임

# 움직일 발판이 없는 경우 or 밖으로 넘어가는거 포함 패배
# 같은 발판에 존재 가능
# 같은 발판에 있다 둘중 한 플레이어가 이동하여 해당 발판이 사라지면 다른 플레이어 패배
# 시작: 플레이어 a 시작
# 항상 이길 수 있는 플레이어 패배하는 플레이어가 정해져 있음
# 항상 이기는 플레이어는 실수하지 않고 항상 지는 플레이어는 최대한 버티는 방향으로 했을 때 최적값 구하기

# 목표: 양플레이어가 최적으로 움직였을 때 횟수의 합
# 생각 방향: 보드 게임 bfs or dfs 접근
# 각 플레이어가 최적으로 움직이는 부분을 구현 핵심 누가 항상 이기는 플레이어인지 확인하기
# 최적이란? 이기는 플레이는 이길 수 있는 방향으로 지는 플레이어는 무조건 버티도록 하는 방향성 고민
# 항상 이기는 플레이어의 조건

# board: 보드 상태 aloc:a의 위치 bloc:b의 위치

import copy


def solution(board, aloc, bloc):
    m = len(board)  # 열
    n = len(board[0])  # 행

    ax, ay = aloc[0], aloc[1]

    bx, by = bloc[0], bloc[1]

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    result = 0

    check = []

    q = [(0, ax, ay, bx, by, board)]

    while q:

        count, a_x, a_y, b_x, b_y, b = q.pop()

        for i, j in zip(dx, dy):

            # a 시작 및 이동경로 보드 내인지 확인
            if 0 <= a_x + i < m and 0 <= a_y + j < n:

                # 발판 존재 확인
                if b[a_x + i][a_y + j] != 0:

                    # 발판 저장 및 새롭게 구성
                    c = copy.deepcopy(b)

                    # 기존 발판 사라짐
                    c[a_x][a_y] = 0

                    # b가 거기 서있을경우
                    if c[b_x][b_y] == 0:
                        result = max(result, count + 1)
                        check.append(["A", count + 1])
                        continue

                    # b 시작 및 이동경로 보드 내인지 확인
                    for v, w in zip(dx, dy):
                        if 0 <= b_x + v < m and 0 <= b_y + w < n:

                            # 발판 존재 확인
                            if c[b_x + v][b_y + w] != 0:

                                # 기존 발판 저장
                                e = copy.deepcopy(c)

                                # 기존 발판 사라짐
                                e[b_x][b_y] = 0

                                # a가 거기 서있었을 경우
                                if e[a_x + i][a_y + j] == 0:
                                    result = max(result, count + 2)
                                    check.append(["B", count + 2])
                                    continue

                                q.append((count + 2, a_x + i, a_y + j, b_x + v, b_y + w, e))

                            else:
                                result = max(count + 1, result)
                                check.append(["A", count + 1])
                        else:
                            result = max(count + 1, result)
                            check.append(["A", count + 1])

                else:
                    result = max(count, result)
                    check.append(["B", count])

            else:
                result = max(count, result)
                check.append(["B", count])

    print(check)

    return result

# 내 풀이(개선 중)
# 조건
# 발판 있는 곳 없는 곳 존재
# 밟던 발판 다른 곳으로 이동시 사라짐
# 양 플레이어 상하좌우로 움직임

# 움직일 발판이 없는 경우 or 밖으로 넘어가는거 포함 패배
# 같은 발판에 존재 가능
# 같은 발판에 있다 둘중 한 플레이어가 이동하여 해당 발판이 사라지면 다른 플레이어 패배
# 시작: 플레이어 a 시작
# 항상 이길 수 있는 플레이어 패배하는 플레이어가 정해져 있음
# 항상 이기는 플레이어는 실수하지 않고 항상 지는 플레이어는 최대한 버티는 방향으로 했을 때 최적값 구하기

# 목표: 양플레이어가 최적으로 움직였을 때 횟수의 합
# 생각 방향: 보드 게임 bfs or dfs 접근
# 각 플레이어가 최적으로 움직이는 부분을 구현 핵심 누가 항상 이기는 플레이어인지 확인하기
# 최적이란? 이기는 플레이는 이길 수 있는 방향으로 지는 플레이어는 무조건 버티도록

# board: 보드 상태 aloc:a의 위치 bloc:b의 위치

import copy


def solution(board, aloc, bloc):
    m = len(board)  # 열
    n = len(board[0])  # 행

    ax, ay = aloc[0], aloc[1]

    bx, by = bloc[0], bloc[1]

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    result = 0

    a_win = 0
    b_win = 0

    q = [(0, ax, ay, bx, by, board)]

    while q:

        count, a_x, a_y, b_x, b_y, b = q.pop()

        for i, j in zip(dx, dy):

            # a 시작 및 이동경로 보드 내인지 확인
            if 0 <= a_x + i < m and 0 <= a_y + j < n:

                # 발판 존재 확인
                if b[a_x + i][a_y + j] != 0:

                    # 발판 저장 및 새롭게 구성
                    c = copy.deepcopy(b)

                    # 기존 발판 사라짐
                    c[a_x][a_y] = 0

                    # b가 거기 서있을경우
                    if c[b_x][b_y] == 0:
                        result = max(result, count + 1)
                        a_win += 1
                        continue

                    # b 시작 및 이동경로 보드 내인지 확인
                    for v, w in zip(dx, dy):
                        if 0 <= b_x + v < m and 0 <= b_y + w < n:

                            # 발판 존재 확인
                            if c[b_x + v][b_y + w] != 0:

                                # 기존 발판 저장
                                e = copy.deepcopy(c)

                                # 기존 발판 사라짐
                                e[b_x][b_y] = 0

                                # a가 거기 서있었을 경우
                                if e[a_x + i][a_y + j] == 0:
                                    result = max(result, count + 2)
                                    b_win += 1
                                    continue

                                q.append((count + 2, a_x + i, a_y + j, b_x + v, b_y + w, e))

                            else:
                                result = max(count + 1, result)
                                a_win += 1
                        else:
                            result = max(count + 1, result)
                            a_win += 1

                else:
                    result = max(count, result)
                    b_win += 1


            else:
                result = max(count, result)
                b_win += 1

    print(a_win, b_win)
    return result

# 다른 사람 풀이
n,m = 0,0
move = [(0,1),(0,-1),(1,0),(-1,0)]
visit = [[0]*5 for _ in range(5)]
def OOB(x,y):
    return x < 0 or x >= n or y < 0 or y >= m

# 결과값이
def play(board,curx,cury,opx,opy):
    global visit
    if visit[curx][cury]: return 0
    canWin = 0
    for mov in move:
        dx, dy = mov
        nx, ny = curx + dx, cury + dy
        if OOB(nx,ny) or visit[nx][ny] or board[nx][ny] == 0 : continue
        # 방문처리
        visit[curx][cury] = 1
        opResult = play(board,opx,opy,nx,ny)+1
        # 방문처리 끝
        visit[curx][cury] = 0

        # 현재 저장된 값 패배인데 상대가 졌다고 하면 이기는 경우로 저장
        if canWin % 2 == 0 and opResult % 2 == 1 : canWin = opResult
        # 현재 저장된 값 패배인데 상대가 이겼다고 하면 최대한 늦게 지는 횟수 선택
        elif canWin % 2 == 0 and opResult % 2 == 0 : canWin = max(canWin,opResult)
        # 현재 저장된 값 승리인데 상대가 졌다고 하면 최대한 빨리 이기는 횟수 선택
        elif canWin % 2 == 1 and opResult % 2 == 1 : canWin = min(canWin,opResult)
    return canWin

def solution(board, aloc, bloc):
    global n,m
    n, m = len(board), len(board[0])
    return play(board,aloc[0],aloc[1],bloc[0],bloc[1])

# 다른 사람 풀이
def solution(board, aloc, bloc):
    answer = 0

    deltas = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def neighbor(loc, board):
        for dx, dy in deltas:
            n = (loc[0]+dx, loc[1]+dy)
            if n in board:
                yield (*n, loc[2])

    def dfs(aloc, bloc, board, depth):
        neighbors = list(neighbor(aloc, board))

        if not neighbors or aloc[:2] not in board:
            return 0, depth

        res = list(dfs(bloc, n, board - {aloc[:2]}, depth + 1) for n in neighbors)
        wins = [r[1] for r in res if r[0] == 0]
        loses = [r[1] for r in res if r[0] == 1]

        if wins:
            return 1, min(wins)
        else:
            return 0, max(loses)


    board = {(r, c) for r, row in enumerate(board) for c, val in enumerate(row) if val}
    answer = dfs(tuple(aloc + [0]), tuple(bloc + [1]), board, 0)[1]

    return answer