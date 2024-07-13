"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/72414

"""
# 내 풀이(개선 중)
"""
주어진 변수:
play_time: 재생시간, adv_time:재생시간 길이 logs:시청자들이 시청한 구간정보

목표: 누적 재생시간이 나오는 곳에 공익광고 삽입

시작시간 구하기(여러 개라면 제일 빠른 시간)

생각방향: 주어진 광고시간을 초당으로 누적인원을 집계했을 때 가장 많이 본 시간의 시작점 구하기

모두 초로 바꿔서 구하기 
"""


def solution(play_time, adv_time, logs):
    play = play_time.split(":")
    play = list(map(int, play))

    # 플레이타임을 모두 초로 변경
    p = play[0] * 60 * 60 + play[1] * 60 + play[2]

    # 초당 뷰 체크 목록
    view_check = [0] * (p + 1)

    adver = adv_time.split(":")
    adver = list(map(int, adver))

    # 광고 시간을 모두 초로 변경
    adver = adver[0] * 60 * 60 + adver[1] * 60 + adver[2]

    l = []

    for i in logs:
        # - 제거
        viewer = i.split("-")
        v_start = viewer[0]
        v_end = viewer[1]

        # : 제거
        v_start = v_start.split(":")
        v_start = list(map(int, v_start))

        v_end = v_end.split(":")
        v_end = list(map(int, v_end))

        v_start = v_start[0] * 60 * 60 + v_start[1] * 60 + v_start[2]
        v_end = v_end[0] * 60 * 60 + v_end[1] * 60 + v_end[2]

        l.append((v_start, v_end))

    # 각 초별 시청자 집계
    for start, end in l:
        for t in range(start, end):
            view_check[t] += 1

    # 최고점 기록
    best_view = 0
    best_time = 0

    check = 0

    for i in range(adver + 1):
        check += view_check[i]

    best_view = check

    # 누적 집계 최고점 찾기
    for i in range(adver, p + 1):
        check -= view_check[i - adver]
        check += view_check[i]

        if check > best_view:
            best_view = check
            best_time = i - adver + 1

    result = ""

    # best_time 변환
    hour = best_time // 3600

    if len(str(hour)) == 1:
        h = str(0) + str(hour)

    else:
        h = str(hour)
    result = result + h + ":"

    minute = (best_time - 3600 * hour) // 60

    if len(str(minute)) == 1:
        m = str(0) + str(minute)
    else:
        m = str(minute)
    result = result + m + ":"
    second = best_time - 3600 * hour - 60 * minute

    if len(str(second)) == 1:
        s = str(0) + str(second)
    else:
        s = str(second)

    result = result + s

    return result

# 내 풀이(개선 중)_정확도100 시간 초과 몆 개 발생
"""
주어진 변수:
play_time: 재생시간, adv_time:재생시간 길이 logs:시청자들이 시청한 구간정보

목표: 누적 재생시간이 나오는 곳에 공익광고 삽입

시작시간 구하기(여러 개라면 제일 빠른 시간)

생각방향: 주어진 광고시간을 초당으로 누적인원을 집계했을 때 가장 많이 본 시간의 시작점 구하기

모두 초로 바꿔서 구하기 
"""


def solution(play_time, adv_time, logs):
    play = play_time.split(":")
    play = list(map(int, play))

    # 플레이타임을 모두 초로 변경
    p = play[0] * 60 * 60 + play[1] * 60 + play[2]

    # 초당 뷰 체크 목록
    view_check = [0] * (p + 1)

    adver = adv_time.split(":")
    adver = list(map(int, adver))

    # 광고 시간을 모두 초로 변경
    adver = adver[0] * 60 * 60 + adver[1] * 60 + adver[2]

    l = []

    for i in logs:
        # - 제거
        viewer = i.split("-")
        v_start = viewer[0]
        v_end = viewer[1]

        # : 제거
        v_start = v_start.split(":")
        v_start = list(map(int, v_start))

        v_end = v_end.split(":")
        v_end = list(map(int, v_end))

        v_start = v_start[0] * 60 * 60 + v_start[1] * 60 + v_start[2]
        v_end = v_end[0] * 60 * 60 + v_end[1] * 60 + v_end[2]

        l.append((v_start, v_end))

    # 각 초별 시청자 집계
    for start, end in l:
        for t in range(start, end):
            view_check[t] += 1

    # 최고점 기록
    best_view = 0
    best_time = 0

    check = 0
    for i in range(adver + 1):
        check += view_check[i]

    best_view = check

    # 누적 집계 최고점 찾기
    for i in range(adver, p + 1):
        check -= view_check[i - adver]
        check += view_check[i]

        if check > best_view:
            best_view = check
            best_time = i - adver + 1
    result = ""

    # best_time 변환
    hour = best_time // 3600

    if len(str(hour)) == 1:
        h = str(0) + str(hour)

    else:
        h = str(hour)
    result = result + h + ":"

    minute = (best_time - 3600 * hour) // 60

    if len(str(minute)) == 1:
        m = str(0) + str(minute)
    else:
        m = str(minute)
    result = result + m + ":"
    second = best_time - 3600 * hour - 60 * minute

    if len(str(second)) == 1:
        s = str(0) + str(second)
    else:
        s = str(second)

    result = result + s

    return result
# 내 풀이(개선 중)
"""
주어진 변수:
play_time: 재생시간, adv_time:재생시간 길이 logs:시청자들이 시청한 구간정보

