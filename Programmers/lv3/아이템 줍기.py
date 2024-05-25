"""
출처: 프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/87694
"""
# 내 풀이(개선 중)
"""
사각형들의 모든 점들을 알아낸 후 주어진 점을 이동시키는 것을 실행

그 중 사각형 내부에 있는 점 거르기+중복점 제거 생각 아이디어

그리고 매 순간 그 중 아이템이 있는 점에 도달하는 지 여부 확인+ 최단 거리 구하기 

# 주어진 조건들 통하여 알 수 있는 정보: 
주어진 점들의 좌표들, 선분들의 좌표, 외부에 있는 점들의 좌표, 
"""
from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    # sol(내부의 선분등을 제대로 표현하기 힘듬)
    #     # 내부에 있지 않은 점
    #     check=set([])

    #     for x1,y1,x2,y2 in rectangle:
    #         new=[]

    #         for v1,w1,v2,w2 in rectangle:
    #             if  v1<x1<v2 and w1<y1<w2:
    #                 new.append((x1,y1))
    #             if  v1<x2<v2 and w1<y1<w2:
    #                 new.append((x2,y1))
    #             if v1<x1<v2 and w1<y2<w2:
    #                 new.append((x1,y2))
    #             if v1<x2<v2 and w1<y2<w2:
    #                 new.append((x2,y2))

    #         check=check|(set([(x1,y1),(x1,y2),(x2,y1),(x2,y2)])-set(new))

    # 이동시킬 맵
    m = [[0] * 50 for _ in range(50)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 사각형 위의 모든 점
    new = []

    for x1, y1, x2, y2 in rectangle:

        for x in [x1, x2]:
            for y in range(y1, y2 + 1):
                new.append((x, y))

        for y in [y1, y2]:
            for x in range(x1, x2 + 1):
                new.append((x, y))

    new = set(new)  # 중복 제거

    # 사각형 내부의 점 구분
    check = []

    for x1, y1, x2, y2 in rectangle:
        for x, y in new:
            if x1 < x < x2 and y1 < y < y2:
                check.append((x, y))

    road = new - set(check)

    for x, y in road:
        m[x][y] = 1

    #     m[characterX][characterY]="start"

    #     m[itemX][itemY]="destination"

    q = [(characterX, characterY)]

    # 방문처리 확인
    v = [[0] * 50 for _ in range(50)]

    plus = []

    # 거리
    result = 0

    # bfs
    while q:
        x, y = q.pop()

        # 방문 처리
        v[x][y] = 1

        if x == itemX and y == itemY:
            return result

        for nx, ny in zip(dx, dy):
            if 0 <= x + nx <= 50 and 0 <= y + ny <= 50 and v[x + nx][y + ny] == 0 and m[x + nx][y + ny] == 1:
                plus.append((x + nx, y + ny))

        if len(q) == 0:
            plus = list(set(plus))
            q += plus
            result += 1
            plus = []

        print(q)


# 내 풀이

"""
사각형들의 모든 점들을 알아낸 후 주어진 점을 이동시키는 것을 실행

그 중 사각형 내부에 있는 점 거르기+중복점 제거 생각 아이디어

그리고 매 순간 그 중 아이템이 있는 점에 도달하는 지 여부 확인+ 최단 거리 구하기 
"""


def solution(rectangle, characterX, characterY, itemX, itemY):
    check = []

    #     for x1,y1,x2,y2 in rectangle:

    #         for v1,w1,v2,w2 in rectangle:

    #             if  v1<x1<v2 and w1<y1<w2:

    answer = 0
    return answer