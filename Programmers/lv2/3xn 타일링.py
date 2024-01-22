# 내 풀이(개선 중)
# bfs로 접근했으나 dp로 각 사각형을 쪼개서 계산하는 방향성 생각해보기!
from collections import deque
def solution(n):
    check = [0, 0, 3, 0, 11]
    if (n * 3) % 2 == 1:
        return 0

    else:
        if n == 2 or n == 4:
            return check[n] % 1000000007

        else:
            for i in range(5, n + 1):
                if i % 2 == 0:
                    num = check[i - 2] * 3 + 2
                    check.append(num)
                else:
                    check.append(0)

            return check[n] % 1000000007



# 다른 사람 풀이
def solution(n):
    mod = 1000000007
    dp = [0 for i in range(n+1)]
    dp[2] = 3
    if n > 2:
        dp[4] = 11
        for i in range(6, n+1):
            if i % 2 == 0:
                dp[i] = dp[i-2] * 3 + 2
                for j in range(i-4, -1, -2):
                    dp[i] += dp[j] * 2
                dp[i] = dp[i] % mod
            else:
                dp[i] = 0
    return dp[n]