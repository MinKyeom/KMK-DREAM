# 내 풀이(개선 중2)
def solution(n):
    # n:n가로 길이
    dp = [0] * (n + 1)
    dp[0] = 0

    if n == 1:
        dp[1] = 1
        return dp[1] % 1000000007
    elif n == 2:
        dp[2] = 3
        return dp[2] % 1000000007
    elif n == 3:
        dp[3] = 10
        return dp[3] % 1000000007
    else:
        dp[1] = 1
        dp[2] = 3
        dp[3] = 10
    if n >= 4:
        dp[4] = dp[3] + dp[2] * 2 + dp[1] * 5 + 2
    if n >= 5:
        dp[5] = dp[4] + dp[3] * 2 + dp[2] * 5 + dp[1] * 2 + 2
    if n >= 6:
        dp[6] = dp[5] + dp[4] * 2 + dp[3] * 5 + dp[2] * 2 + dp[1] * 2 + 4
    if n >= 7:
        for i in range(7, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] * 2 + dp[i - 3] * 5 + dp[i - 4] * 2 + dp[i - 5] * 2 + dp[i - 6] * 4

    return dp[n] % 1000000007

# 내 풀이(개선 중)
def solution(n):
    # n:n가로 길이
    dp = [0] * (n + 1)

    dp[0] = 0

    if n == 1:
        dp[1] = 1
        return dp[1] % 1000000007
    elif n == 2:
        dp[2] = 3
        return dp[2] % 1000000007
    elif n == 3:
        dp[3] = 10
        return dp[3] % 1000000007
    else:
        dp[0] = 0
        dp[1] = 1
        dp[2] = 3
        dp[3] = 10

    for i in range(4, n + 1):
        dp[i] = dp[i - 3] * 10

    return dp[n] % 1000000007


