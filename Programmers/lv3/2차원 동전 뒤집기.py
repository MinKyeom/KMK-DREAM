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
