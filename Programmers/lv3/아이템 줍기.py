"""
출처: 프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/87694
"""

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