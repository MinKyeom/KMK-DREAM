"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/12979
"""
# 내 풀이
from collections import deque


def solution(n, stations, w):
    before = set(stations)

    # 기지국 설치
    new = set([])

    s = deque(stations)
    min_network = 0
    max_network = 0
    result = 0

    # 시작부분 범위 내에 없는 경우
    if s[0] - w > 1:
        max_network = 1 + 2 * w
        new.add(1 + w)
        result += 1

    # 기지국 개설 후 시작
    else:
        max_network = s.popleft() + w

    while max_network < n:
        if len(s) > 0:

            # 이미 설치된 곳의 전파가 드는 권역에 있는 경우(연장하기)
            if s[0] - w <= max_network <= s[0] + w:
                max_network = s[0] + w
                s.popleft()

            # 전파가 드는 권역이 아닌 경우(최대한 넓은 범위를 커버하게하기)
            elif s[0] - w >= max_network + 1:
                result += 1
                new.add(max_network + 1 + w)
                max_network = max_network + 1 + 2 * w

            # 이미 최대로 설치된 곳의 최대치보다 범위가 현재 넓은 경우
            elif s[0] + w < max_network:
                while True and s:
                    if s[0] + w <= max_network:
                        s.popleft()

                    else:
                        break

        else:
            result += 1
            new.add(max_network + 1 + w)
            max_network = max_network + 1 + 2 * w

    # print(s,max_network)

    return len(new - before)
# 내 풀이_개선 중
from collections import deque


def solution(n, stations, w):
    s = deque(stations)
    min_network = 0
    max_network = 0
    result = 0
    # 기지국이 설치된 곳
    check = set([])

    while max_network < n and s:
        if len(s) > 0:

            # 이미 설치된 곳의 전파가 드는 권역에 있는 경우(연장하기)
            if s[0] - w <= max_network <= s[0] + w:
                max_network = s[0] + w
                s.popleft()

            # 전파가 드는 권역이 아닌 경우(최대한 넓은 범위를 커버하게하기)
            elif s[0] - w > max_network:
                result += 1
                max_network = max_network + 1 + 2 * w

            # 이미 최대로 설치된 곳의 최대치보다 범위가 현재 넓은 경우
            elif s[0] + w < max_network:
                while True and s:
                    if s[0] + w <= max_network:
                        s.popleft()
                    else:
                        break

        else:
            result += 1
            max_network = max_network + 1 + 2 * w

    print(s, max_network)

    return result
# 내 풀이_개선 중
from collections import deque


def solution(n, stations, w):
    stations = deque(stations)
    result = 0
    start = 0
    check = []

    while start <= n - 1:
        if len(stations) > 0:
            # 이미 설치된 곳에서 전파가 닿는 경우
            if 0 <= (stations[0] - 1) - start <= w:
                start = (stations[0]) - 1
                stations.popleft()
            # 그렇지 않은 경우 설치
            else:
                check.append(start)
                start += (w + 1)
                result += 1
        else:
            if start + w > n - 1:
                return result
            else:
                check.append(start)
                start += (w + 1)
                result += 1

    return resultㄴㄴ

# 내 풀이_개선 중
def solution(n, stations, w):
    net = [False] * n

    for s in stations:
        net[s - 1] = True

    # 현재 위치
    start = 0
    # w 거리측정
    dis = 0
    # 추가 될 위치
    add = 0

    check = set(stations)

    while start < n:
        if net[start] == False:
            dis += 1
            if dis > w:
                add += 1
                check.add(start)
                dis = 0
        else:
            dis = 0
            while start < n - 1:
                check_last = min(start + w, n - 1)

                for i in range(start + 1, check_last + 1):
                    if net[i] == True:
                        break
                else:
                    start = check_last
                    break

                start = i

        start += 1

    return len(check) - len(stations)

# 내 풀이
def solution(n, stations, w):
    net = [False] * n
    check = set(stations)
    for s in stations:
        s = s - 1
        min_num = max(0, s - w - 1)
        max_num = min(n - 1, s + w + 1)

        for n in range(min_num, max_num + 1):
            net[n] = True

    result = 0

    for t in range(w + 1, n, 2 * w + 1):
        if not ((t - 1) // 2) + 1 + 1 in check:
            result += 1

    return result + len(check)

# 다른 사람 풀이
def solution(n, stations, w):
    ans = 0
    idx = 0
    location = 1

    while(location <= n) :
        if(idx < len(stations) and location >= stations[idx]-w) :
            location = stations[idx]+w+1
            idx += 1
        else :
            location += 2*w+1
            ans += 1
    return ans
