"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/17676
"""
# 내 풀이
# 누적합
from collections import defaultdict

Data = [0] * 24 * 60 * 60 * 1000


# for s in range(24*60*60):
#     Data[s]=0

def time_to_sec(x, y):
    global Data

    t = x.split(":")
    hour, minu, sec = int(t[0]), int(t[1]), float(t[2])
    end_time = (int(hour) * 60 * 60 + int(minu) * 60 + sec) * 1000

    blank = list(y)
    blank.pop()
    y = "".join(blank)

    # 시작 시간, 끝 시간
    start = end_time - float(y) * 1000 + 1
    start = max(0, start)
    end_time = min(24 * 60 * 60 * 1000 - 1, end_time + 999)
    start, end = int(start), int(end_time)

    for tra in range(start, end + 1):
        Data[tra] += 1

    return 0


def solution(lines):
    global Data

    for l in lines:
        d = l.split(" ")
        time = time_to_sec(d[1], d[2])

    result = 0
    count = 0
    result = max(Data)

    return result

# 내 풀이_개선 중
# 누적합
from collections import defaultdict

Data = defaultdict(int)


# for s in range(24*60*60):
#     Data[s]=0

def time_to_sec(x, y):
    global Data

    t = x.split(":")
    hour, minu, sec = int(t[0]), int(t[1]), float(t[2])
    end_time = (int(hour) * 60 * 60 + int(minu) * 60 + sec) * 1000

    blank = list(y)
    blank.pop()
    y = "".join(blank)
    # 시작 시간, 끝 시간
    start = end_time - float(y) * 1000 + 1
    start = max(0, start)
    start, end = int(start), int(end_time)
    for tra in range(start, end + 1):
        Data[tra] += 1

    return 0


def solution(lines):
    global Data

    for l in lines:
        d = l.split(" ")
        time = time_to_sec(d[1], d[2])

    result = 0
    count = 0
    for t in range(24 * 60 * 60 * 1000):
        if t < 1000:
            count += Data[t]
        else:
            count += Data[t]
            count -= Data[t - 1000]

        result = max(result, count)

    return result
# 내 풀이_개선 중
from collections import defaultdict

Data = defaultdict(int)


# for s in range(24*60*60):
#     Data[s]=0

def time_to_sec(x, y):
    global Data

    t = x.split(":")
    hour, minu, sec = int(t[0]), int(t[1]), float(t[2])
    end_time = int(hour) * 60 * 60 + int(minu) * 60 + sec

    blank = list(y)
    blank.pop()
    y = "".join(blank)
    # 시작 시간, 끝 시간
    start = end_time - float(y) + 0.001
    start = int(max(start, 0))

    if end_time == int(end_time):
        end = int(end_time)
    else:
        end = int(end_time) + 1

    for s in range(start, end + 1):
        Data[s] += 1

    return 0


def solution(lines):
    global Data

    for l in lines:
        d = l.split(" ")
        time = time_to_sec(d[1], d[2])

    max_progress = 0

    for i, j in Data.items():
        max_progress = max(j, max_progress)

    print(Data)

    return max_progress

