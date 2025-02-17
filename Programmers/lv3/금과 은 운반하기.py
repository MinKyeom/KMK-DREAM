"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/86053
"""
# 풀이 과정
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
# 시간을 1씩 올려서 혹은 내려서 접근하는 방식은 많은 시간을 소요해 시간초과로 이어진다
# 이분탐색(이진탐색)을 바탕으로 접근해야 한다

import heapq


def solution(a, b, g, s, w, t):
    start = 0
    end = (10 ** 9) * (10 ** 5) * 4

    result = (10 ** 9) * (10 ** 5) * 4

    # 도시 개수
    city = len(g)

    while start <= end:

        gold_max, gold_min = 0, 0
        silver_max, silver_min = 0, 0
        weight = 0
        mid = (start + end) // 2

        for k in range(city):

            # 편도 횟수
            count = mid // t[k]

            # 왕복만 가능
            if count % 2 == 0:
                check = (count // 2) * w[k]

                if check >= s[k] + g[k]:
                    check = s[k] + g[k]
                    weight += check
                    silver_max += s[k]
                    silver_min += s[k]
                    gold_max += g[k]
                    gold_min += g[k]

                else:
                    weight += check
                    if check >= s[k]:
                        silver_max += s[k]
                        gold_min += check - s[k]

                    # 실버만 채워야함
                    else:
                        silver_max += check

                    if check >= g[k]:
                        gold_max += g[k]
                        silver_min += check - g[k]
                    else:
                        gold_max += check

            # 마지막 편도 한 번까지 가능
            else:
                check = ((count // 2) + 1) * w[k]

                if check >= s[k] + g[k]:
                    check = s[k] + g[k]
                    weight += check
                    silver_max += s[k]
                    silver_min += s[k]
                    gold_max += g[k]
                    gold_min += g[k]

                else:
                    weight += check
                    if check >= s[k]:
                        silver_max += s[k]
                        gold_min += check - s[k]

                    # 실버만 채워야함
                    else:
                        silver_max += check

                    if check >= g[k]:
                        gold_max += g[k]
                        silver_min += check - g[k]
                    else:
                        gold_max += check

        if weight >= a + b and gold_max >= a and silver_max >= b:
            result = min(result, mid)
            end = mid - 1

            # num=silver_max

        #             for i in range(gold_min,gold_max+1):
        #                 if i >=a and num>=b:
        #                     break
        #                 else:
        #                     num-=1
        #             else:
        #                 start=mid+1
        #                 continue

        #             result=min(result,mid)
        #             end=mid-1

        else:
            start = mid + 1

    return result

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


# 다른 사람 풀이

def solution(a, b, g, s, w, t):
    start = 0
    # 최악의 경우
    # 광물의 최대무게 : 10**9 * 2(금,은)
    # 도시가 1개만 있고 소요시간이 최대, 1씩 옮길 수 있을 때 : 10**5 * 2(왕복)
    answer = end = (10 ** 9) * (10 ** 5) * 4

    # 이진 탐색
    while start <= end:
        mid = (start + end) // 2
        gold = 0
        silver = 0
        total = 0

        for i in range(len(g)):
            # 현재 정보
            now_gold = g[i]
            now_silver = s[i]
            now_weight = w[i]
            now_time = t[i]

            # 주어진 시간내에서 이동할 수 있는 횟수 (왕복으로 계산)
            move_cnt = mid // (now_time * 2)

            # 편도 추가
            if mid % (now_time * 2) >= now_time:
                move_cnt += 1

            # 주어지 시간 내 최대 적재 가능량 누적하기
            possible_move_weight = move_cnt * now_weight
            gold += now_gold if (now_gold < possible_move_weight) else possible_move_weight
            silver += now_silver if (now_silver < possible_move_weight) else possible_move_weight
            total += now_gold + now_silver if (now_gold + now_silver < possible_move_weight) else possible_move_weight

        # total이 a+b 보다 크거나 같으면서 금과 은의 누적 최대값이 a와 b보다 크거나 같아야 한다.
        # 만약 금과 은의 누적 최대값이 보내야만 하는 a,b보다 작다면 현재 시간 내 처리 불가능하다.
        if total >= a + b and gold >= a and silver >= b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1
    return answer