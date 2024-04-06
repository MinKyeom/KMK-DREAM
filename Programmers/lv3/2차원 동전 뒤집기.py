# 내 풀이(시간 초과)
# 비트 마스크를 활용하여 재풀이
# nCr 원리등에 활용

# 내 풀이(개선 중)
# 조건: 동전을 뒤집기 위해서는 해당 줄에 포함된 모든 동전 뒤집기
# 0: 앞면 1:뒷면
# 만들 수 없다면 1

# 초기 모형:beginning, 목표 모형:target

# 목표: 최소 몆 번을 뒤집어야 목표한 모형이 되는지 여부

# 생각방향
# 하나의 돌의 앞 뒤 모양을 바꿀 떄 십자가 형태로 가로 세로 다 바꾼다!(잘못된 생각)
# 행 또는 열을 통째로 뒤집는다 행과 열 동시에 x
# 그리디 생각 > 세부 조건이 너무 많아 풀기 난해 방향 전환
# 타겟이 10으로 길이가 짧기 때문에 브루트포스 접근 생각
# 뒤집는 순서에 따라 바뀌는가 여부 확인 후 풀이 스타트
# deepcopy를 활용하여 원형을 만든 후 가로 바꿀 거 세로 바꿀 거를 바꾼 후 타겟과 확인 (효율성 개선 필요)
# 각각은 모두 뒤집냐 뒤집지 않냐의 상황을 감안하여 다시 완탐의 방향으로 접근!

# 임의의 돌이 다시 원래 형태로 유지되려면 0 또는 짝수번을 유지해야한다
# dp로 접근: 지속적인 형태의 반복
# 주어진 타겟의 길이로 볼 떄 여러번 반복 가능

from itertools import combinations
from collections import deque
import copy


def change_raw(new, i, m):
    for k in i:
        for t in range(len(m)):
            if new[t][k] == 0:
                new[t][k] = 1
            else:
                new[t][k] = 0

    return new


def change_col(new_2, j, n):
    for k in j:
        for t in range(len(n)):
            if new_2[k][t] == 0:
                new_2[k][t] = 1
            else:
                new_2[k][t] = 0

    return new_2


def solution(beginning, target):
    b = beginning
    t = target

    # 타겟과 같을 경우 바로 끝
    if b == t:
        return 0

    elif len(b) == 1:
        return 1

    m = [k for k in range(len(target))]  # 세로 길이
    n = [t for t in range(len(target[0]))]  # 가로 길이

    check = []

    for i in m:
        for j in n:
            check.append([i, j])

    check.sort(key=lambda x: (x[0] + x[1]))

    check = deque(check)

    check.popleft()  # [0,0] 제거 완전 같은 경우 제거

    # m:세로 n:가로
    while check:
        raw, col = check.popleft()  # raw:가로 바꿀 줄 수 # col: 세로 바꿀 줄 수

        raw_list = list(combinations(n, raw))
        col_list = list(combinations(m, col))

        if raw == 0:
            for i in col_list:
                new = copy.deepcopy(b)  # 기본 모형 초기화
                new = change_col(new, i, n)

                if new == t:
                    return col + raw

            continue

        elif col == 0:
            for i in raw_list:
                new = copy.deepcopy(b)  # 기본 모형 초기화
                new = change_raw(new, i, m)

                if new == t:
                    return raw + col

            continue

        for i in raw_list:  # i 바꿀 라인 모음

            new = copy.deepcopy(b)  # 새로운 형태를 만들기 위해 deepcopy 비긴닝 복사 #기본 모형 초기화

            new_raw = change_raw(new, i, m)  # 형태 변환(가로 변환)

            for j in col_list:  # j 바꿀 라인 모음

                new_2 = copy.deepcopy(new_raw)

                final = change_col(new_2, j, n)

                if final == t:
                    return raw + col

    return -1
# 내 풀이 (개선 중)
# 조건: 동전을 뒤집기 위해서는 해당 줄에 포함된 모든 동전 뒤집기
# 0: 앞면 1:뒷면
# 만들 수 없다면 1

# 초기 모형:beginning, 목표 모형:target

# 목표: 최소 몆 번을 뒤집어야 목표한 모형이 되는지 여부

# 생각방향
# 하나의 돌의 앞 뒤 모양을 바꿀 떄 십자가 형태로 가로 세로 다 바꾼다!(잘못된 생각)
# 행 또는 열을 통째로 뒤집는다

# 임의의 돌이 다시 원래 형태로 유지되려면 0 또는 짝수번을 유지해야한다
# dp로 접근: 지속적인 형태의 반복
# 주어진 타겟의 길이로 볼 떄 여러번 반복 가능

