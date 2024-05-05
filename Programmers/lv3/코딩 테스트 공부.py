"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/118668
"""
# 내 풀이(개선 중)
# 알고력: 0이상의 정수 코딩력: 0이상의 정수
# 조건: 알고력, 코딩력, 알고력 증가량, 코딩력 증가량, 걸리는 시간

# 목표: 모든 문제를 푸는 코딩력,알고력을 얻는 최단 시간 (최단 시간안에 역량 얻기)
# 중요포인트:모든 문제 다 안풀어도 됨,같은 문제 여러번 풀기 가능

# 생각 접근 및 방향 변화: 최대로 걸리는 시간을 산정 후 그 시간에 도달하기 전 코딩력 알고력 체크
# 도달해야 될 알고력과 코딩력을 확인 후 최단 시간에 도달하는 방향으로 나아가는 생각
# 완탐 불가능
# 효율1 알고력 효율2 코딩력을 기준으로 가장 효율이 좋은 것을 넣는 방식 고민
# 시간 대비 효율
# 시간 효율로 dp 구성 가능한지 여부(반복되는 문제를 통해 답을 찾는 과정이라 생각이 들기 때문이다.)
# 요구력에 제일 근사한 값이 두 개 나올 시 dp에 넣을지 생각

import heapq


def solution(alp, cop, problems):
    result = []

    check_alp, check_cop = 0, 0

    count = 0

    for a, c, algorism, coding, time in problems:
        check_alp = max(a, check_alp)
        check_cop = max(c, check_cop)
        count += time

    if alp >= check_alp and cop >= check_cop:
        return 0

    elif alp >= check_alp and cop < check_cop:
        dp = dp = [[float("inf"), [alp, cop]]] * (check_cop - cop + 1)
        dp[0][0] = check_cop - cop

    elif alp < check_alp and cop >= check_cop:
        dp = dp = [[float("inf"), [alp, cop]]] * (check_alp - cop + 1)
        dp[0][0] = check_alp - cop

    else:
        dp = [[float("inf"), [alp, cop]]] * (check_alp - alp + check_cop - cop + 1)
        dp[0][0] = check_alp - alp + check_cop - cop

    # 최대 시간이 dp 길이 while True로 할 시 3중 for문으로 시간복잡도 급격히 증가

    #     for i in range(len(dp)):

    #         for a,b,c,d,t in problems:
    #             if dp[i][1][0]>=a and dp[i][1][1]>=b:
    #                 # 해당 문제를 풀 시 진행되는 시간 i+t

    #                 # 효율 알고리즘
    #                 if dp[i][1][0]+a >=check_alp and dp[i][1]< check_alp:
    #                     # 한계치로 인한 효율 감소
    #                     one=check_alp-dp[i][1][0]

    #                 elif dp[i][1][0]+a < check_alp:
    #                     one=a
    #                 else:
    #                     one=0

    #                 # 효율 코딩력
    #                 if dp[i][1][1]+b >=check_cop and dp[i][1]< check_cop:
    #                     # 한계치로 인한 효율 감소
    #                     two=check_cop-dp[i][1][1]

    #                 elif dp[i][1][0]+a < check_alp:
    #                     two=b

    #                 else:
    #                     two=0

    # 시간+1인 순간도 비교

    return 0

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
