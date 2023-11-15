# 내 풀이(개선 중)
def solution(n):
    result = []

    tri = []

    t = int(n * (1 + n) / 2)

    for a in range(1, n + 1):
        k = [False for b in range(a)]
        tri.append(k)

    count = 1
    direction = 0
    # 높이
    high = n
    start = 0  # 아래 대각선 시작 위치
    left = 0  # 왼쪽방향
    right = 0
    while count <= t:
        # 1 아래 대각선
        if direction == 0:
            for a in range(start, n):
                for b in range(left, len(tri[a])):
                    if tri[a][b] == False:
                        tri[a][b] = count
                        count += 1
                        break
                    else:
                        continue
            direction = 1

        # 2 밑변
        elif direction == 1:
            for a in range(len(tri[high - 1])):
                if tri[high - 1][a] == False:
                    tri[high - 1][a] = count
                    count += 1

            high -= 1

            direction = 2

        # 3 오른쪽 대각선
        elif direction == 2:
            for a in range(high - 1, 0, -1):
                for b in range(len(tri[a]) - 1 - right, -1, -1):
                    if tri[a][b] == False:
                        tri[a][b] = count
                        count += 1
                        break
            direction = 0
            start += 2
            left += 1
            right += 1

    for a in range(len(tri)):
        result += tri[a]

    return result