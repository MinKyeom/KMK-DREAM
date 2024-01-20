# 내 풀이 (개선 중)
def solution(begin, end):
    road_num = [k for k in range(begin, end + 1)]
    road = [1 for _ in range(begin, end + 1)]

    for i in range(len(road)):
        t = int(road_num[i] ** 0.5)

        if t == 1:
            road[i] == 1
            continue

        for j in range(2, t + 1):
            if road_num[i] / j == int(road_num[i] // j) and road_num[i] / j <= 10000000:
                road[i] = road_num[i] // j
            else:
                continue

    if begin == 1:
        road[0] = 0

    return road
