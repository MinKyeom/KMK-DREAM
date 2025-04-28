"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/84021
"""
# 풀이 과정
"""
조건:
1회에 1번
조각 회전가능
뒤집기 불가능 

목표:
채울 수 있는 최대칸을 구하여라 

생각방향:모양이 들어맞아야 인접한 곳이 비는 일이 없어짐에 따라 빈 곳과 테이블을 비교해야한다

회전하는 방법에 대한 아이디어 생각 > 회전변환

닮음의 원칙 응용 생각 고민

# 양쪽 맵의 도형 좌표들을 모두 모은 후 리스트로 모은 후 두 맵 중 하나의 좌표를 하나씩 팝 한 후 
회전변환 후 도형 중 가장 작은 점을 찾은 후 평행 이동 시켰을 때 같은 도형이라면 집합상 동일하다는 점을 체크 후 구하기 
"""

v = []

# 보드 도형
board = []

# 테이블 도형
check = []

from collections import deque
import copy


def find(i, j, g, s):
    global v_baord, v_table, board, check

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    new = []

    q = deque([[i, j]])

    while q:
        a, b = q.popleft()
        v[a][b] = True
        new.append([a, b])

        for k, t in zip(dx, dy):
            if 0 <= a + k < len(g) and 0 <= b + t < len(g[0]):
                if v[a + k][b + t] == False and s == "board":
                    if g[a + k][b + t] == 0:
                        q.append([a + k, b + t])
                        v[a + k][b + t] = True
                elif v[a + k][b + t] == False and s == "table":
                    if g[a + k][b + t] == 1:
                        q.append([a + k, b + t])
                        v[a + k][b + t] = True
                        # print(a+k,b+t)

    # print(new,"new",s)

    x = copy.deepcopy(new)

    # if s=="board":
    #     check.append(x)
    # else:
    #     board.append(x)

    return x


def solution(game_board, table):
    global check, board, v

    g = game_board
    t = table

    # 행 길이
    m = len(table)

    # 열 길이
    n = len(table[0])

    # 방문 기록
    v = [[False] * n for _ in range(m)]

    s = "board"

    # 보드의 빈공간 도형 찾기
    for i in range(m):
        for j in range(n):
            if g[i][j] == 0 and v[i][j] == False:
                plus = find(i, j, g, s)
                board.append(plus)

    # 보드 내 도형을 구한 후 초기화
    v = [[False] * n for _ in range(m)]

    s = "table"

    # 테이블의 도형 찾기
    for i in range(m):
        for j in range(n):
            if t[i][j] == 1 and v[i][j] == False:
                # print(i,j,"table 도형 찾기 시작점")
                plus = find(i, j, t, s)
                # print(check,"find 후 check")
                check.append(plus)

    # 테이블의 도형을 하나씩 뽑아낸 후 모든 좌표를 90도 회전변환 후 닮음 여부 체크
    result = 0  # 채워질때마다 추가

    # board=deque(board)

    # check:테이블 도형 board: 보드 도형

    board = deque(board)

    count = len(board)

    # print(check,"table 도형",board,"보드 도형")

    while count > 0:
        o = board.popleft()
        o.sort()
        board.append(o)
        count -= 1

    while check:
        k = check.pop()
        new = []
        k.sort()
        new.append(k)
        one = []  # 90도
        two = []  # 180도
        three = []  # 270도

        for x, y in k:
            one.append([-y, x])
            two.append([-x, -y])
            three.append([y, -x])

        one.sort()
        two.sort()
        three.sort()
        new.append(one)
        new.append(two)
        new.append(three)

        new_board = []

        while board:
            figure = board.popleft()

            # 꼭짓점의 개수 체크
            if len(new[0]) == len(figure):
                flag = False
                # 0도~270도
                for i in range(4):
                    num1, num2 = (new[i][0][0] - figure[0][0]), (new[i][0][1] - figure[0][1])

                    for j in range(len(figure)):
                        if (new[i][j][0] - figure[j][0]) != num1 or (new[i][j][1] - figure[j][1]) != num2:
                            break
                    else:
                        # 같은 도형
                        flag = True
                        # print(new[0],i,"figure",figure,num1,num2)
                        result += len(new[0])
                        break
            else:
                new_board.append(figure)
                continue

            if flag == False:
                new_board.append(figure)

            elif flag == True:
                break

        board += new_board

    return result

# 내 풀이(개선 중)
"""
조건:
1회에 1번
조각 회전가능
뒤집기 불가능 

