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