"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/70130
"""
# 내 풀이(개선 중)
"""
생각방향
"""
from itertools import combinations


def solution(a):
    k = []
    n = len(a) // 2

    for i in range(1, n):
        j = list(combinations(a, i * 2))
        k += j

    # 스타수열 찾기

    result = 0

    while k:
        check = k.pop()

        if len(check) == 2:
            return 2

        # 2번 조건 확인
        common = set([check[0], check[1]]) & set([check[2], check[3]])

        if len(common) == 0:
            continue

        else:
            for s in range(0, len(check), 2):
                common = set([check[s], check[s + 1]]) & common
                if len(common) == 0 or check[s] == check[s + 1]:
                    break
            else:
                return len(check)

    return result