목표:
채울 수 있는 최대칸을 구하여라 

생각방향:모양이 들어맞아야 인접한 곳이 비는 일이 없어짐에 따라 빈 곳과 테이블을 비교해야한다

회전하는 방법에 대한 아이디어 생각 > 회전변환

닮음의 원칙 응용 생각 고민

# 양쪽 맵의 도형 좌표들을 모두 모은 후 리스트로 모은 후 두 맵 중 하나의 좌표를 하나씩 팝 한 후 
회전변환 후 도형 중 가장 작은 점을 찾은 후 평행 이동 시켰을 때 같은 도형이라면 집합상 동일하다는 점을 체크 후 구하기 
"""

v = []

# 보드 도형
board = []

# 테이블 도형
check = []

from collections import deque
import copy


def find(i, j, g, s):
    global v_baord, v_table, board, check

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    new = []

    q = deque([(i, j)])

    while q:
        a, b = q.popleft()
        v[a][b] = True
        new.append((a, b))

        for k, t in zip(dx, dy):
            if 0 <= a + k < len(g) and 0 <= b + t < len(g[0]):
                if v[a + k][b + t] == False and g[a + k][b + t] == 1:
                    q.append((a + k, b + t))

    new = tuple(new)
    x = copy.deepcopy(new)

    if s == "board":
        check.append((x))
    else:
        board.append((x))

    return 0


def solution(game_board, table):
    global check, board, v

    g = game_board
    t = table

    # 열 길이
    m = len(table)

    # 행 길이
    n = len(table[0])

    # 방문 기록
    v = [[False] * n for _ in range(m)]

    s = "board"

    # 보드의 도형 찾기
    for i in range(m):
        for j in range(n):
            if g[i][j] == 1 and v[i][j] == False:
                find(i, j, g, s)

    # 보드 내 도형을 구한 후 초기화
    v = [[False] * n for _ in range(m)]

    s = "table"

    # 테이블의 도형 찾기
    for i in range(m):
        for j in range(n):
            if t[i][j] == 1 and v[i][j] == False:
                find(i, j, t, s)

    # 테이블의 도형을 하나씩 뽑아낸 후 모든 좌표를 90도 회전변환 후 닮음 여부 체크
    result = 0  # 채워질때마다 추가

    # board=deque(board)

    # check:테이블 도형 board: 보드 도형
    while check:
        k = check.pop()
        k.sort()

        count = len(board)

        # 합동인 도형이 있는 경우
        flag = False

        while count > 0:
            x = board.popleft()
            x.sort()

            # 도형의 꼭짓점 개수가 같을 때
            if len(k) == len(x):
                # 평행이동 수치
                y = k[0][0] - x[0][0]
                z = k[0][1] - x[0][1]

                change = 3  # 회전 변환
                while change > 0:
                    new = []
                    # 기본 상태 비율로 줄이기
                    for one, two in k:
                        one -= y
                        two -= z
                        new.append((one, two))

                    new = tuple(new)
                    if set(new) == set(x):
                        break

                    else:
                        change -= 1
                        for num in range(len(k)):
                            k[num][0], k[num][1] = -k[num][1], k[num][0]

            else:
                board.append(x)

            count -= 1

    return result

# 내 풀이 (개선 중)
"""
조건:
1회에 1번
조각 회전가능
뒤집기 불가능 

목표:
채울 수 있는 최대칸을 구하여라 

생각방향:모양이 들어맞아야 인접한 곳이 비는 일이 없어짐에 따라 빈 곳과 테이블을 비교해야한다

