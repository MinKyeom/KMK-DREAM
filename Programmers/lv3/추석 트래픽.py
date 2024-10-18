"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/17676
"""
# 내 풀이
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