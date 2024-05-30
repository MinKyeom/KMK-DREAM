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