회전하는 방법에 대한 아이디어 생각 > 회전변환

닮음의 원칙 응용 생각 고민

# 양쪽 맵의 도형 좌표들을 모두 모은 후 리스트로 모은 후 두 맵 중 하나의 좌표를 하나씩 팝 한 후 
회전변환 후 도형 중 가장 작은 점을 찾은 후 평행 이동 시켰을 때 같은 도형이라면 집합상 동일하다는 점을 체크 후 구하기 
"""

v = []

# 보드 도형
board = []

# 테이블 도형
check = []

from collections import deque
import copy


def find(i, j, g, s):
    global v_baord, v_table, board, check

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    new = []

    q = deque([(i, j)])

    while q:
        a, b = q.popleft()
        v[a][b] = True
        new.append((a, b))

        for k, t in zip(dx, dy):
            if 0 <= a + k < len(g) and 0 <= b + t < len(g[0]):
                if v[a + k][b + t] == False and g[a + k][b + t] == 1:
                    q.append((a + k, b + t))

    new = tuple(new)
    x = copy.deepcopy(new)

    if s == "board":
        check.append((x))
    else:
        board.append((x))

    return 0


def solution(game_board, table):
    global v

    g = game_board
    t = table

    # 열 길이
    m = len(table)

    # 행 길이
    n = len(table[0])

    # 방문 기록
    v = [[False] * n for _ in range(m)]

    s = "board"

    # 보드의 도형 찾기
    for i in range(m):
        for j in range(n):
            if g[i][j] == 1 and v[i][j] == False:
                find(i, j, g, s)

    # 보드 내 도형을 구한 후 초기화
    v = [[False] * n for _ in range(m)]

    s = "table"

    # 테이블의 도형 찾기
    for i in range(m):
        for j in range(n):
            if t[i][j] == 1 and v[i][j] == False:
                find(i, j, t, s)

    # 테이블의 도형을 하나씩 뽑아낸 후 모든 좌표를 90도 회전변환 후 닮음 여부 체크
    result = 0  # 채워질때마다 추가

    # board=deque(board)

    """
    while check:
        k=check.pop()
        k.sort()

        count=len(board)

        while count>0:
            x=board.popleft()
            x.sort()

            # 도형의 개수가 같을 때
            if len(k)==len(x):
                #평행이동 수치
                y=k[0][0]-x[0][0]
                z=k[0][1]-x[0][1]

                change=3 #회전 변환
                while change>0:

                    #기본 상태
                    if change==3:
                        for one,two in k:
                            one+=y
                            two+=z
                            new.append((one,two))

                        new=tuple(new)
                        if set(new)==set(x):
                            break

                        else:
                            change-=1

                    else:
                        for one,two in k:




            else:
                board.append(x)
                count-=1
    """

    return result

# 내 풀이(개선 중)
"""
조건:
1회에 1번
조각 회전가능
뒤집기 불가능 

목표:
채울 수 있는 최대칸을 구하여라 

생각방향:모양이 들어맞아야 인접한 곳이 비는 일이 없어짐에 따라 빈 곳과 테이블을 비교해야한다

회전하는 방법에 대한 아이디어 생각

