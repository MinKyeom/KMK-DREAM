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

# 다른 사람 풀이
