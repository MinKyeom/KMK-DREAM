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