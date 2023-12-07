# 내 풀이
"""
틀린 이유:
0 1번이 최소성을 유지해도
1 2 3이 최소성을 만들 수도 있다는걸 생각!
"""
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

    # 최소성을 만족하는 리스트 제거_하나로 완전한 집합 제거
    for e in range(len(relation[0])):
        i = k.popleft()
        if len(i) == len(set(i)):
            result += 1
        else:
            k.append(i)

    count = 2  # 조합 시작 수

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

            for e in range(len(k[0])):
                new_check = []

                for f in range(len(d)):
                    new_check.append(d[f][e])

                if new_check not in new_:
                    new_.append(new_check)

                else:
                    break

            if len(new_) == len(k[0]):
                all_d = []
                for a in d:
                    all_d += a

                all_check.append(all_d)

            else:
                continue

        count += 1

    # 최소성을 만족하는 수 구분
    final = []

    # print(all_check)
    all_check = deque(all_check)

    for a in all_check:
        flag = False
        for b in all_check:
            flag_in = False
            if a == b:
                continue
            elif len(a) <= len(b):
                continue
            elif len(a) > len(b):
                for c in b:
                    if c in a:
                        if a.count(c) >= b.count(c):
                            continue
                        else:
                            flag_in = True
                    else:
                        flag_in = True
                        break
            if flag_in == False:
                flag = True
                break
        if flag == False:
            final.append(a)
    print(final)
    return len(final) + result
# 다른 사람 풀이

def solution(relation):
    answer_list = list()
    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)

        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                if (num & i) == num:
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)
    return len(answer_list)