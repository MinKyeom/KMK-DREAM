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
import copy


def solution(n, weak, dist):
    # 최대 친구 수
    max_p = len(dist)

    # 취약점 확인 포인트
    point = set(weak)

    dist.sort(reverse=True)

    first = dist[0]

    q = deque([])
    new = set([])

    for i in weak:
        new_left = copy.deepcopy(new)
        new_right = copy.deepcopy(new)

        for w in range(first + 1):
            right = min(i + w, n - 1)

            if i - w < 0:
                left = n - abs(i - w)

            else:
                left = i - w

            if left in point:
                new_left.add(left)
            if right in point:
                new_right.add(right)

        q.append(new_left)
        q.append(new_right)

    person = 1
    new_q = []

    while q and person < len(dist):
        k = q.popleft()

        if len(point - k) == 0:
            return person

        p = dist[person]

        for i in weak:
            new_left = copy.deepcopy(k)
            new_right = copy.deepcopy(k)

            for w in range(p + 1):
                right = min(i + w, n - 1)

                if i - w < 0:
                    left = n - abs(i - w)

                else:
                    left = i - w

                if left in point:
                    new_left.add(left)
                if right in point:
                    new_right.add(right)

            new_q.append(new_left)
            new_q.append(new_right)

        if len(q) == 0:
            person += 1
            q = list(q)
            q += new_q
            q = deque(q)
            new_q = []

    return -1

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