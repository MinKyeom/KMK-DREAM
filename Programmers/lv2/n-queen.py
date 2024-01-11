# 내 풀이(개선 중)
from itertools import combinations


def solution(n):
    k = [[] for _ in range(n)]
    num = [a for a in range(n * n)]
    count = 0

    for i in range(n):
        for j in range(n):
            k[i].append(count)
            count += 1

    t = list(combinations(num, n))

    return 0


# 다른 사람 풀이
def solution(n):
    # 어태까지의 queen 위치 ls, 내가 두려는 위치 new
    def check(ls, new):
        for i in range(len(ls)):
            # 같은 열에 퀸을 둔 적이 있거나, 대각 위치에 둔 적이 있다면, return False
            if new == ls[i] or (len(ls) - i) == abs(ls[i] - new):
                return False
        return True

    def dfs(n, ls):
        # 끝 행까지 도달! return 1
        if len(ls) == n:
            return 1
        # 끝 행이 아니라면, 다음 줄을 다시 탐색
        cnt = 0
        for i in range(n):
            if check(ls, i):
                cnt += dfs(n, ls + [i])
        # 탐색 결과를 return
        return cnt

    return dfs(n, [])