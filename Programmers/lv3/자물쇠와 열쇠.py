"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/60059
"""

# 내 풀이(개선 중)
"""
최대 이동 상하좌우 모두 n번씩
회전 n

상하 , 좌우 
각각 모두 한 후 
회전 90도를 4번 한 후 확인 후 
그래도 불가능하다면 False
"""
import copy
from itertools import product


def rotation():
    return 0


def move():
    return 0


def open_door():
    return 0


def solution(key, lock):
    rotation = [0, 1, 2, 3]
    n = len(key)
    check = [k - n for k in range(2 * n + 1)]

    move = list(product(check, repeat=2))

    lock_check = []
    # 홈 위치
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 1:
                lock_check.append((i, j))

    flag = False

    for r in rotation:
        start = copy.deepcopy(key)

    for ud, lr in move:
        break

    return flag

# 다른 사람 풀이
def compare(board,key,x,y,M, N):
    answer = True
    # x,y는 key를 더할 시작 좌표
    # M은 키의 길이로 board에 키 전체값을 더해야한다.
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] += key[i][j]

    for i in range(N):
        if not answer: break

        for j in range(N):
            if board[i+M][j+M] != 1:
                answer = False
                break
    #  더해진 board에 다시 key 빼기
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]

    return answer

def solution(key, lock):

    N, M = len(lock), len(key)

    board = [[0] * (N + 2*M) for _ in range(N + 2*M)]
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]

    for i in range(4):
        key = rotate(key)

        # 1에서 시작하는 이유?
        # 1에서 board의 범위는 0 ~ N+2M
        # 0부터 시작하게 되면 key랑 lock이 겹치는 부분이 하나도 없어서 의미가 없다.
        # 마찬가지로 N+M은 겹치는 부분이 없고, N+M보다 큰 경우 범위인 N+2M의 범위를 넘기기 때문에 런타임 에러 발생

        for i in range(1, N+M):
            for j in range(1, N+M):
                # board의 시작점이 i,j좌표.
                if compare(board, key, i, j, M, N):
                    return True

    return False


def rotate(key):
    n = len(key)

    rotate_key = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotate_key[j][n-i-1] = key[i][j]
    return rotate_key

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))