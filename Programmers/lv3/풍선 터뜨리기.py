"""
출처: 프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/68646
"""
# 내 풀이(개선 중)
"""
맨 끝에 두 개는 항상 살아남음 

"""
def solution(a):
    result = []

    if len(a) >= 3:
        for i in range(1, len(a) - 1):
            num = a[i]

            # 좌
            count_left = 0
            for l in range(i):
                if a[l] < num:
                    count_left += 1
                    if count_left >= 2:
                        break
            # 우
            count_right = 0
            for r in range(i + 1, len(a)):
                if a[r] < num:
                    count_right += 1
                    if count_right >= 2:
                        break

            if count_left == 0 and count_right >= 1:
                result.append(num)
            elif count_right == 0 and count_left >= 1:
                result.append(num)
            elif count_right == 0 and count_left == 0:
                result.append(num)

    return len(set(result)) + 2

# 내 풀이(개선 중)
"""
맨 끝에 두 개는 항상 살아남음 

"""
def solution(a):
    result = []

    if len(a) >= 3:
        for i in range(1, len(a) - 1):
            num = a[i]
            left = float("inf")
            right = float("inf")

            # 좌
            for l in range(i):
                left = min(left, a[l])

            # 우
            for r in range(i + 1, len(a)):
                right = min(right, a[r])

            if right < num and left < num:
                continue
            else:
                result.append(num)

    return len(set(result)) + 2

# 다른 사람 풀이
def solution(a):
    answer = 2  # 양 끝값
    dp = [[0 for _ in range(len(a))] for _ in range(2)]
    dp[0][0] = a[0]
    dp[1][-1] = a[-1]
    # 좌측->우측 방향 최솟값dp
    for i in range(1, len(a)):
        dp[0][i] = min(dp[0][i - 1], a[i])
    # 우측->좌측 방향 최솟값dp
    for i in range(len(a) - 2, -1, -1):
        dp[1][i] = min(dp[1][i + 1], a[i])

    for i in range(1, len(a) - 1):
        left_min = dp[0][i - 1]  # 좌측 최솟값
        right_min = dp[1][i + 1]  # 우측 최솟값
        # 양쪽 모두 큰경우
        if left_min > a[i] and right_min > a[i]:
            answer += 1
        # 한쪽은 크고 다른한쪽은 작은경우
        elif (left_min > a[i] and right_min < a[i])
            or (left_min < a[i] and right_min > a[i]):
            answer += 1

    return answer


def solution(a):
    ret = 2
    if 0 <= len(a) <= 2:
        return len(a)
    left = a[0]
    right = a[-1]

    for i in range(1, len(a) - 1):
        if left > a[i]:
            left = a[i]
            ret += 1
        if right > a[-1 - i]:
            right = a[-1 - i]
            ret += 1
    if left == right:
        return ret - 1
    else:
        return ret


def solution(a):
    if len(a) == 1:
        return 1

    answer = 2  # 기본적으로 양쪽 끝은 끝까지 살아남을 수 있음

    # 최솟값 쌓기 ----------------
    l_min = [a[0]]
    r_min = [a[-1]]
    for i in range(1, len(a)):
        if a[i] < l_min[-1]:
            l_min.append(a[i])
        else:
            l_min.append(l_min[-1])
        if a[len(a) - 1 - i] < r_min[-1]:
            r_min.append(a[len(a) - 1 - i])
        else:
            r_min.append(r_min[-1])
    r_min.reverse()
    # -----------------

    # 찾은 최솟값으로 비교 계산 -------------
    for i in range(1, len(a) - 1):
        if l_min[i - 1] > a[i] or r_min[i + 1] > a[i]:
            answer += 1
    # --------------------------------

    return answer