"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/49191
"""

# 내 풀이(개선 중)
from collections import defaultdict


def solution(n, results):
    answer = 0

    rank_win = defaultdict(list)
    rank_lose = defaultdict(list)

    for win, lose in results:
        rank_win[win].append(lose)
        rank_lose[lose].append(win)

    rank = [False] * (n + 1)

    while True:
        before = rank.count(False)

        for p in range(1, n + 1):
            if len(rank_win[p]) + len(rank_lose[p]) == (n - 1):
                rank[p] = n - len(rank_win[p])
            else:
                win = n + 1
                for w in rank_win[p]:
                    if rank[w] != False:
                        win = min(rank[w], win)
                lose = 0
                for l in rank_lose[p]:
                    if rank[l] != False:
                        lose = max(rank[l], lose)

                if win - lose == 2:
                    rank[p] = (l + n) // 2

        after = rank.count(False)

        if before == after:
            break

    return (n + 1) - rank.count(False)