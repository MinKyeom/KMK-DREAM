"""
출처:백준,
https://www.acmicpc.net/problem/2775
"""

# 풀이 과정_개선 중
count = int(input())

for i in range(count):
    k = int(input())
    n = int(input())

    dp = [[0] * (n + 1) for k in range(k + 1)]
    for num in range(n + 1):
        dp[0][num] = num

    """
    dp[n][k]=dp[n-1][0]~ dp[n-1][k]까지 모두 더함
    """

    for floor in range(1, k + 1):
        for num in range(1, n + 1):
            dp[floor][n] += dp[floor - 1][num]

    print(dp[k][n])