"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/214289
"""
# 풀이 과정
def solution(temperature, t1, t2, a, b, onboard):
    t = temperature
    p = onboard

    max_t, min_t = t2, t1

    dp = [[1e9] * 51 for _ in range(1001)]

    dp[0][t + 10] = 0

    count = sum(p)

    for i in range(1, len(onboard)):  # i 시간
        if p[i] == 1:
            start = t1
            end = t2 + 1
        else:
            start = -10
            end = 40 + 1

        for j in range(start, end):
            if j == t:
                check = [dp[i - 1][j + 10]]

                if j + 10 != 0:
                    check.append(dp[i - 1][j - 1 + 10])
                if j + 10 != 50:
                    check.append(dp[i - 1][j + 1 + 10])

                dp[i][j + 10] = min(check)

            elif j > t:
                check = [dp[i - 1][j + 10] + b]

                if j + 10 != 0:
                    check.append(dp[i - 1][j + 10 - 1] + a)
                if j + 10 != 50:
                    check.append(dp[i - 1][j + 10 + 1])

                dp[i][j + 10] = min(check)


            else:
                check = [dp[i - 1][j + 10] + b]

                if j + 10 != 0:
                    check.append(dp[i - 1][j + 10 - 1])
                if j + 10 != 50:
                    check.append(dp[i - 1][j + 10 + 1] + a)

                dp[i][j + 10] = min(check)

        if p[i] == 1:
            count -= 1
            if count == 0:
                last = i
                return min(dp[last])

                # return min(dp[len(p)-1])


"""
def solution(temperature, t1, t2, a, b, onboard):
    mintemp, maxtemp = t1, t2

    # dp[temp][t] = 시간 t에 실내온도가 (temp+10)도인
    # 상황을 만드는 최소 소비 전력
    dp = [[1e9] * 51 for _ in range(1001)]

    # 초기화 (t=0)
    dp[0][temperature + 10] = 0

    for t, is_onboard in enumerate(onboard[1:], 1):
        print(t,is_onboard)
        # 승객이 탑승한 상황에서는 오직 mintemp <= temp <= maxtemp
        # 인 경우만 고려하면 된다.
        if is_onboard:
            mintemp_to_consider = mintemp
            maxtemp_to_consider = maxtemp + 1
        else:
            mintemp_to_consider = -10
            maxtemp_to_consider = 40 + 1

        for temp in range(mintemp_to_consider, maxtemp_to_consider):
            if temp == temperature:
                candidates = [dp[t - 1][temp + 10]]
                if temp + 10 != 0:
                    candidates.append(dp[t - 1][temp - 1 + 10])
                if temp + 10 != 50:
                    candidates.append(dp[t - 1][temp + 1 + 10])

                dp[t][temp + 10] = min(candidates)

            elif temp > temperature:
                candidates = [dp[t - 1][temp + 10] + b]
                if temp + 10 != 0:
                    candidates.append(dp[t - 1][temp - 1 + 10] + a)
                if temp + 10 != 50:
                    candidates.append(dp[t - 1][temp + 1 + 10])

                dp[t][temp + 10] = min(candidates)
            else:
                candidates = [dp[t - 1][temp + 10] + b]
                if temp + 10 != 0:
                    candidates.append(dp[t - 1][temp - 1 + 10])
                if temp + 10 != 50:
                    candidates.append(dp[t - 1][temp + 1 + 10] + a)

                dp[t][temp + 10] = min(candidates)

    answer = min(dp[len(onboard) - 1])
    return answer
    """
# 내 풀이(개선 중)
def solution(temperature, t1, t2, a, b, onboard):
    t = temperature  # 현재 온도
    p = onboard  # 승객 탑승 여부
    start = max(t - t2, t1 - t)
    check = start  # 처음 기온차
    result = 0  # 전력량
    num = sum(p)

    for i in range(len(p)):
        if p[i] == 1:
            if start == 0:
                if num > 1 and p[i + 1] != 1:
                    if b + b > a:
                        start += 1
                    else:
                        result += b
                elif num > 1 and p[i + 1] == 1:
                    result += b
            num -= 1

        else:  # 승객 탑승 x
            if start > 1:
                result += a
                start -= 1
            elif start == 1 and check != 1 and p[i + 1] != 1:
                if b + b > a:
                    start -= 1
                    result += a
                else:
                    result += b

            elif start == 1 and p[i + 1] == 1:
                start -= 1
                result += a

            elif start == 0 and p[i + 1] != 1:
                if b + b > a:
                    start += 1
                else:
                    result += b
            elif start == 0 and p[i + 1] == 1:
                result += b

        print(result, start, p[i])

        if num == 0:
            return result
# 내 풀이(개선 중)
from collections import deque


def solution(temperature, t1, t2, a, b, onboard):
    result = float("inf")  # 전력소모량
    p = onboard  # 승객 탑승 여부
    t = temperature  # temperature: 실외온도
    now = temperature  # 현재기온
    s = sum(onboard)
    o = []
    for x in range(len(p)):
        if p[x] == 1:
            o.append(x)

    # want: 희망온도 off: 전원 temperature: 시간에 따른 온도
    check = [[now, temperature, "off"] for _ in range(len(p))]  # 시간에 따른 에어컨 전원 및 온도 변경여부 0,1,-1

    #### 목표 ####
    # 승객이 탑승중일때 최적화된 실내 온도를 최소의 전력으로 맞추기
    # 승객이 탑승할때도 에어컨이 켜져있다면 외부 온도와 관계없이 에어컨의 조건에 따른다!
    # 사이인거 등호 포함!
    # 더 더울경우 t2 추울경우 t1
    # 탑승객이 없을경우 최적화를 맞출 필요가 없다 그래야 최소 전력 가능!
    # 변화가 생기기 직전에 에어컨 on
    #################################

    # 기준점 t: 현재 온도

    ####
    # 온도를 선택하는 방법 중 전력이 최소로 드는걸 선택
    # [현재온도, 전력]으로 이루어진 리스트를 활용하여 체크
    # 최근 고객이 탈 때까지 최적한 온도를 맞출 수 있는 지 여부 확인 실외온도를 채택할경우

    count = 0
    # [현재기온,전력,시간,남은 승객 수]
    q = deque([[now, 0, 0, s]])
    result = float("inf")

    while q:
        c, e, time, x = q.pop()
        new = []
        new_x = x
        # 최적화 온도 여부 체크
        if not t1 <= c <= t2 and p[time] == 1:
            continue
        elif t1 <= c <= t2 and p[time] == 1:
            new_x = x - 1

        if e >= result:
            continue

        if time == len(p) - 1 or x == 0:
            if e < result:
                result = e
            continue

        # 에어컨 off 경우 실외 온도와 동일하게
        if c == t and c > t2 and c - (time + 1 - o[s - x]) <= t2:
            q.append([c, e, time + 1, new_x])
            # new.append([c,e,time+1,x])
        elif c == t and c < t1 and c + (time + 1 - o[s - x]) >= t1:
            q.append([c, e, time + 1, new_x])
            # new.append([c,e,time+1,x])
        elif c > t and c + (time + 1 - o[s - x]) - 1 >= t1:
            q.append([c - 1, e, time + 1, new_x])
            # new.append([c-1,e,time+1,x])
        elif c < t and c - (time + 1 - o[s - x]) + 1 <= t2:
            q.append([c + 1, e, time + 1, new_x])
            # new.append([c+1,e,time+1,x])

        # 에어컨 on 경우 변동
        if c > t2:
            q.append([c - 1, e + a, time + 1, new_x])
            # new.append([c-1,e+a,time+1,x])
        elif c < t1:
            q.append([c + 1, e + a, time + 1, new_x])
            # new.append([c+1,e+a,time+1,x])
        elif t1 <= c <= t2:
            q.append([c, e + b, time + 1, new_x])
            # new.append([c,e+b,time+1,x])
            if abs(t2 - c) >= abs(c - t1):
                q.append([c + 1, e + a, time + 1, new_x])
                # new.append([c+1,e+a,time+1,x])
            elif abs(t2 - c) < abs(c - t1):
                q.append([c - 1, e + a, time + 1, new_x])
                # new.append([c-1,e+a,time+1,x])

        # new=sorted(new, key=lambda x:x[1])

    return result
# 내 풀이(개선 중)
from collections import deque


def solution(temperature, t1, t2, a, b, onboard):
    result = 0  # 전력소모량
    p = onboard  # 승객 탑승 여부
    t = temperature  # temperature: 실외온도
    now = temperature  # 현재기온
    # want: 희망온도 off: 전원 temperature: 시간에 따른 온도
    check = [[now, temperature, "off"] for _ in range(len(p))]  # 시간에 따른 에어컨 전원 및 온도 변경여부 0,1,-1

    #### 목표 ####
    # 승객이 탑승중일때 최적화된 실내 온도를 최소의 전력으로 맞추기
    # 승객이 탑승할때도 에어컨이 켜져있다면 외부 온도와 관계없이 에어컨의 조건에 따른다!
    # 사이인거 등호 포함!
    # 더 더울경우 t2 추울경우 t1
    # 탑승객이 없을경우 최적화를 맞출 필요가 없다 그래야 최소 전력 가능!
    # 변화가 생기기 직전에 에어컨 on
    #################################

    # 기준점 t: 현재 온도

    ####
    # 온도를 선택하는 방법 중 전력이 최소로 드는걸 선택
    # [현재온도, 전력]으로 이루어진 리스트를 활용하여 체크

    count = 0
    # [현재기온,전력,시간]
    q = deque([[now, 0, 0]])
    result = []

    while q:
        c, e, time = q.popleft()

        # 최적화 온도 여부 체크
        if not t1 <= c <= t2 and p[time] == 1:
            continue

        if time == len(p) - 1:
            result.append(e)
            continue

        # 에어컨 off 경우
        if c == t:
            q.append([c, e, time + 1])
        elif c > t:
            q.append([c - 1, e, time + 1])
        elif c < t:
            q.append([c + 1, e, time + 1])

        # 에어컨 on 경우 변동
        if c > t2:
            q.append([c - 1, e + a, time + 1])
        elif c < t1:
            q.append([c + 1, e + a, time + 1])
        elif t1 <= c <= t2:
            q.append([c, e + b, time + 1])
            q.append([c + 1, e + a, time + 1])
            q.append([c - 1, e + a, time + 1])

    return min(result)


# 내 풀이(개선 중)
def solution(temperature, t1, t2, a, b, onboard):
    result = 0  # 전력소모량
    p = onboard  # 승객 탑승 여부
    t = temperature  # 현재온도 #temperature: 실외온도

    # want: 희망온도 off: 전원 temperature: 시간에 따른 온도
    check = [[temperature, temperature, "off"] for _ in range(len(p))]  # 시간에 따른 에어컨 전원 및 온도 변경여부 0,1,-1

    print(check, "before")

    #### 목표 ####
    # 승객이 탑승중일때 최적화된 실내 온도를 최소의 전력으로 맞추기
    # 승객이 탑승할때도 에어컨이 켜져있다면 외부 온도와 관계없이 에어컨의 조건에 따른다!
    # 사이인거 등호 포함!
    # 더 더울경우 t2 추울경우 t1
    # 탑승객이 없을경우 최적화를 맞출 필요가 없다 그래야 최소 전력 가능!
    #################################

    # 기준점 t: 현재 온도
    while True:

        for k in range(len(p)):
            if p[k] == 1:
                if not t1 <= check[k][0] <= t2:
                    before = check[k][0]

                    if check[k][0] > t2:
                        check[k][0] = t2

                        for i in range(k - 1, -1, -1):
                            check[i][0] = check[i + 1][0] + 1
                            check[i][1] = t2
                            check[i][2] = "on"
                            if check[i][0] == before:
                                break
                    else:
                        check[k][0] = t1
                        for i in range(k - 1, -1, -1):
                            check[i][0] = check[i + 1][0] - 1
                            check[i][1] = t1
                            check[i][2] = "on"
                            if check[i][0] == before:
                                break

                else:
                    pass

                print(check)

        # 시간 경과에 따른 통과 했을 경우
        else:
            break

    # result 최적화 후 나중에 한 번 더 계산! think

    return result

# 다른 사람 풀이
def solution(temperature, t1, t2, a, b, onboard):
    mintemp, maxtemp = t1, t2

    # dp[temp][t] = 시간 t에 실내온도가 (temp+10)도인
    # 상황을 만드는 최소 소비 전력
    dp = [[1e9] * 51 for _ in range(1001)]

    # 초기화 (t=0)
    dp[0][temperature + 10] = 0

    for t, is_onboard in enumerate(onboard[1:], 1):
        # 승객이 탑승한 상황에서는 오직 mintemp <= temp <= maxtemp
        # 인 경우만 고려하면 된다.
        if is_onboard:
            mintemp_to_consider = mintemp
            maxtemp_to_consider = maxtemp + 1
        else:
            mintemp_to_consider = -10
            maxtemp_to_consider = 40 + 1

        for temp in range(mintemp_to_consider, maxtemp_to_consider):
            if temp == temperature:
                candidates = [dp[t - 1][temp + 10]]
                if temp + 10 != 0:
                    candidates.append(dp[t - 1][temp - 1 + 10])
                if temp + 10 != 50:
                    candidates.append(dp[t - 1][temp + 1 + 10])

                dp[t][temp + 10] = min(candidates)

            elif temp > temperature:
                candidates = [dp[t - 1][temp + 10] + b]
                if temp + 10 != 0:
                    candidates.append(dp[t - 1][temp - 1 + 10] + a)
                if temp + 10 != 50:
                    candidates.append(dp[t - 1][temp + 1 + 10])

                dp[t][temp + 10] = min(candidates)
            else:
                candidates = [dp[t - 1][temp + 10] + b]
                if temp + 10 != 0:
                    candidates.append(dp[t - 1][temp - 1 + 10])
                if temp + 10 != 50:
                    candidates.append(dp[t - 1][temp + 1 + 10] + a)

                dp[t][temp + 10] = min(candidates)

    answer = min(dp[len(onboard) - 1])
    return answer