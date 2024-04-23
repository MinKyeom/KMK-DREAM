"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/118669
"""

# 내 풀이(생각 방향 정리)
# 조건: 1~n번의 지점: 출입구 ,쉼터, 산봉우리 중 하나
# intensity:휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 의미
# 출입구는 처음 끝 한번씩 산봉우리 한 번 포함하는 다시 원래 출입구로 돌아오는 등산코스 다른 출입구 한 번더 반복 x
# 거리 가중치 최소화를 처음 보고 든 생각 다익스트라 알고리즘

# 지점 수:n 등산로 정보:paths 출입구 정보: gates 산봉우리들 번호:summits
# [intensity 최소로 만드는 산봉우리, 그 때의 intensity] 산봉우리가 여러 개 일시 가장 낮은 번호의 산봉우리

# 목표: intensity가 최소가 되도록 등산 코스 정하기

# 생각 방향 등산로를 만들면서 쉼터,산봉우리 갈 시 intensity 재갱신 후 최대로 된 걸 체크

from collections import defaultdict


def solution(n, paths, gates, summits):
    map = defaultdict(list)
    print(map)

    answer = []
    return answer