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
# 효율이 떨어져도 검증해야될 필요성 느낌: 문제 푸는데 최소한의 역량 확보와 효율과 차이가 날 수 있음

import heapq

def solution(alp, cop, problems):
    # 목표 역량
    algorism, coding = 0, 0

    for a, c, algo, code, time in problems:
        algorism = max(a, algorism)
        coding = max(c, coding)

    # dp를 활용하기 위한 최대 시간 계산
    if alp >= algorism:
        plus_alp = 0
    else:
        plus_alp = algorism - alp

    if cop >= coding:
        plus_cop = 0
    else:
        plus_cop = coding - cop

    max_time = plus_alp + plus_cop
    dp = [[] for _ in range(plus_alp + plus_cop + 1)]

    # 이미 충족된 경우
    if len(dp) == 0:
        return 0

    dp[0].append([alp, cop])

    # i 경과 시간
    for i in range(len(dp)):

        for al, co in dp[i]:
            if al >= algorism and co >= coding:
                return i

            for a, c, algo, code, time in problems:
                # 문제 풀이가 가능할 때
                if al >= a and co >= c and i + time <= max_time and algo + code >= time:
                    if al + algo >= algorism:
                        if al >= algorism:
                            x = 0
                        else:
                            x = algorism - al
                    else:
                        x = algo

                    if co + code >= coding:
                        if co >= coding:
                            y = 0
                        else:
                            y = coding - co
                    else:
                        y = code

                    if x + y > time:
                        dp[i + time].append([al + algo, co + code])

            if i + 1 <= max_time:
                if al + 1 <= algorism:
                    dp[i + 1].append([al + 1, co])
                if co + 1 <= coding:
                    dp[i + 1].append([al, co + 1])
        new = []

    #         # 등수 매기기 문제랑 비슷한 방식으로 dp 내부 리스트를 추려야한다!
    #         if i+1<=max_time:
    #             check=float("inf")

    #             dp[i+1]=[]
    #             dp[i+1]+=new

    return 0
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
# 효율이 떨어져도 검증해야될 필요성 느낌: 문제 푸는데 최소한의 역량 확보와 효율과 차이가 날 수 있음

import heapq


def solution(alp, cop, problems):
    # 목표 역량
    algorism, coding = 0, 0

    for a, c, algo, code, time in problems:
        algorism = max(a, algorism)
        coding = max(c, coding)

    # dp를 활용하기 위한 최대 시간 계산
    if alp >= algorism:
        plus_alp = 0
    else:
        plus_alp = algorism - alp

    if cop >= coding:
        plus_cop = 0
    else:
        plus_cop = coding - cop

    max_time = plus_alp + plus_cop
    dp = [[] for _ in range(plus_alp + plus_cop + 1)]

    # 이미 충족된 경우
    if len(dp) == 0:
        return 0

    dp[0].append([alp, cop])

    # i 경과 시간
    for i in range(len(dp)):

        for al, co in dp[i]:
            if al >= algorism and co >= coding:
                return i

            for a, c, algo, code, time in problems:

                if al >= a and co >= c and i + time <= max_time and algo + code >= time:

                    if al >= algorism and co < coding and code < time:
                        continue
                    elif co >= coding and al < algorism and algo < time:
                        continue
                    else:
                        dp[i + time].append([al + algo, co + code])

            if i + 1 <= max_time:
                dp[i + 1].append([al + 1, co])
                dp[i + 1].append([al, co + 1])

        new = []

        if i + 1 <= max_time:
            num = float("inf")

            for v, w, in dp[i + 1]:

                if v < algorism and w < coding:
                    one = algorism - v
                    two = coding - w

                elif v < algorism and w >= coding:
                    one = algorism - v
                    two = 0

                elif v >= algorism and w < coding:
                    one = 0
                    two = coding - w

                if one + two < num:
                    num = one + two
                    new = []
                    new.append([v, w])

                elif one + two == num:

                    if not [v, w] in new:
                        new.append([v, w])

            dp[i + 1] = []
            dp[i + 1] += new

    return 0

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
# 효율이 떨어져도 검증해야될 필요성 느낌: 문제 푸는데 최소한의 역량 확보와 효율과 차이가 날 수 있음

