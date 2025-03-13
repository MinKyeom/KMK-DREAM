"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/258705
"""

# 풀이 과정
# 일정 규칙성을 지닌 것으로 판단되어 점화식>dp 생각 접근
# 점화식 찾기
# 위에 삼각형이 있나 없나 여부에 따른 점화식의 변화
# 직전한을 수가 아닌 모양으로 표현해서 규칙성 찾아보기!
def solution(n, tops):
    reuslt = 0
    dp = [0] * (n + 1)  # 0~n
    # case 분류
    # \\ 실행 여부로 구분!
    i = [0] * (n + 1)  # 실행
    j = [0] * (n + 1)  # 비실행

    i[0] = 0
    j[0] = 1
    # 두번 째 항
    if tops[0] == 1:
        i[1] = 1
        j[1] = 3
    else:
        i[1] = 1
        j[1] = 2

    for k in range(1, n):
        if tops[k] == 1:
            i[k + 1] = (i[k] + j[k]) % 10007
            j[k + 1] = (i[k] * 2 + j[k] * 3) % 10007
        else:
            i[k + 1] = (i[k] + j[k]) % 10007
            j[k + 1] = (i[k] + j[k] * 2) % 10007

    return (i[n] + j[n]) % 10007

# 내 풀이(개선 중)
# 일정 규칙성을 지닌 것으로 판단되어 점화식>dp 생각 접근
# 점화식 찾기
# 위에 삼각형이 있나 없나 여부에 따른 점화식의 변화
# 직전한을 수가 아닌 모양으로 표현해서 규칙성 찾아보기!
def solution(n, tops):
    reuslt = 0
    dp = [0] * (n + 2)  # 0~n
    d_p = [0] * (n + 1)  # 아래 점 기준

    # 첫 항
    if tops[0] == 1:
        dp[1] = 1
        dp[2] = 4
    else:
        dp[1] = 1
        dp[2] = 3

    # 두 번째
    if len(tops) >= 2:
        if tops[1] == 1:
            if tops[0] == 1:
                dp[2] = 15
            else:
                dp[2] = 11
        else:
            if tops[0] == 1:
                dp[2] = 11
            else:
                dp[2] = 8

    for i in range(1, n):
        if tops[i] == 1:
            dp[i + 2] = dp[i + 1] * 3 + dp[i] * (tops[i - 1] + 1)
            # u_p[i+1]=2*u_p[i]
            # d_p[i+2]+=d_p[i]
        else:
            dp[i + 2] = dp[i + 1] * 2 + dp[i] * (tops[i - 1] + 1)
            # u_p[i+1]=2*u_p[i]
            # d_p[i+2]+=d_p[i]
    print(dp)
    return 0

# 내 풀이(개선 중)
# 일정 규칙성을 지닌 것으로 판단되어 점화식>dp 생각 접근
# 점화식 찾기
# 위에 삼각형이 있나 없나 여부에 따른 점화식의 변화
# 직전한을 수가 아닌 모양으로 표현해서 규칙성 찾아보기!
def solution(n, tops):
    reuslt = 0
    dp = [0] * (n + 1)  # 0~n
    dp[0] = 1
    # 첫 항
    if tops[0] == 1:
        dp[1] = 4
    else:
        dp[1] = 3

    if n >= 2:
        if tops[1] == 1:
            if tops[0] == 1:
                dp[2] = 15
            else:
                dp[2] = 11
        else:
            if tops[0] == 1:
                dp[2] = 11
            else:
                dp[2] = 8

    for i in range(2, n):
        if tops[i] == 1:
            dp[i + 1] = dp[i] * 3
            count = 1
            for j in range(i):
                count *= (tops[j] + 2)
            count += dp[i - 2]
            dp[i + 1] += count
        else:
            dp[i + 1] = dp[i] * 2
            count = 1
            for j in range(i):
                count *= (tops[j] + 2)
            count += dp[i - 2]
            dp[i + 1] += count
    return dp[-1] % 10007

# 다른 사람 풀이
def solution(n, tops):
    MOD = 10007
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    a[0] = 0
    b[0] = 1

    for k in range(1, n + 1):
        if tops[k - 1]:
            a[k] = (a[k - 1] + b[k - 1]) % MOD
            b[k] = (2 * a[k - 1] + 3 * b[k - 1]) % MOD
        else:
            a[k] = (a[k - 1] + b[k - 1]) % MOD
            b[k] = (a[k - 1] + 2 * b[k - 1]) % MOD

    return (a[n] + b[n]) % MOD