# 내 풀이 (개선 중)
"""
틀린 이유:
0 1번이 최소성을 유지해도
1 2 3이 최소성을 만들 수도 있다는걸 생각!
"""


def solution(relation):
    from itertools import combinations
    from collections import deque
    result = 0
    k = [[] for t in range(len(relation[0]))]

    for a in range(len(relation)):
        for b in range(len(relation[a])):
            k[b].append(relation[a][b])
    k = deque(k)

    # 최소성을 만족하는 리스트 제거_ 하나로 완전함
    for e in range(len(relation[0])):
        i = k.popleft()
        if len(i) == len(set(i)):
            result += 1
        else:
            k.append(i)

    count = 1  # 조합 시작 수

    all_check = []  # 모든 만족 수 체크

    while True:
        check_k = []

        if len(k) >= count:
            check = deque(list(combinations(k, count)))
        else:
            break

        while check:
            d = check.popleft()
            new_ = []  # 비교군
            # print(d)
            for e in range(len(k[0])):
                new_check = []  # 비교 원소

                for f in range(len(d)):
                    new_check.append(d[f][e])

                if new_check not in new_:
                    new_.append(new_check)

                else:
                    break

            # print(new_)

            if len(new_) == len(k[0]):
                k_num = []  # 리스트 순서 체크

                for a in d:
                    n = k.index(a)
                    k_num.append(n)

                all_check.append(k_num)

            else:
                continue

        count += 1
    print(all_check)
    # 최소성을 만족하는 수 구분
    final = []

    all_check = deque(all_check)

    while all_check:
        t = all_check.pop()
        flag = False
        for a in all_check:
            if set(a) & set(t) == set(a):
                flag = True
                break
        if flag == False:
            final.append(t)
    return len(final) + result

# 다른 사람 풀이