"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/84021
"""
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


