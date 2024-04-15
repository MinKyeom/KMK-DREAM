"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/131702
"""
# 내 풀이(개선 중)
# 조건: 시계 방향으로만 돌리는거 가능, 한 번당 90도 단 상하좌우도 같이 돌아간다
# 모서리 3개만 돌아감 꼭짓점:2개 돌아감
# 시계 0:12 1:3 2:6 3:9
# 해결 가능한 퍼즐만 주어집니다.
# 행과 열의  길이는  동일

# 목표: 최소한의 횟수로 퍼즐 해결

# 생각방향: 각각의 모든 수는 3번을 초과하지 않는다(제자리로 돌아가기 때문이다)
# 주어진 조건을 봤을 때 완탐으로해도 시간초과 발생 가능성 적음
# for문을 바탕으로 전체를 둘러본 후 주변이 해당 시계를 포함하여 주변이 전부 0이 아닐경우 실행
# 그리고 만약 해당 시계를 바꿨음에도 주변이 모두 0 아닐경우 하나라도 0일 경우 stop
# 완탐의 경우 모든 시계 내 원소가 0 1 2 3 중 하나라는 생각접근
# 각 칸의 돌려지는 횟수가 총합으로 각 칸이 돌려져야 될 횟수를 4로 나눴을때 나머지 횟수랑 동일해야한다.
# 최대 경우의 수를 만든 후 직접 계산 시 시간 초과 4**64가지이기 떄문이다. 중복 순열
# 줄일 방법을 고민하기 or 새로운 접근 방향 고민
# 포인트 사고: 하나의 줄을 고정! 고정된 줄을 중심으로 나머지 줄의 돌릴 수도 정해진다
# 하나씩 고정시키면 자연스럽게 위에 맞춰서 아래가 정해진다!! 경우의 수도 첫줄 경우의 수이다 4**8가 최대가 된다
# 원순열 기본 원리랑 비슷 고정시킨 후 원형으로 만든 후 경우의 수 표현하는 방식

# 시계 돌리기

from itertools import product
from collections import deque


def clock(new, a, b, t, row, col):
    change = [0, 1, 2, 3]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i, j in zip(dx, dy):
        if 0 <= a + i < row and 0 <= b + j < col:
            # k: 돌릴 횟수
            z = (new[a + i][b + j] + t) % 4
            new[a + i][b + j] = change[z]

    return new


def solution(clockHands):
    change = [0, 1, 2, 3]

    result = []

    c = clockHands

    row = len(c)
    col = len(c[0])

    # 목표 모양
    target = [[0] * col for _ in range(row)]

    # 맨 윗줄 고정 시킬 회전 수 경우의 수 중복 순열
    check = deque(list(product([0, 1, 2, 3], repeat=col)))

    while check:
        # 회전 시킬판 deepcopy 대신 시간복잡도가 덜 드는 슬라이싱 활용!
        new = c[:]

        # 기준점이 돌아가는 횟수
        count = 0

        # 고정 시킬 첫줄 회전 횟수 체크
        k = check.popleft()

        for i in range(col):
            if k[i] != 0:
                new[0][i] = change[(new[0][i] + k[i]) % 4]
                count += k[i]

                # 동서남북 바꾸기
                new = clock(new, 0, i, k[i], row, col)

        for v in range(1, row):
            for w in range(col):
                if new[v - 1][w] != 0:
                    # 위를 0으로 만들기 위한 돌릴 횟수 지정
                    x = abs(4 - new[v - 1][w])
                    new[v][w] = change[(new[v][w] + x) % 4]
                    count += x

                    # 동서남북 바꾸기
                    new = clock(new, v, w, x, row, col)

        # 목표한 모양과 같은 경우 기록 (맨 아래가 다를 수 있기 떄문이다)
        if new == target:
            result.append(count)

    return min(result) if len(result) > 0 else 0

# 내 풀이(개선 중)
# 조건: 시계 방향으로만 돌리는거 가능, 한 번당 90도 단 상하좌우도 같이 돌아간다
# 모서리 3개만 돌아감 꼭짓점:2개 돌아감
# 시계 0:12 1:3 2:6 3:9
# 해결 가능한 퍼즐만 주어집니다.
# 행과 열의  길이는  동일

# 목표: 최소한의 횟수로 퍼즐 해결

# 생각방향: 각각의 모든 수는 3번을 초과하지 않는다(제자리로 돌아가기 때문이다)
# 주어진 조건을 봤을 때 완탐으로해도 시간초과 발생 가능성 적음
# for문을 바탕으로 전체를 둘러본 후 주변이 해당 시계를 포함하여 주변이 전부 0이 아닐경우 실행
# 그리고 만약 해당 시계를 바꿨음에도 주변이 모두 0 아닐경우 하나라도 0일 경우 stop
# 완탐의 경우 모든 시계 내 원소가 0 1 2 3 중 하나라는 생각접근
# 각 칸의 돌려지는 횟수가 총합으로 각 칸이 돌려져야 될 횟수를 4로 나눴을때 나머지 횟수랑 동일해야한다.
# 최대 경우의 수를 만든 후 직접 계산 시 시간 초과 4**64가지이기 떄문이다. 중복 순열
# 줄일 방법을 고민하기 or 새로운 접근 방향 고민


# 시계 돌리기

# def operation:

#     return check

def solution(clockHands):
    change = [0, 1, 2, 3]
    result = 0
    c = clockHands

    check = c[:]

    row = len(c)
    col = len(c[0])

    #     for i in range(row):
    #         for j in range(col):

    #             if i+1<row and i-1>=0 and j+1<col and j-1>=0:
    #                 if check[i][j]!=0 and check[i+1][j]!=0 and check[i-1][j]!=0 and check[i][j+1]!=0 and check[i][j-1]!=0:
    #                     check=operation(check,i,j)

    #             # 좌상단 꼭짓점
    #             elif i-1<0 and j-1<0:
    #                 pass

    #             # 우상단 꼭짓점
    #             elif i-1<0 and j+1>=col:
    #                 pass

    #             # 좌하단 꼭짓점
    #             elif i+1>=row and j-1<0:
    #                 pass

    #             # 우하단 꼭짓점
    #             elif i+1>=row and j+1>=col:
    #                 pass

    #             # 모서리
    #             else:
    #                 pass

    return result

# 내 풀이(개선 중)
# 조건: 시계 방향으로만 돌리는거 가능, 한 번당 90도 단 상하좌우도 같이 돌아간다
# 모서리 3개만 돌아감 꼭짓점:2개 돌아감
# 시계 0:12 1:3 2:6 3:9
# 해결 가능한 퍼즐만 주어집니다.

# 목표: 최소한의 횟수로 퍼즐 해결

# 생각방향: 각각의 모든 수는 3번을 초과하지 않는다(제자리로 돌아가기 때문이다)
# 주어진 조건을 봤을 때 완탐으로해도 시간초과 발생 가능성 적음
# for문을 바탕으로 전체를 둘러본 후 주변이 해당 시계를 포함하여 주변이 전부 0이 아닐경우 실행
# 그리고 만약 해당 시계를 바꿨음에도 주변이 모두 0 아닐경우 하나라도 0일 경우 stop
# 완탐의 경우 모든 시계 내 원소가 0 1 2 3 중 하나라는 생각접근
# 각 칸의 돌려지는 횟수가 총합으로 각 칸이 돌려져야 될 횟수를 4로 나눴을때 나머지 횟수랑 동일해야한다.

# 시계 돌리기

# def operation:

#     return check

def solution(clockHands):
    change = [0, 1, 2, 3]
    result = 0
    c = clockHands

    check = c[:]

    row = len(c)
    col = len(c[0])

    #     for i in range(row):
    #         for j in range(col):

    #             if i+1<row and i-1>=0 and j+1<col and j-1>=0:
    #                 if check[i][j]!=0 and check[i+1][j]!=0 and check[i-1][j]!=0 and check[i][j+1]!=0 and check[i][j-1]!=0:
    #                     check=operation(check,i,j)

    #             # 좌상단 꼭짓점
    #             elif i-1<0 and j-1<0:
    #                 pass

    #             # 우상단 꼭짓점
    #             elif i-1<0 and j+1>=col:
    #                 pass

    #             # 좌하단 꼭짓점
    #             elif i+1>=row and j-1<0:
    #                 pass

    #             # 우하단 꼭짓점
    #             elif i+1>=row and j+1>=col:
    #                 pass

    #             # 모서리
    #             else:
    #                 pass

    return result
# 내 풀이(개선 중)

# 조건: 시계 방향으로만 돌리는거 가능, 한 번당 90도 단 상하좌우도 같이 돌아간다
# 모서리 3개만 돌아감 꼭짓점:2개 돌아감
# 시계 0:12 1:3 2:6 3:9
# 해결 가능한 퍼즐만 주어집니다.

# 목표: 최소한의 횟수로 퍼즐 해결

# 생각방향: 각각의 모든 수는 3번을 초과하지 않는다(제자리로 돌아가기 때문이다)
# 주어진 조건을 봤을 때 완탐으로해도 시간초과 발생 가능성 적음
# for문을 바탕으로 전체를 둘러본 후 주변이 해당 시계를 포함하여 주변이 전부 0이 아닐경우 실행
# 그리고 만약 해당 시계를 바꿨음에도 0이 아닐경우 반복 생각
# 완탐의 경우 모든 시계 내 원소가 0 1 2 3 중 하나라는 생각접근

def solution(clockHands):
    change = [0, 1, 2, 3]
    result = 0
    c = clockHands

    check = c[:]

    row = len(c)
    col = len(c[0])

    #     for i in range(row):
    #         for j in range(col):

    #             if i+1<row and i-1>=0 and j+1<col and j-1>=0:
    #                 pass

    #             # 좌상단 꼭짓점
    #             elif i-1<0 and r

    return result