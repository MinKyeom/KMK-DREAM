"""
출처: 프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/169198
"""

# 풀이 과정
def solution(m, n, startX, startY, balls):
    result = []
    for x, y in balls:
        check = []
        # 아래벽
        if startY >= y and startX == x:
            pass
        else:
            d_1 = ((abs(startX - x) ** 2 + abs(-startY - y) ** 2))
            check.append(d_1)
        # 왼쪽벽
        if startX >= x and startY == y:
            pass
        else:
            d_2 = ((abs(-startX - x) ** 2 + abs(startY - y) ** 2))
            check.append(d_2)
        # 위쪽벽
        if startY <= y and startX == x:
            pass
        else:
            d_3 = ((abs(startX - x) ** 2 + abs(2 * n - startY - y) ** 2))
            check.append(d_3)
        # 오른쪽벽
        if startX <= x and startY == y:
            pass
        else:
            d_4 = ((abs(2 * m - startX - x) ** 2 + abs(startY - y) ** 2))
            check.append(d_4)
        # 왼쪽 사이드
        d_5 = ((abs(-startX - x) ** 2 + abs(-startY - y) ** 2))
        check.append(d_5)
        # 왼쪽 위 사이드
        d_6 = ((abs(-startX - x) ** 2 + abs(2 * n - startY - y) ** 2))
        check.append(d_6)
        # 오른쪽 위 사이드
        d_7 = ((abs(2 * m - startX - x) ** 2 + abs(2 * n - startY - y) ** 2))
        check.append(d_7)
        # 오른쪽 아래 사이드
        d_8 = ((abs(2 * m - startX - x) ** 2 + abs(-startY - y) ** 2))
        check.append(d_8)
        result.append(min(check))

    return result


# 다른 사람 풀이
def solution(m, n, startX, startY, balls):
    answer = []
    start = [startX, startY]
    for i in range(len(balls)):
        end = [balls[i][0], balls[i][1]]
        distance = 10 ** 10
        temp = []
        if start[0] != end[0] or start[1] > end[1]:
            temp.append(abs(start[0] - end[0]) ** 2 + abs(2 * n - start[1] - end[1]) ** 2)  # 우
        if start[0] != end[0] or start[1] < end[1]:
            temp.append(abs(start[0] - end[0]) ** 2 + abs(start[1] + end[1]) ** 2)  # 좌
        if start[1] != end[1] or start[0] < end[0]:
            temp.append(abs(start[0] + end[0]) ** 2 + abs(start[1] - end[1]) ** 2)  # 상
        if start[1] != end[1] or start[0] > end[0]:
            temp.append(abs(2 * m - start[0] - end[0]) ** 2 + abs(start[1] - end[1]) ** 2)  # 하
        for dist in temp:
            if dist < distance:
                distance = dist
        answer.append(distance)
    return answer

###
def solve(x, y, startX, startY, ballX, ballY):
    dists = []
    # 위쪽 벽
    # 단, x좌표가 같고 목표의 y가 더 크면 안된다.
    if not (ballX == startX and ballY > startY):
        d2 = (ballX - startX) ** 2 + (ballY - 2 * y + startY) ** 2
        dists.append(d2)
    # 아래쪽 벽
    # 단, x좌표가 같고 목표의 y가 더 작으면 안된다.
    if not (ballX == startX and ballY < startY):
        d2 = (ballX - startX) ** 2 + (ballY + startY) ** 2
        dists.append(d2)
    # 왼쪽 벽에 맞는 경우
    # 단, y좌표가 같고 목표의 x가 더 작으면 안된다.
    if not (ballY == startY and ballX < startX):
        d2 = (ballX + startX) ** 2 + (ballY - startY) ** 2
        dists.append(d2)
    # 오른쪽 벽
    # 단, y좌표가 같고 목표의 x가 더 크면 안된다.
    if not (ballY == startY and ballX > startX):
        d2 = (ballX - 2 * x + startX) ** 2 + (ballY - startY) ** 2
        dists.append(d2)

    return min(dists)


def solution(m, n, startX, startY, balls):
    answer = []
    for ballX, ballY in balls:
        answer.append(solve(m, n, startX, startY, ballX, ballY))
    return answer
