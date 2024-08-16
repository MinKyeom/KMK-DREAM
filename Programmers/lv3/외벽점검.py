"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/60062
"""
# 내 풀이(개선 중)
"""
1시간 
보내야 할 친구 수

n:외벽 길이
weak:취약 지점
dist:친구들이 이동 할 수 있는 길이

"""
from collections import deque


def solution(n, weak, dist):
    # 최대 친구 수
    max_p = len(dist)

    # 취약점 확인 포인트
    point = set(weak)

    dist.sort(reverse=True)

    d = deque(dist)

    check = []

    while d:
        p = d.popleft()

        for i in weak:
            # 시계방향
            right = []
            count = 0

            while count < p:
                if i + count in weak:
                    right.append(i + count)

                count += 1

            # 반시계방향
            left = []
            count = 0
            while count < p:
                if i - count < 0:
                    num = n - abs(i - count)
                else:
                    num = i - count
                if num in weak:
                    left.append(num)

                count += 1

            print(left, right)
            break
    return -1