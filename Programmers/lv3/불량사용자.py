"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/64064
"""

# 내 풀이(개선 중)
from collections import defaultdict


def solution(user_id, banned_id):
    # 불량사용자 아이디 항목별 종류
    check = defaultdict(int)

    for i in banned_id:
        check[i] = 0

    for i in user_id:
        for j in banned_id:
            if len(i) == len(j):
                for k in range(len(i)):
                    if j[k] != "*" and i[k] == j[k]:
                        continue
                    elif j[k] == "*":
                        continue
                    else:
                        break
                else:
                    print(i, j)
                    check[j] += 1
                    break
            else:
                continue

    print(check)

    result = 1
    for num in check.values():
        result *= num

    return result