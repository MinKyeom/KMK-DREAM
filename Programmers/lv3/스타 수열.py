"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/70130
"""
# 내 풀이(개선 중)
"""
생각방향
# 부분수열의 모든 경우의 수를 비트마스크로 나타낸 후 스타수열 거르기
# 비트마스크로 부분수열을 만드는 과정에서 걸러야한다. 다 만든 후 거르면 시간 초과
"""
from itertools import combinations


def solution(a):
    k = []
    n = len(a) // 2
    result = 0

    num = int("1" * len(a))
    bit_mask = []

    # 부분 수열 만들기 & 1번 조건
    for i in range(1 << len(a)):
        sub = []
        for j in range(len(a)):
            if i & (1 << j):
                sub.append(a[j])

        bit_mask.append(sub)

        # bit_mask=sorted(bit_mask, key=lambda x:(len(x)))

        # 스타수열 찾기
        while bit_mask:
            check = bit_mask.pop()

            if len(check) % 2 == 1 or len(check) < 2:
                continue

            elif len(check) <= result:
                continue

            elif len(check) == 2:
                if len(set(check)) == 1:
                    continue
                result = max(result, len(check))
                continue

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
                    result = max(result, len(check))

    return result
# 내 풀이(개선 중)
"""
생각방향
# 부분수열의 모든 경우의 수를 비트마스크로 나타낸 후 스타수열 거르기
"""
from itertools import combinations

def solution(a):
    k = []
    n = len(a) // 2
    result = 0

    bit_mask = []

    # 부분 수열 만들기 & 1번 조건
    for i in range(1 << len(a)):
        sub = []
        for j in range(len(a)):
            if i & (1 << j):
                sub.append(a[j])
        bit_mask.append(sub)

    # bit_mask=sorted(bit_mask, key=lambda x:(len(x)))

    # 스타수열 찾기
    while bit_mask:
        check = bit_mask.pop()

        if len(check) % 2 == 1 or len(check) < 2:
            continue

        elif len(check) <= result:
            continue

        elif len(check) == 2:
            if len(set(check)) == 1:
                continue
            result = max(result, len(check))
            continue

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
                result = max(result, len(check))

    return result

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