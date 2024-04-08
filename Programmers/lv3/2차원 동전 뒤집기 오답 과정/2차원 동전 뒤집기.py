# 오답 과정: 프로그램이 진행되는 큰 순서를 이해 후 이해 안되는 포인트들을 쪼개서 부분이해

# 비트마스크를 통해 내 풀이보다 효율성 좋게 얻는 부분
# 난 각 행의 번호, 열의 번호를 하나씩 구하여 조합으로 개수를 일일이 만든 후 다시 조합을 만든 후 구했다
# deepcopy 대신 슬라이싱으로 메모리 주소를 다르게 원본을 유지하는 방식을 택하여 훨씬 빠른 효율을 만들었다!
# 내가 행과 열에 각각 리스트를 생성 후 조합을 구했던 부분을 for문 하나로 해결하여 압도적으로 효율적이다!
# 완탐 영역에 있어서는 다른 것과 효율을 비교하는것 실례일정도로 빠르다!


# 쪼개서 이해하기

"""
# 행 뒤집기
def flip(ary, bits, row):
    row_cnt = 0
    for i in range(row):
        if bits & (1 << i):  # i번째 행을 뒤집어야 하는 경우
            ary[i] = [1 - e for e in ary[i]]
            row_cnt += 1
    return ary, row_cnt


# 열 확인하기
def check(ary, col):
    col_cnt = 0
    for j in range(col):
        tmp = set([row[j] for row in ary])  # j열
        if len(tmp) == 2:  # 목표 상태 도달 불가능
            return -1
        elif 1 in tmp:  # 뒤집어야 하는 경우
            col_cnt += 1
    return col_cnt


def solution(beginning, target):
    answer = float('inf')
    row, col = len(beginning), len(beginning[0])
    board = [[1 if beginning[i][j] != target[i][j] else 0 for j in range(col)] for i in range(row)]

    # 0...0 : 모든 행을 뒤집지 않는다
    # 1...1 : 모든 행을 뒤집는다
    for bits in range(2 ** row):
        flipped, row_cnt = flip(board[:], bits, row)  # 뒤집어야 할 행만큼 행 뒤집기
        col_cnt = check(flipped, col)  # 열 확인하기
        if col_cnt == -1:  # 목표 상태로 도달 불가능
            continue

        answer = min(row_cnt + col_cnt, answer)

    if answer == float('inf'):
        return -1
    return answer

"""

#######    쪼개서 이해할 포인트 #############

# point 1

# board = [[1 if beginning[i][j] != target[i][j] else 0 for j in range(col)] for i in range(row)]
"""
begin과 타겟이 다르다면 1 그렇지 않다면 0( col과 i의 범위로 수를 for문으로 돌리면서)

목적: 타겟과 다른 부분을 1로 표현으로 구분 지음 
"""

# point 2

# for bits in range(2 ** row):
#     flipped, row_cnt = flip(board[:], bits, row)  # 뒤집어야 할 행만큼 행 뒤집기
#     col_cnt = check(flipped, col)  # 열 확인하기
#     if col_cnt == -1:  # 목표 상태로 도달 불가능
#         continue

"""
목적: 행을 모두 뒤집는걸 전체로 비트마스크 실행 및 모든 행,열은 최대 1번만 뒤집으니까 행을 뒤집은 후 타겟과 다른 열을 확인 후 뒤집기


"""