import heapq


def solution(alp, cop, problems):
    # 목표 역량
    algorism, coding = 0, 0

    for a, c, algo, code, time in problems:
        algorism = max(a, algorism)
        coding = max(c, coding)

    # dp를 활용하기 위한 최대 시간 계산
    if alp >= algorism:
        plus_alp = 0
    else:
        plus_alp = algorism - alp

    if cop >= coding:
        plus_cop = 0
    else:
        plus_cop = coding - cop

    max_time = plus_alp + plus_cop
    dp = [[] for _ in range(plus_alp + plus_cop + 1)]

    # 이미 충족된 경우
    if len(dp) == 0:
        return 0

    dp[0].append([alp, cop])

    # i 경과 시간
    for i in range(len(dp)):

        for al, co in dp[i]:
            if al >= algorism and co >= coding:
                return i

            for a, c, algo, code, time in problems:

                if al >= a and co >= c and i + time <= max_time and algo + code >= time:

                    if al >= algorism and co < coding and code < time:
                        continue
                    elif co >= coding and al < algorism and algo < time:
                        continue
                    else:
                        dp[i + time].append([al + algo, co + code])

            dp[i + 1].append([al + 1, co])
            dp[i + 1].append([al, co + 1])

        new = []

        for v, w, in dp[i + 1]:
            for x, y in dp[i + 1]:
                if v < x and w < y:
                    break
            else:
                if not [v, w] in new:
                    new.append([v, w])

        dp[i + 1] = []
        dp[i + 1] += new

    return 0

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
# 효율이 떨어져도 검증해야될 필요성 느낌: 문제 푸는데 최소한의 역량 확보와 효율과 차이가 날 수 있음

import heapq

def solution(alp, cop, problems):

    # 목표 역량
    algorism,coding=0,0

    for a,c,algo,code,time in problems:
        algorism=max(a,algorism)
        coding=max(c,coding)


    # dp를 활용하기 위한 최대 시간 계산
    if alp>=algorism:
        plus_alp=0
    else:
        plus_alp=algorism-alp

    if cop>=coding:
        plus_cop=0
    else:
        plus_cop=coding-cop

    max_time=plus_alp+plus_cop
#     dp=[[] for _ in range(plus_alp+plus_cop+1)]

#     # 이미 충족된 경우
#     if len(dp)==0:
#         return 0

#     dp[0].append([alp,cop])

    dp=[[0,alp,cop]]

    result=[]

    while dp:
        time,al,co = heapq.heappop(dp)

        if al>=algorism and co>=coding:
            if len(result)==0:
                check_time=time
            else:
                if check_time<time:
                    break
                else:
                    result.append(time)

        for a,c,algo,code,t in problems:

            # 문제 풀이 가능 및 최대 시간 초과 x 및
            if al>=a and co>=c and t+time<=max_time and algo+code > time:

                # 한 쪽 충족 및 효율 기준치 미달
                if al>=algorism and code<time:
                    continue
                elif co>=coding and algo<time:
                    continue

                else:
                    heapq.heappush(dp,[t+time,al+algo,co+code])

        if not [time+1,al+1,co] in dp:
            heapq.heappush(dp,[time+1,al+1,co])

        if not [time+1,al,co+1] in dp:
            heapq.heappush(dp,[time+1,al,co+1])


        print(dp)
        break

    return 0

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
# 효율이 떨어져도 검증해야될 필요성 느낌: 문제 푸는데 최소한의 역량 확보와 효율과 차이가 날 수 있음

import heapq

