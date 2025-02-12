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

# 다른 사람 풀이
    t = int(input())

    for _ in range(t):
        floor = int(input())
        num = int(input())
        f0 = [x for x in range(1, num + 1)]
        for k in range(floor):
            for i in range(1, num):
                f0[i] += f0[i - 1]
            print(f0)  # 프린트문을 추가
        print(f0[-1])