"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/49191
"""
# 내 풀이
from collections import defaultdict
from collections import deque


def solution(n, results):
    rank_win = defaultdict(set)
    rank_lose = defaultdict(set)

    for win, lose in results:
        rank_win[win].add(lose)
        rank_lose[lose].add(win)

    # 이긴 플레이 경로 재구성
    for player in range(1, n + 1):
        visit = [False] * (n + 1)
        visit[0] = True
        visit[player] = True

        q = deque([player])

        while q:
            opponent = q.popleft()
            visit[opponent] = True

            for i in rank_win[opponent]:
                if visit[i] == False:
                    q.append(i)
                    rank_win[player].add(i)

    # 진 플레이들 재구성
    for player in range(1, n + 1):
        visit = [False] * (n + 1)
        visit[0] = True
        visit[player] = True

        q = deque([player])

        while q:
            opponent = q.popleft()
            visit[opponent] = True

            for i in rank_lose[opponent]:
                if visit[i] == False:
                    q.append(i)
                    rank_lose[player].add(i)

    # 결과를 알 수 있는 플레이를 검색
    answer = 0

    for player in range(1, n + 1):
        if len(rank_win[player] | rank_lose[player]) == n - 1:
            answer += 1

    return answer

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