목표: 누적 재생시간이 나오는 곳에 공익광고 삽입

시작시간 구하기(여러 개라면 제일 빠른 시간)

생각방향: 주어진 광고시간을 초당으로 누적인원을 집계했을 때 가장 많이 본 시간의 시작점 구하기

모두 초로 바꿔서 구하기 
"""


def solution(play_time, adv_time, logs):
    play = play_time.split(":")
    play = list(map(int, play))

    # 플레이타임을 모두 초로 변경
    p = play[0] * 60 * 60 + play[1] * 60 + play[2]

    # 초당 뷰 체크 목록
    view_check = [0] * (p + 1)

    adver = adv_time.split(":")
    adver = list(map(int, adver))

    # 광고 시간을 모두 초로 변경
    adver = adver[0] * 60 * 60 + adver[1] * 60 + adver[2]

    l = []

    for i in logs:
        # - 제거
        viewer = i.split("-")
        v_start = viewer[0]
        v_end = viewer[1]

        # : 제거
        v_start = v_start.split(":")
        v_start = list(map(int, v_start))

        v_end = v_end.split(":")
        v_end = list(map(int, v_end))

        v_start = v_start[0] * 60 * 60 + v_start[1] * 60 + v_start[2]
        v_end = v_end[0] * 60 * 60 + v_end[1] * 60 + v_end[2]

        l.append((v_start, v_end))

    # 각 초별 시청자 집계
    for start, end in l:
        for t in range(start, end + 1):
            view_check[t] += 1

    # 최고점 기록
    best_view = 0
    best_time = 0

    check = 0
    for i in range(1, adver):
        check += view_check[i]

    # 누적 집계 최고점 찾기
    for i in range(1, p - adver):
        if check > best_view:
            best_view = check
            best_time = i - 1
        else:
            check -= view_check[i - 1]
            check += view_check[i]

    # print(best_time)

    # best_time 변환
    hour = best_time // 3600

    if len(str(hour)) == 1:
        h = str(0) + str(hour)

    else:
        h = str(hour)

    print(h)

    minute = (best_time - 3600 * hour) // 60

    return 0

# 내 풀이(개선 중)

"""
주어진 변수:
play_time: 재생시간, adv_time:재생시간 길이 logs:시청자들이 시청한 구간정보

목표: 누적 재생시간이 나오는 곳에 공익광고 삽입

시작시간 구하기(여러 개라면 제일 빠른 시간)

생각방향: 주어진 광고시간을 초당으로 누적인원을 집계했을 때 가장 많이 본 시간의 시작점 구하기

모두 초로 바꿔서 구하기 
"""


def solution(play_time, adv_time, logs):
    play = play_time.split(":")
    play = list(map(int, play))

    # 플레이타임을 모두 초로 변경
    p = play[0] * 60 * 60 + play[1] * 60 + play[2]

    # 초당 뷰 체크 목록
    view_check = [0] * p

    adver = adv_time.split(":")
    adver = list(map(int, adver))

    # 광고 시간을 모두 초로 변경
    adver = adver[0] * 60 * 60 + adver[1] * 60 + adver[2]

    l = []

    for i in logs:
        # - 제거
        viewer = i.split("-")
        v_start = viewer[0]
        v_end = viewer[1]

        # : 제거
        v_start = v_start.split(":")
        v_start = list(map(int, v_start))

        v_end = v_end.split(":")
        v_end = list(map(int, v_end))

        v_start = v_start[0] * 60 * 60 + v_start[1] * 60 + v_start[2]
        v_end = v_end[0] * 60 * 60 + v_end[1] * 60 + v_end[2]

        l.append((v_start, v_end))

    # 각 초별 시청자 집계
    for start, end in l:
        for t in range(start, end):
            view_check[t] += 1

    # 최고점 기록
    best_view = 0
    best_time = 0

    check = 0
    for i in range(adver - 1):
        check += view_check[i]

    # 누적 집계 최고점 찾기
    for i in range(1, p - adver):

        if check > best_view:
            best_view = check
            best_time = i - 1
            print(i - 1, check)
        else:
            check -= view_check[i - 1]
            check += view_check[i]

    # print(best_time)

    # best_time 변환
    hour = best_time // 3600

    if len(str(hour)) == 1:
        h = str(0) + str(hour)

    else:
        h = str(hour)

    print(h)

    minute = (best_time - 3600 * hour) // 60

    return 0

# 다른 사람 풀이
def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)        # 1
    adv_time = str_to_int(adv_time)
    all_time = [0 for i in range(play_time + 1)]

    for l in logs:                           # 2
        start, end = l.split('-')
        start = str_to_int(start)
        end = str_to_int(end)
        all_time[start] += 1
        all_time[end] -= 1

    for i in range(1, len(all_time)):       # 3
        all_time[i] = all_time[i] + all_time[i - 1]

    for i in range(1, len(all_time)):       # 4
        all_time[i] = all_time[i] + all_time[i - 1]

    most_view = 0                           # 5
    max_time = 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1

    return int_to_str(max_time)


def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s