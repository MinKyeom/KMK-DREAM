"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/388353
"""
# 풀이과정
"""
겉면에서 출발하는 bfs실시 후 도착 가능한 알파벳 제거
두 번 반복된 경우 적용할 필요 없음 모두 그냥 빼버리는게 가능

해당 알파벳 찾은 후 빈공간으로 bfs 적용하는 방식이 좀 더 효율적일거라 생각된다.
"""


def dfs(x, y):
    return 0


def solution(storage, requests):
    s = []

    for stor in storage:
        s.append(list(stor))

    print(s)

    for r in requests:
        if len(r) == 2:
            check = r[0]

        else:
            continue

    answer = 0
    return answer