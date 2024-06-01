"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/86053
"""
# 내 풀이(개선 중)
"""
조건: 
새 도시를 만들 조건: 금:a 은:b

이해 과정:i번 도시에는 일정 이상의 광물이 있고, 새 도시에 광물을 전달해준다

목표:새로운 도시를 건설하기 위한 최단 시간을 구하시오
"""

"""

# 필요한 금:a 은:b 
g[i]:i번 도시에 보유한 금
s[i]:i번 도시에 보유한 은

신도시까지 이동시간: t[i] 옮길 수 있는 최대 양 w[i]

"""


# 생각 방향: 각 도시에 일정량을 가져오는 경우를 모두 산정 후 그 중 누적 후 시간이 최소인것을 구한다.
# 시간 빠른 순으로 트럭을 돌려보내고 받고를 한 후 금과 은 중에 더 많은 광석을 먼저 소비하는 방식으로 한 후 다시 heap 리스트에 추가!
# 각 시간을 늘려가면서 최대 금,최소 은 ,최대 은 ,최소 금의 범위를 산정 후 접근 후 해당 범위 내에 조건 달성 시 정답 달성

def solution(a, b, g, s, w, t):
    k = a + b

    city = len(g)
    check = []

    #     for k in range(city):
    #         c=(s[k]+g[k])//w[k]

    #         if c==0:
    #             check.append(1)
    #         else:
    #             check.append(c*2+1)

    time = 0

    while True:
        gold_max = 0
        silver_max = 0
        # 누적 무게
        weight = 0

        for i in range(city):
            if time >= t[i]:
                n = time // t[i]

                # 왕복
                if n % 2 == 0:
                    check = w[i] * (n // 2)

                    # 최대양보다 많을 경우
                    if check >= g[i] + s[i]:
                        weight += g[i] + s[i]
                        silver_max += s[i]
                        gold_max += g[i]
                    else:
                        weight += check

                        if check >= g[i]:
                            gold_max += g[i]

                        else:
                            gold_max += check

                        if check >= s[i]:
                            silver_max += s[i]

                        else:
                            silver_max += check

                # 왕복+편도
                else:
                    check = w[i] * ((n // 2) + 1)

                    # 최대양보다 많을 경우
                    if check >= g[i] + s[i]:
                        weight += g[i] + s[i]
                        silver_max += s[i]
                        gold_max += g[i]

                    else:
                        weight += check

                        if check >= g[i]:
                            gold_max += g[i]

                        else:
                            gold_max += check

                        if check >= s[i]:
                            silver_max += s[i]

                        else:
                            silver_max += check

        if weight >= a + b and gold_max >= a and silver_max >= b:
            return time

        time += 1

    return 0

# 내 풀이(개선 중)
"""
조건: 
새 도시를 만들 조건: 금:a 은:b

이해 과정:i번 도시에는 일정 이상의 광물이 있고, 새 도시에 광물을 전달해준다

목표:새로운 도시를 건설하기 위한 최단 시간을 구하시오
"""

"""

# 필요한 금:a 은:b 
g[i]:i번 도시에 보유한 금
s[i]:i번 도시에 보유한 은

신도시까지 이동시간: t[i] 옮길 수 있는 최대 양 w[i]

"""


# 생각 방향: 각 도시에 일정량을 가져오는 경우를 모두 산정 후 그 중 누적 후 시간이 최소인것을 구한다.
# 시간 빠른 순으로 트럭을 돌려보내고 받고를 한 후 금과 은 중에 더 많은 광석을 먼저 소비하는 방식으로 한 후 다시 heap 리스트에 추가!
# 각 시간을 늘려가면서 최대 금,최소 은 ,최대 은 ,최소 금의 범위를 산정 후 접근 후 해당 범위 내에 조건 달성 시 정답 달성

def solution(a, b, g, s, w, t):
    k = a + b

    city = len(g)
    check = []
    for k in range(city):
        c = (s[k] + g[k]) // w[k]

        if c == 0:
            check.append(1)
        else:
            check.append(c * 2 + 1)

    time = max(check)

    while True:
        gold_max, gold_min = 0, 0
        silver_max, silver_min = 0, 0
        # 누적 무게
        weight = 0

        for i in range(city):
            if time >= t[i]:
                n = time // t[i]

                # 왕복
                if n % 2 == 0:
                    check = w[i] * (n // 2)

                    # 최대양보다 많을 경우
                    if check >= g[i] + s[i]:
                        weight += g[i] + s[i]
                        silver_max += s[i]
                        silver_min += s[i]
                        gold_max += g[i]
                        gold_min += g[i]
                    else:
                        weight += check

                        if check >= g[i]:
                            gold_max += g[i]

                            if check - g[i] >= s[i]:
                                silver_min += s[i]
                            else:
                                silver_min += s[i] - (check - g[i])
                        else:
                            gold_max += check

                        if check >= s[i]:
                            silver_max += s[i]

                            if check - s[i] >= g[i]:
                                gold_min += g[i]
                            else:
                                gold_min += g[i] - (check - s[i])
                        else:
                            silver_max += check

                # 왕복+편도
                else:
                    check = w[i] * ((n // 2) + 1)

                    # 최대양보다 많을 경우
                    if check >= g[i] + s[i]:
                        weight += g[i] + s[i]
                        silver_max += s[i]
                        gold_max += g[i]

                    else:
                        weight += check

                        if check >= g[i]:
                            gold_max += g[i]

                            if check - g[i] >= s[i]:
                                silver_min += s[i]
                            else:
                                silver_min += s[i] - (check - g[i])

                        else:
                            gold_max += check

                        if check >= s[i]:
                            silver_max += s[i]

                            if check - s[i] >= g[i]:
                                gold_min += g[i]
                            else:
                                gold_min += g[i] - (check - s[i])

                        else:
                            silver_max += check

        print(gold_max, gold_min, silver_max, silver_min)

        if weight >= a + b and gold_max >= a and silver_min >= b:
            time -= 1

        elif weight >= a + b and silver_max >= b and gold_min >= a:
            time -= 1

        else:
            return time + 1

    return 0

# 내 풀이(개선 중)

"""
조건: 
새 도시를 만들 조건: 금:a 은:b

