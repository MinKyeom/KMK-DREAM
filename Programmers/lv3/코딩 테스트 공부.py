"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/118668
"""

# 내 풀이(개선 중)
# 알고력: 0이상의 정수 코딩력: 0이상의 정수
# 조건: 알고력, 코딩력, 알고력 증가량, 코딩력 증가량, 걸리는 시간

# 목표: 모든 문제를 푸는 코딩력,알고력을 얻는 최단 시간 (최단 시간안에 역량 얻기)
# 단 모든 문제 다 안풀어도 됨

# 생각 접근: 최대로 걸리는 시간을 산정 후 그 시간에 도달하기 전 코딩력 알고력 체크

def solution(alp, cop, problems):
    check_alp, check_cop = 0, 0

    # 걸리는 시간

    count = 0

    for a, c, add_a, add_c, time in problems:
        check_alp = max(a, check_alp)
        check_cop = max(a, check_cop)
        count += time

    answer = 0
    return answer
