"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/42898
"""
# 내 풀이
from collections import deque


def solution(m, n, puddles):
    puddles = set(list(map(tuple, puddles)))

    check = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(2, m + 1):
        if not (i, 1) in puddles:
            check[1][i] = 1
        else:
            break

    for j in range(2, n + 1):
        if not (1, j) in puddles:
            check[j][1] = 1
        else:
            break

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            if not (j, i) in puddles:
                check[i][j] = check[i - 1][j] + check[i][j - 1]
            else:
                check[i][j] = 0

    return check[n][m] % 1000000007


# 다른 사람 풀이
def solution(m,n,puddles):
    grid = [[0]*(m+1) for i in range(n+1)] #왼쪽, 위로 한줄씩 만들어서 IndexError 방지
    if puddles != [[]]:                    #물이 잠긴 지역이 0일 수 있음
        for a, b in puddles:
            grid[b][a] = -1                #미리 -1로 체크
    grid[1][1] = 1
    for j in range(1,n+1):
        for k in range(1,m+1):
            if j == k == 1:                #(1,1)은 1로 만들어두고, 0이 되지 않도록
                continue
            if grid[j][k] == -1:           #웅덩이는 0으로 만들어 다음 덧셈 때 영향끼치지 않게
                grid[j][k] = 0
                continue
            grid[j][k] = (grid[j][k-1] + grid[j-1][k])%1000000007   #[a,b] = [a-1,b] + [a,b-1] 공식

    return grid[n][m]