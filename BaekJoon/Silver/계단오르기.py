"""
출처:백준,
https://www.acmicpc.net/problem/2579
"""

# 풀이 과정
n = int(input())
stage = [0]

for i in range(n):
    k = int(input())
    stage.append(k)

dp = [0] * (n + 1)
dp_check = [False] * (n + 1)

dp[1] = stage[1]
if n == 1:
    print(stage[1])

elif n == 2:
    print(max(stage[1], stage[1] + stage[2]))
else:

    if stage[1] == 0:
        dp[2] == stage[2]


    else:
        dp[2] = stage[1] + stage[2]
        dp_check[2] = True

    count = 3

    while count < n + 1:
        if dp_check[count - 1] == False:
            one = stage[count] + dp[count - 1]

        else:
            one = stage[count] + dp[count - 3] + stage[count - 1]

        two = stage[count] + dp[count - 2]

        if one > two:
            dp_check[count] = True
            dp[count] = one
        else:
            dp_check[count] = False
            dp[count] = two

        count += 1

    print(dp[-1])

"""

6
10
20
15
25
10
20

"""