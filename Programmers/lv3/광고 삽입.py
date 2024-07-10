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