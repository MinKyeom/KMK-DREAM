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

# 다른 사람 풀이
import sys

input = sys.stdin.readline

n = int(input())

# 계단의 숫자를 초기화 합니다. 1층은 1번째(not 0번째) 인덱스에 저장합니다.
stairs = [0] * 301
for i in range(1, n + 1):
    stairs[i] = int(input())

# dp 배열을 초기화합니다.
dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

# 점화식을 계산합니다.
for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[n])