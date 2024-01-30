# 내 풀이
def count(k,dp):
    for a in range(4,k+1):
        dp[a]=dp[a-1]+dp[a-2]+dp[a-3]
    return dp[k]

n = int(input())
result=[]
for t in range(n):
    k = int(input())
    dp=[0,1,2,4]
    if k<=3:
        result.append(dp[k])
    else:
        dp = [0, 1, 2, 4] + [0] * (k - 3)
        num = count(k, dp)
        result.append(num)

for i in result:
    print(i)