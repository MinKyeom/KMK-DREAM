"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/87377
"""
# 풀이 과정
def solution(line):
    from itertools import combinations

    # 직선 2개씩 묶음 집합
    k = list(combinations(line, 2))

    # 교점들의 집합
    result = []
    line_x, line_y = [], []
    for a in k:
        a = list(a)
        # ad-bc check 평행 또는 일치 확인
        if a[0][0] * a[1][1] - a[0][1] * a[1][0] == 0:
            continue

        else:
            x = (a[0][1] * a[1][2] - a[0][2] * a[1][1]) / (a[0][0] * a[1][1] - a[0][1] * a[1][0])
            y = (a[0][2] * a[1][0] - a[0][0] * a[1][2]) / (a[0][0] * a[1][1] - a[0][1] * a[1][0])

            if int(x) == x and int(y) == y:
                result.append([int(x), int(y)])
                line_x.append(int(x))
                line_y.append(int(y))
    ################### 교점까지 완료 ##################
    # print(result)
    # print(line_x)
    line_y.sort()
    print(line_y)

    line_x.sort()
    print(line_y)

    """
    if abs(line_x[0])>=abs(line_x[-1]):
        max_x=abs(line_x[0])
    else:
        max_x=abs(line_x[-1])
    """

    check_x = max(line_x) - min(line_x) + 1

    # print(check_x,"x")
    map = [list("." * check_x) for b in range(min(line_y), max(line_y) + 1)]

    # print(map, "map")

    result.sort(key=lambda x: (-x[1]))
    # print(result)

    for c, d in result:
        # print(max(line_y)-d,max_x+c,"좌표 확인")
        map[max(line_y) - d][c - min(line_x)] = "*"

    for t in range(len(map)):
        map[t] = "".join(map[t])

    # print(map)

    return map
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

# 다른 사람 풀이
def solution(line):
    stars = []

    # 교차점 찾기
    for i in range(len(line)):
        a, b, e = line[i]
        for j in range(i + 1, len(line)):
            c, d, f = line[j]
            # 분모가 0인 경우
            if a * d - b * c == 0:
                continue
            # 분모가 0이 아닌 경우, 정수일 때만
            elif (b * f - e * d) / (a * d - b * c) == int((b * f - e * d) / (a * d - b * c)) and \
                    (e * c - a * f) / (a * d - b * c) == int((e * c - a * f) / (a * d - b * c)):
                x = int((b * f - e * d) / (a * d - b * c))
                y = int((e * c - a * f) / (a * d - b * c))
                stars.append((x, y))  # 교점 리스트에 추가

    stars = list(set(stars))  # 중복 제거
    stars.sort(key=lambda x: (x[1], -x[0]), reverse=True)  # x좌표 오름차순, y좌표 내림차순

    # x,y 최대,최소 구하기
    x_list = []
    y_list = []
    for i in stars:
        x_list.append(i[0])
        y_list.append(i[1])
    x_max = max(x_list)
    x_min = min(x_list)
    y_max = max(y_list)
    y_min = min(y_list)

    # 좌표 초기화
    plaid = [['.' for _ in range(x_min, x_max + 1)] for _ in range(y_min, y_max + 1)]
    for i in stars:
        x = i[0] - x_min
        y = y_max - i[1]  # x,y 좌표로 변경
        plaid[y][x] = '*'  # y가 행, x가 열

    result = []
    for i in plaid:  # 문자열로 합쳐서 결과 리스트에 추가
        result.append(''.join(i))
    return result
# 다른 사람 풀이
def solution(line):
    # 교점구하기
    nodeList = list()
    for i in range(len(line)):
        a, b, e = line[i]

        for c, d, f in line[i + 1:]:
            if a * d - b * c == 0: continue
            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)

            if int(x) == x and int(y) == y and (x, y) not in nodeList:
                nodeList.append((int(x), int(y)))

    # 교점의 가장 큰/작은 값 구하기
    nodeList.sort(key=lambda x: x[0])
    minx, maxx = nodeList[0][0], nodeList[-1][0]
    nodeList.sort(key=lambda x: x[1])
    miny, maxy = nodeList[0][1], nodeList[-1][1]

    # 배열에 별 그리기
    arr = [["." for j in range(maxx - minx + 1)] for i in range(maxy - miny + 1)]
    for x, y in nodeList:
        r, c = y - miny, x - minx
        arr[r][c] = "*"

    return ["".join(item) for item in arr][::-1]  # r방향이 좌표와 반대이므로 뒤집어서 출력