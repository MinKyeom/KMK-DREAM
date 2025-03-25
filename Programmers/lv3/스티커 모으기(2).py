"""
출처 프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/12971
"""
# 풀이 과정
from collections import deque


def solution(sticker):
    s = deque(sticker)
    if len(s) == 0 or len(s) == 1:
        return max(s)

    dp_one = [0] * len(s)
    dp_one[0] = s[0]
    dp_one[1] = max(s[0], s[1])

    for i in range(2, len(s) - 1):
        dp_one[i] = max(dp_one[i - 1], dp_one[i - 2] + s[i])

    k = s.popleft()
    s.append(k)

    one = max(dp_one)

    dp_two = [0] * len(s)
    dp_two[0] = s[0]
    dp_two[1] = max(s[0], s[1])

    for i in range(2, len(s) - 1):
        dp_two[i] = max(dp_two[i - 1], dp_two[i - 2] + s[i])

    two = max(dp_two)

    return max(one, two)
# 내 풀이(개선 중)
from collections import deque


def solution(sticker):
    s = deque(sticker)

    if len(s) == 1 or len(s) == 2:
        return max(s)

    result = [0, 0, 0]

    count = 0

    while count < 3:
        start = 0
        result[count] += s[0]

        while start <= len(s) - 2:
            if start <= len(s) - 6:
                if s[start + 2] + s[start + 4] < s[start + 3]:
                    result[count] += s[start + 3]
                    start += 3
                else:
                    result[count] += s[start + 2]
                    start += 2
            else:
                if start == len(s) - 4:
                    result[count] += s[start + 2]
                    start += 2
                    break
                elif start == len(s) - 3:
                    break
                else:
                    if s[start + 2] >= s[start + 3]:
                        result[count] += s[start + 2]
                        break
                    else:
                        result[count] += s[start + 3]
                        break
        count += 1
        n = s.popleft()
        s.append(n)

    # print(result)

    return max(result)


# 내 풀이(개선 중)
def solution(sticker):
    if len(sticker) == 1 or len(sticker) == 2:
        return max(sticker)

    result = [0, 0]

    zero_start = set([0])

    start = 0

    # 0 start
    while start < len(sticker) - 1:
        if start <= len(sticker) - 6:
            if sticker[start + 2] + sticker[start + 4] < sticker[start + 3]:
                zero_start.add(start + 3)
                start += 3
            else:
                zero_start.add(start + 2)
                start += 2
        else:
            if start == len(sticker) - 4:
                zero_start.add(start + 2)
                start += 2
                break
            elif start == len(sticker) - 5:
                if sticker[start + 2] >= sticker[start + 3]:
                    zero_start.add(start + 2)
                    break
                else:
                    zero_start.add(start + 3)
                    break

    for i in zero_start:
        result[0] += sticker[i]

    one_start = set([1])
    start = 1

    # 1 start
    while start < len(sticker):
        if start <= len(sticker) - 5:
            if sticker[start + 2] + sticker[start + 4] < sticker[start + 3]:
                one_start.add(start + 3)
                start += 3
            else:
                one_start.add(start + 2)
                start += 2
        else:
            if start == len(sticker) - 3:
                one_start.add(start + 2)
                start += 2
                break
            elif start == len(sticker) - 4:
                if sticker[start + 2] >= sticker[start + 3]:
                    one_start.add(start + 2)
                    break
                else:
                    one_start.add(start + 3)
                    break

    for i in one_start:
        result[1] += sticker[i]

        # print(zero_start,one_start)

    return max(result)


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

# 다른 사람 풀이
def solution(sticker):
    answer = 0
    if len(sticker) == 1:
        return sticker.pop()

    size = len(sticker)
    # 1번 선택하는 경우 -> 1..n-1번 배열에 대한 DP
    dp1 = [0] + sticker[:-1]
    for i in range(2, size):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + dp1[i])

    # 2번 선택하는 경우 -> 2...n번 배열에 대한 DP
    dp2 = [0] + sticker[1:]
    for i in range(2, size):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + dp2[i])

    answer = max(dp1[-1], dp2[-1])
    return answer