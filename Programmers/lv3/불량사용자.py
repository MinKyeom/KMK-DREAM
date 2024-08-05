"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/64064
"""
# 내 풀이
from collections import deque


def solution(user_id, banned_id):
    # 불량사용자 아이디 항목별 종류
    check = [[] for _ in range(len(banned_id))]

    if len(banned_id) == 0:
        return 0

    for num in range(len(banned_id)):
        for j in user_id:
            ban = banned_id[num]

            if len(ban) == len(j):
                for i in range(len(ban)):
                    if ban[i] != "*" and ban[i] != j[i]:
                        break
                    elif ban[i] == "*":
                        continue
                else:
                    check[num].append(j)

            else:
                continue

    if len(banned_id) == 1:
        return len(set(check[0]))

    result = []
    q = deque([])

    # 기본 큐 만들기
    for k in check[0]:
        q.append([k])

    for ban in range(1, len(banned_id)):
        add_mem = []
        for new in check[ban]:
            for before in q:
                add_mem.append(before + [new])

        q = deque([])
        q += add_mem
        count = len(q)
        while count > 0:
            t = q.popleft()
            count -= 1
            if len(t) != len(set(t)):
                continue
            else:
                q.append(t)

    result = []

    for r in add_mem:
        k = set(r)
        if len(r) == len(k):
            if len(result) == 0:
                result.append(k)

            else:
                for n in result:
                    if len(n - k) == 0:
                        break
                else:
                    result.append(k)

    return len(result)

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