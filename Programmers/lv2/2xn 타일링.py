# 내 풀이
# dp
def solution(n):
    dp = [0, 1, 2, 3]
    if n == 0 or n == 1 or n == 2 or n == 3:
        return dp[n]
    count = 4

    i = dp[3]  # n-1
    j = dp[2]  # n-2

    while count <= n:
        new = i + j
        i, j = new, i
        count += 1

    return new % 1000000007

# 다른 사람 풀이
def tiling(n):
    a,b=1,1
    for i in range(n):a,b=b,a+b
    return a%100000


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(tiling(6))