def solution(alp, cop, problems):
    check_alp, check_cop = 0, 0
    min_alp, min_cop = float("inf"), float("inf")

    for a, c, algorism, coding, time in problems:
        check_alp = max(a, check_alp)
        check_cop = max(c, check_cop)
        min_alp = min(a, min_alp)
        min_cop = min(c, min_cop)

    if min_alp >= alp:
        t_a = min_alp - alp
    else:
        t_a = 0
    if min_cop >= cop:
        t_b = min_cop - cop
    else:
        t_b = 0

    if alp >= check_alp and cop >= check_cop:
        return 0

    elif alp >= check_alp and cop < check_cop:
        dp = [[] for _ in range(check_cop - cop + 1)]

    elif alp < check_alp and cop >= check_cop:
        dp = [[] for _ in range(check_alp - alp + 1)]

    else:
        dp = [[] for _ in range(check_alp - alp + check_cop - cop + 1)]

    # dp[0].append([alp,cop])

    problems.sort()

    dp[t_a + t_b].append([alp + t_a, cop + t_b])

    # 최대 시간이 dp 길이 while True로 할 시 3중 for문으로 시간복잡도 급격히 증가

    for i in range(t_a + t_b, len(dp)):

        # dp 효율 정리
        new = []

        # dp[i] 정리 및 중복제거
        for x in dp[i]:
            for y in dp[i]:
                if x != y:
                    if x[0] <= y[0] and x[1] <= y[1]:
                        break

            else:
                if not [x[0], x[1]] in new:
                    new.append([x[0], x[1]])

        dp[i] = []
        dp[i] += new

        for v, w in dp[i]:
            if v >= check_alp and w >= check_cop:
                return i

            for a, b, c, d, t in problems:

                # 문제 풀이 가능
                if v >= a and w >= b and t + i < len(dp):
                    if v > check_alp and d < t:
                        continue
                    elif w > check_cop and c < t:
                        continue

                    # if not [v+c,w+d] in dp[t+i] and not c+d < t:
                    # # 해당 문제를 풀 시 진행되는 시간 i+t
                    #     dp[t+i].append([v+c,w+d])

                    elif d + c < t:
                        continue

                    dp[t + i].append([v + c, w + d])

                elif v < a:
                    break

            if t + 1 < len(dp):
                if not [v + 1, w] in dp[i + 1]:
                    dp[i + 1].append([v + 1, w])

                if not [v, w + 1] in dp[i + 1]:
                    dp[i + 1].append([v, w + 1])

            # dp[i+1].append([v+1,w])
            # dp[i+1].append([v,w+1])

    return 0

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
# 효율이 떨어져도 검증해야될 필요성 느낌: 문제 푸는데 최소한의 역량 확보와 효율과 차이가 날 수 있음

import heapq


def solution(alp, cop, problems):
    check_alp, check_cop = 0, 0

    for a, c, algorism, coding, time in problems:
        check_alp = max(a, check_alp)
        check_cop = max(c, check_cop)

    if alp >= check_alp and cop >= check_cop:
        return 0

    elif alp >= check_alp and cop < check_cop:
        dp = [[] for _ in range(check_cop - cop + 1)]

    elif alp < check_alp and cop >= check_cop:
        dp = [[] for _ in range(check_alp - alp + 1)]

    else:
        dp = [[] for _ in range(check_alp - alp + check_cop - cop + 1)]

    dp[0].append([alp, cop])

    # 최대 시간이 dp 길이 while True로 할 시 3중 for문으로 시간복잡도 급격히 증가

    for i in range(len(dp)):

        # dp 효율 정리
        new = []

        # dp[i] 정리
        for x in dp[i]:
            for y in dp[i]:
                if x != y:
                    if x[0] < y[0] and x[1] < y[1]:
                        break

            else:
                if not [x[0], x[1]] in new:
                    new.append([x[0], x[1]])

        dp[i] = []
        dp[i] += new

        for v, w in dp[i]:
            if v >= check_alp and w >= check_cop:
                return i

            for a, b, c, d, t in problems:

                # 문제 풀이 가능
                if v >= a and w >= b and t + i < len(dp):
                    if v > check_alp and d < t:
                        continue
                    elif w > check_cop and c < t:
                        continue

                    if not [v + c, w + d] in dp[t + i] and not c + d < t:
                        # 해당 문제를 풀 시 진행되는 시간 i+t
                        dp[t + i].append([v + c, w + d])

            if t + 1 < len(dp):
                if not [v + 1, w] in dp[i + 1]:
                    dp[i + 1].append([v + 1, w])

                if not [v, w + 1] in dp[i + 1]:
                    dp[i + 1].append([v, w + 1])

    return 0

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
