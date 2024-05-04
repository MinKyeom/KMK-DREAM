"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/118668
"""
# 내 풀이(개선 중)
# 알고력: 0이상의 정수 코딩력: 0이상의 정수
# 조건: 알고력, 코딩력, 알고력 증가량, 코딩력 증가량, 걸리는 시간

# 목표: 모든 문제를 푸는 코딩력,알고력을 얻는 최단 시간 (최단 시간안에 역량 얻기)
# 중요포인트:모든 문제 다 안풀어도 됨,같은 문제 여러번 풀기 가능

# 생각 접근: 최대로 걸리는 시간을 산정 후 그 시간에 도달하기 전 코딩력 알고력 체크
# 완탐 불가능
# 효율1 알고력 효율2 코딩력을 기준으로 가장 효율이 좋은 것을 넣는 방식 고민


import heapq


def solution(alp, cop, problems):
    result = []

    check_alp, check_cop = 0, 0

    # 걸리는 시간

    count = 0

    for a, c, algorism, coding, time in problems:
        check_alp = max(a, check_alp)
        check_cop = max(c, check_cop)
        count += time

    q = [[0, alp, cop]]

    while q:
        time, algorism, coding = heapq.heappop(q)

        before = len(q)

        if algorism >= check_alp and coding >= check_cop:
            return time

        for a, b, c, d, t in problems:
            if a <= algorism and b <= coding:
                if algorism >= check_alp and d < t:
                    continue
                elif algorism >= check_alp and d <= t:
                    heapq.heappush(q, [time + t, algorism + c, coding + d])

                elif coding >= check_cop and c < t:
                    continue

                elif coding >= check_cop and c >= t:
                    heapq.heappush(q, [time + t, algorism + c, coding + d])

                else:
                    heapq.heappush(q, [time + t, algorism + c, coding + d])

        if algorism < check_alp and coding < check_cop:
            heapq.heappush(q, [time + 1, algorism + 1, coding])
            heapq.heappush(q, [time + 1, algorism, coding + 1])
            heapq.heappush(q, [time + 2, algorism + 1, coding + 1])
        elif algorism < check_alp and not coding < check_cop:
            heapq.heappush(q, [time + 1, algorism + 1, coding])
        elif not algorism < check_alp and coding < check_cop:
            heapq.heappush(q, [time + 1, algorism, coding + 1])


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
