"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/12907
"""

# 내 풀이_개선 중
from collections import Counter, deque


def solution(n, money):
    q = deque([[n, []]])
    result = []

    while q:
        count, num = q.popleft()

        for i in money:
            if count > i:
                q.append([count - i, num + [i]])
            elif count == i:
                if not Counter(num + [i]) in result:
                    result.append(Counter(num + [i]))

    return len(result) % 1000000007