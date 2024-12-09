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