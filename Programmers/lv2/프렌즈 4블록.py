# 내 풀이
# idea: 첫번쨰로 지워지는 블록 제거 후 재배열 후 다시 블록 제거 반복!
def solution(m, n, board):
    from collections import deque

    b = []

    for k in range(m):
        b.append(list(board[k]))

    result = 0

    dx = [1, 0, 1]
    dy = [0, 1, 1]

    while True:
        count = 0  # 지워지는 블록 체크
        check = deque([])  # 지워지는 블록 목록

        # i,j를 중심으로 팔방위 탐색

        for i in range(m):
            for j in range(n):

                if b[i][j] == 0:
                    continue

                if j - 1 >= 0 and i - 1 >= 0:
                    if b[i][j] == b[i - 1][j - 1] == b[i][j - 1] == b[i - 1][j]:
                        check.append([i, j])
                        continue
                if j + 1 < n and i - 1 >= 0:
                    if b[i][j] == b[i][j + 1] == b[i - 1][j + 1] == b[i - 1][j]:
                        check.append([i, j])
                        continue
                if j - 1 >= 0 and i + 1 < m:
                    if b[i][j] == b[i][j - 1] == b[i + 1][j - 1] == b[i + 1][j]:
                        check.append([i, j])
                        continue
                if j + 1 < n and i + 1 < m:
                    if b[i][j] == b[i + 1][j] == b[i + 1][j + 1] == b[i][j + 1]:
                        check.append([i, j])
                        continue
        while check:
            one, two = check.popleft()
            b[one][two] = 0
            count += 1

        if count == 0:  # 지워지는 블록이 없을 경우 답
            return result

        # 블록 재배치 위에 있는걸로 대체
        # 0이 아닌 부분을 내리는 방법?

        for i in range(m - 1, -1, -1):
            for j in range(n):

                if b[i][j] == 0:
                    start = i - 1

                    while start >= 0:
                        if b[start][j] != 0:
                            b[i][j] = b[start][j]
                            b[start][j] = 0
                            break
                        else:
                            start -= 1

        result += count

    answer = result
    return answer

# 다른 사람 풀이
def solution(m, n, board):
    x = board
    x2 =[]

    for i in x:
        x1 = []
        for i2 in i:
            x1.append(i2)
        x2.append(x1)

    point = 1
    while point != 0:
        list = []
        point = 0
        for i in range(m - 1):
            for j in range(n - 1):
                if x2[i][j] == x2[i][j + 1] == x2[i + 1][j] == x2[i + 1][j + 1] != '팡!':
                    list.append([i, j])
                    point += 1

        for i2 in list:
            i, j = i2[0], i2[1]
            x2[i][j], x2[i][j + 1], x2[i + 1][j], x2[i + 1][j + 1] = '팡!', '팡!', '팡!', '팡!'

        for i3 in range(m):
            for i in range(m - 1):
                for j in range(n):
                    if x2[i + 1][j] == '팡!':
                        x2[i + 1][j], x2[i][j] = x2[i][j], '팡!'

    cnt = 0
    for i in x2:
        cnt += i.count('팡!')
    return cnt