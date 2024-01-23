# 내 풀이(개선 중)
# bfs로 접근했으나 dp로 각 사각형을 쪼개서 계산하는 방향성 생각해보기!
# 규칙성을 파악하는 dp!! 패턴 파악!

def solution(n):
    dp = [0, 0, 3, 0, 11]
    if n == 2:
        return dp[2]
    elif n == 4:
        return dp[4]
    elif n % 2 == 1:
        return 0
    else:
        check = 4

        while check < n:
            new = dp[check] * 3
            dp.append(0)

            for i in range(2, check):
                new += dp[i] * 2

            new += 2

            dp.append(new)

            check += 2

    return dp[n] % 1000000007



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