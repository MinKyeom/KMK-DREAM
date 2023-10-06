# 내 풀이 (개선 중)
def solution(line):
    from itertools import combinations
    from collections import deque

    k = list(combinations(line, 2))
    result = []
    max_x, max_y = 0, 0

    for a in k:
        a = list(a)
        # 직선 두 개 계산
        if (a[0][0] * a[1][1]) - (a[0][1] * a[1][0]) == 0:
            continue
        else:
            # 소거법
            # y좌표
            c = (a[0][0] * a[1][2] - a[1][0] * a[0][2]) / (a[0][1] * a[1][0] - a[0][0] * a[1][1])
            if c == int(c):
                # x좌표
                if a[0][0] != 0:
                    b = (a[0][1] * (-1) * c + a[0][2] * (-1)) / a[0][0]
                    if b == int(b):
                        result.append([int(b), int(c)])
                        if max_x < abs(b):
                            max_x = int(abs(b))
                        if max_y < abs(c):
                            max_y = int(abs(c))

                else:
                    result.append([0, int(c)])
                    # if max_y<abs(c):
                    # max_y=int(abs(c))

            else:
                continue
    # print(result)
    # print(int(max_x),int(max_y),"최대값")

    # result.sort(key=lambda x:(-x[1],x[0]))

    # result=deque(result)

    answer = []

    check_y = 0
    star = ""
    print(max_x, max_y, "최댓값")
    print(result)
    map = [list("." * (max_x * 2 + 1))] * (max_y * 2 + 1)
    # x,y middle max_x+1: x middle max_y+1: y middle

    for v, w in result:
        if v >= 0 and w >= 0:
            map[max_y - abs(w)][max_x + abs(v)] = "*"
        elif v >= 0 and w < 0:
            map[max_y - abs(w)][max_x - abs(v)] = "*"
        elif v < 0 and w >= 0:
            map[max_y + abs(w)][max_x + abs(v)] = "*"
        else:
            map[max_y + abs(w)][max_x - abs(v)] = "*"

    for t in range(len(map)):
        map[t] = "".join(map[t])

    # print(map)

    return answer

# 다른 사람 풀이
from itertools import combinations


def calculation(eq1, eq2):
    x1, y1, c1 = eq1  # 직선1
    x2, y2, c2 = eq2  # 직선2

    # 기울기가 깉아 해가 없는 경우
    if x1 * y2 == y1 * x2:
        return

    # 두 직선의 해
    x = (y1 * c2 - c1 * y2) / (x1 * y2 - y1 * x2)
    y = (c1 * x2 - x1 * c2) / (x1 * y2 - y1 * x2)

    # 두 직선의 해 x, y가 모두 정수라면 반환
    if x == int(x) and y == int(y):
        return [int(x), int(y)]


def solution(lines):
    points = []
    # 모든 선들의 교점 확인
    for eq1, eq2 in combinations(lines, 2):
        point = calculation(eq1, eq2)
        if point: points.append(point)

    # 그림의 시작점과 마지막점 찾기
    w1, w2 = min(points, key=lambda x: x[0])[0], max(points, key=lambda x: x[0])[0] + 1
    h1, h2 = min(points, key=lambda x: x[1])[1], max(points, key=lambda x: x[1])[1] + 1

    # 별을 포함하는 최소한의 크기 배열 생성
    answer = [['.'] * (w2 - w1) for _ in range((h2 - h1))]

    # 그림의 시작점을 기준으로 교점 위치 "*" 변환
    for x, y in points:
        answer[y - h1][x - w1] = '*'

    answer.reverse()

    return [''.join(a) for a in answer]