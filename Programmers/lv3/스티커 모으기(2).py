"""
출처 프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/12971
"""
# 내 풀이(개선 중)
def solution(sticker):
    if len(sticker) == 1 or len(sticker) == 2:
        return max(sticker)

    dp = [0] * len(sticker)

    dp[0] = sticker[0]
    dp[1] = sticker[1]
    dp[2] = max(sticker[2] + sticker[0], dp[1])

    for i in range(3, len(sticker)):
        dp[i] = max(dp[i - 2] + sticker[i], dp[i - 3] + sticker[i], dp[i - 1])

    print(dp)

    return 0
# 내 풀이(개선 중)
from collections import deque
import copy


def solution(sticker):
    k = len(sticker)
    # new=sticker+sticker
    if len(sticker) == 1 or len(sticker) == 2:
        return max(sticker[0], sticker[1])

    q = deque([[0], [1]])

    check = []

    while q:
        num = q.popleft()

        if num[-1] + 1 >= k - 1:
            check.append(num)

        if num[-1] + 2 <= (k - 1):
            q.append(num + [num[-1] + 2])

        if num[-1] + 3 <= (k - 1):
            q.append(num + [num[-1] + 3])

    result = 0

    while check:
        c = check.pop()
        count = 0

        if c[0] == 0 and c[-1] == k - 1:
            continue

        for i in c:
            count += sticker[i]

        result = max(result, count)

    return result