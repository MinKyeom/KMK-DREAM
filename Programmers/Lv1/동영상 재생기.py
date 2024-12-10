"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/340213
"""

# 풀이 과정

def solution(video_len, pos, op_start, op_end, commands):
    check = [video_len, pos, op_start, op_end]

    # 모두 초로 변환
    renew = []

    for c in check:
        k = c.split(":")
        m, s = int(k[0]) * 60, int(k[1])
        renew.append(m + s)

    now = renew[1]

    if renew[2] <= now <= renew[3]:
        now = renew[3]

    for c in commands:
        if c == "prev":
            now -= 10
            now = max(0, now)

        elif c == "next":
            now += 10
            now = min(now, renew[0])

        if renew[2] <= now <= renew[3]:
            now = renew[3]

    if len(str(now // 60)) == 1:
        h = "0" + str(now // 60)
    else:
        h = str(now // 60)

    if len(str(now % 60)) == 1:
        m = "0" + str(now % 60)
    else:
        m = str(now % 60)

    return h + ":" + m

# 다른 사람 풀이
def time_to_seconds(time_str):
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds

def seconds_to_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes:02d}:{seconds:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    video_len = time_to_seconds(video_len)
    current_pos = time_to_seconds(pos)
    op_start = time_to_seconds(op_start)
    op_end = time_to_seconds(op_end)

    for command in commands:
        if op_start <= current_pos <= op_end:
            current_pos = op_end

        if command == "prev":
            current_pos = max(0, current_pos - 10)
        elif command == "next":
            current_pos = min(video_len, current_pos + 10)

    # 마지막 명령 실행 후 한 번 더 오프닝 체크
    if op_start <= current_pos <= op_end:
        current_pos = op_end

    return seconds_to_time(current_pos)