"""


def solution(game_board, table):
    answer = -1
    return answer


# 다른 사람 풀이
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# programmers 퍼즐조각채우기

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# board와 puzzle의 각각 빈공간과 블럭을 찾는 함수 (BFS)
def find_block(board, f):
    empty_board_list = []
    visited = [[False] * len(board[0]) for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if not visited[i][j] and board[i][j] == f:
                queue = deque([(i, j)])
                board[i][j] = f ^ 1
                visited[i][j] = True
                lst = [(i, j)]

                while queue:
                    x, y = queue.popleft()
                    for _ in range(4):
                        nx, ny = x + dx[_], y + dy[_]
                        if nx < 0 or nx > len(board) - 1 or ny < 0 or ny > len(board) - 1:
                            continue
                        elif board[nx][ny] == f:
                            queue.append((nx, ny))
                            board[nx][ny] = f ^ 1
                            visited[nx][ny] = True
                            lst.append((nx, ny))
                empty_board_list.append(lst)

    return empty_board_list


# block의 인덱스들로 table을 만드는 함수
def make_table(block):
    x, y = zip(*block)
    c, r = max(x) - min(x) + 1, max(y) - min(y) + 1
    table = [[0] * r for _ in range(c)]

    for i, j in block:
        i, j = i - min(x), j - min(y)
        table[i][j] = 1
    return table


# 오른쪽으로 90도 회전하는 함수
def rotate(puzzle):
    rotate = [[0] * len(puzzle) for _ in range(len(puzzle[0]))]
    count = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 1:
                count += 1
            rotate[j][len(puzzle) - 1 - i] = puzzle[i][j]
    return rotate, count


def solution(game_board, table):
    answer = 0
    empty_blocks = find_block(game_board, 0)
    puzzles = find_block(table, 1)

    for empty in empty_blocks:
        filled = False
        table = make_table(empty)

        for puzzle_origin in puzzles:
            if filled == True:
                break

            puzzle = make_table(puzzle_origin)
            for i in range(4):
                puzzle, count = rotate(puzzle)

                if table == puzzle:
                    answer += count
                    puzzles.remove(puzzle_origin)
                    filled = True
                    break

    return answer

# 다른 사람 풀이
def solution(game_board, table):

    # game_board의 빈칸, table의 블럭 찾는 함수
    def finding(mat, num):
        # return할 블럭 및 빈칸들이 들어있는 배열
        arr = []
        visit = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                # 현재 찾는 것(블럭 / 빈칸)과 같고 방문하지 않았으면 BFS
                if mat[i][j] != num or visit[i][j]:
                    continue

                Q = [[i, j]]
                visit[i][j] = 1
                k = 0
                while k < len(Q):
                    r, c = Q[k]
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < n and 0 <= nc < n:
                            if not visit[nr][nc] and mat[nr][nc] == num:
                                Q.append([nr, nc])
                                visit[nr][nc] = 1
                    k += 1

                # 도형 추가
                arr.append(Q)
        return arr

    # 도형 위치 인덱스를 1개의 문자열로 이어서 반환
    def hashing(group):
        # 해당 도형 위치의 가장 왼쪽 모서리
        min_r, min_c = 50, 50
        for r, c in group:
            min_r = min(min_r, r)
            min_c = min(min_c, c)

        # 도형을 왼쪽 구석에 넣었을때 위치로 갱신
        for i in range(len(group)):
            group[i][0] -= min_r
            group[i][1] -= min_c

        # 최선 행, 차선 열 오름차순으로 정렬
        group.sort()


        # 문자열로 바꿔주고 return
        arr = []
        for r, c in group:
            arr.append(str(r))
            arr.append(str(c))

        return ''.join(arr)

    # 빈칸의 위치를 90도 회전시키는 함수
    def rotate(shape):
        for i in range(len(shape)):
            r, c = shape[i]
            shape[i] = [c, -r]

    n = len(game_board)
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    answer = 0

    # 블럭과 빈칸 찾음
    block = finding(table, 1)
    blank = finding(game_board, 0)

    # 블럭들 문자열로 해싱후 딕셔너리에 저장
    for i in range(len(block)):
        block[i] = hashing(block[i])

    temp = dict()
    for i in block:
        temp[i] = temp.get(i, 0) + 1
    block = temp

    # 빈칸들을 순회하면서
    # 해당 빈칸을 4번 90도 회전하며, 맞는 블럭이 있는지 탐색
    # 있으면 블럭 딕셔너리에 개수 -1
    for i in range(len(blank)):
        for _ in range(4):
            rotate(blank[i])
            hash_blank = hashing(blank[i])
            if block.get(hash_blank):
                block[hash_blank] -= 1

                # 인덱스가 행열행열....식으로 들어가기 때문에
                # 문자열의 길이 //2 해서 answer에 추가
                answer += len(hash_blank)//2
                break

    return answer