def solution(beginning, target):
    b = beginning
    t = target

    if b == t:
        return 0


    else:
        result = 0

        check = [[0] * len(target[0]) for _ in range(len(target))]

        for i in range(len(target)):
            for j in range(len(target[0])):
                count_1 = sum(target[i])
                start_1 = sum(b[i])
            count_2 = 0
            start_2 = 0
            for k in range(len(target)):
                count_2 += target[k][j]
                start_2 += b[k][j]

            check[i][j] = max(abs(count_1 - start_1), abs(count_2 - start_2))

        print(check)
    return result if result != 0 else -1


# 다른 사람 풀이
# so1 1
def flipColumn(arr, col):
    n = len(arr)

    for i in range(n):
        if arr[i][col] == 1:
            arr[i][col] = 0
        else:
            arr[i][col] = 1


def solution(beginning, target):
    answer = float("inf")
    rows = len(beginning)
    cols = len(beginning[0])

    flipped = []
    # 미리 원본 배열을 flip시켜서 저장
    for i in range(rows):
        flipped.append([])
        for j in range(cols):
            if beginning[i][j]:
                flipped[i].append(0)
            else:
                flipped[i].append(1)

    # and시킬 bitmask를 돌면서
    for unit in range(1 << rows):
        rowFlipped = []
        flipCnt = 0
        for i in range(rows):
            # 000, 010, 100... bitmask 생성
            comp = 1 << i

            # and한 값이 0이 아니면 해당 row 뒤집기
            if unit & comp:
                rowFlipped.append(flipped[i][:])
                flipCnt += 1
            # 해당 row 뒤집지 않기
            else:
                rowFlipped.append(beginning[i][:])

        # 열 뒤집기
        for j in range(cols):
            curCol = []
            targetCol = []

            for i in range(rows):
                curCol.append(rowFlipped[i][j])
                targetCol.append(target[i][j])

            # 현재 column과 target column이 다르면 뒤집기
            if curCol != targetCol:
                flipColumn(rowFlipped, j)
                flipCnt += 1

            # 결국 뒤집은 결과가 target과 같으면 뒤집은 횟수 갱신
        if rowFlipped == target:
            answer = min(answer, flipCnt)

    if answer == float("inf"):
        answer = -1

    return answer

# sol2
def solution(beginning, target):
    # beginning과 target 차이
    # 뒤집어야 하면 1, 그대로 둬야하면 0
    row, col = len(beginning), len(beginning[0])
    board = [[1 if beginning[i][j] != target[i][j] else 0 for j in range(col)] for i in range(row)]

    answer = 0
    # 행 전부 뒤집기
    for i in range(row):
        if board[i][0] == 1:
            answer += 1
            for j in range(col):
                board[i][j] = 1 - board[i][j]

                # 열 확인하기
    for j in range(col):
        tmp = set([board[i][j] for i in range(row)])  # j열
        if len(tmp) == 2:  # 0과 1이 섞여 있다면
            answer = -1
            목표
            상태
            도달
            불가능
            break
        elif 1 in tmp:  # 1로만 이루어져 있으면 = 뒤집어야 하면
            answer += 1

    return answer


# sol3
import math


def fliprow(board, bits):
    flipped = []
    for i in range(len(board)):
        # i번째 row를 뒤집어야 하면 뒤집은 리스트를 저장합니다.
        if bits & (1 << i):
            flipped.append([1 - x for x in board[i]])
        else:
            flipped.append(board[i])
    return flipped


def try_flipcol(board, target):
    n_colflip = 0
    # i번쨰 컬럼을 확인하는데
    for i in range(len(board[0])):
        # 경우의 수는 세가지입니다.
        # 1. 안 뒤집어도 되는 경우
        if [row[i] for row in board] == [t[i] for t in target]:
            continue
        # 2. 뒤집으면 같아지는 경우
        elif [1 - row[i] for row in board] == [t[i] for t in target]:
            n_colflip += 1
        # 3. 어떻게 해도 같아질 수 없는 경우
        else:
            return -1

    return n_colflip


def solution(beginning, target):
    # 뒤집어야 하는 row를 비트로 표현합니다.
    # n개의 row가 있으면 0~2**n-1 까지 수로 나타내면 됩니다.
    n = len(beginning)
    ans = math.inf
    for bits in range(2 ** n):
        flipped = fliprow(beginning[:], bits)
        n_colflip = try_flipcol(flipped, target)
        if n_colflip == -1:
            continue

        n_rowflip = sum(bits & (1 << i) != 0 for i in range(n))
        ans = min(n_rowflip + n_colflip, ans)

    return ans if ans != math.inf else -1