이해 과정:i번 도시에는 일정 이상의 광물이 있고, 새 도시에 광물을 전달해준다

목표:새로운 도시를 건설하기 위한 최단 시간을 구하시오
"""

"""

# 필요한 금:a 은:b 
g[i]:i번 도시에 보유한 금
s[i]:i번 도시에 보유한 은

신도시까지 이동시간: t[i] 옮길 수 있는 최대 양 w[i]

"""
# 내 풀이(개선 중)
"""
조건: 
새 도시를 만들 조건: 금:a 은:b

이해 과정:i번 도시에는 일정 이상의 광물이 있고, 새 도시에 광물을 전달해준다

목표:새로운 도시를 건설하기 위한 최단 시간을 구하시오
"""

"""

# 필요한 금:a 은:b 
g[i]:i번 도시에 보유한 금
s[i]:i번 도시에 보유한 은

신도시까지 이동시간: t[i] 옮길 수 있는 최대 양 w[i]

"""


# 생각 방향: 각 도시에 일정량을 가져오는 경우를 모두 산정 후 그 중 누적 후 시간이 최소인것을 구한다.
# 시간 빠른 순으로 트럭을 돌려보내고 받고를 한 후 금과 은 중에 더 많은 광석을 먼저 소비하는 방식으로 한 후 다시 heap 리스트에 추가!
# 각 시간을 늘려가면서 최대 금,최소 은 ,최대 은 ,최소 금의 범위를 산정 후 접근 후 해당 범위 내에 조건 달성 시 정답 달성

def solution(a, b, g, s, w, t):
    k = a + b

    city = len(g)

    time = min(t)

    while True:
        gold_max = 0
        silver_max = 0
        # 누적 무게
        weight = 0

        for i in range(city):
            if time >= t[i]:
                n = time // t[i]

                # 왕복 불가
                if n % 2 == 0:
                    check = w[i] * (n // 2)

                    # 최대양보다 많을 경우
                    if check >= g[i] + s[i]:
                        weight += g[i] + s[i]
                        silver_max += s[i]
                        gold_max += g[i]
                    else:
                        weight += check

                        if check >= g[i]:
                            gold_max += g[i]
                        if check >= s[i]:
                            silver_max += s[i]

                # 왕복+편도
                else:
                    check = w[i] * ((n // 2) + 1)

                    # 최대양보다 많을 경우
                    if check >= g[i] + s[i]:
                        weight += g[i] + s[i]
                        silver_max += s[i]
                        gold_max += g[i]

                    else:
                        weight += check

                        if check >= g[i]:
                            gold_max += g[i]
                        else:
                            gold_max += check

                        if check >= s[i]:
                            silver_max += s[i]
                        else:
                            silver_max += check

        if weight >= a + b and gold_max >= a and silver_max >= b:
            return time

        time += 1

    return 0

# 생각 방향: 각 도시에 일정량을 가져오는 경우를 모두 산정 후 그 중 누적 후 시간이 최소인것을 구한다.
# 시간 빠른 순으로 트럭을 돌려보내고 받고를 한 후 금과 은 중에 더 많은 광석을 먼저 소비하는 방식으로 한 후 다시 heap 리스트에 추가!

import heapq


def solution(a, b, g, s, w, t):
    k = a + b

    truck = []

    city = len(g)

    for i in range(city):
        heapq.heappush(truck, (t[i], w[i], i))

    count = 0

    while truck:
        time = heapq.heappop(truck)

        count += 1
        break

    return 0