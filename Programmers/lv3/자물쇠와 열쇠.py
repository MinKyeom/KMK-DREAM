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