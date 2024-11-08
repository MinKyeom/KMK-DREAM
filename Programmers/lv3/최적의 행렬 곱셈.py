"""
출처 프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/12942
"""
# 내 풀이_ 개선 중
import copy
from collections import deque


def solution(matrix_sizes):
    m = matrix_sizes
    dp = [0] * (len(m) - 1)

    check = deque(copy.deepcopy(m))

    result = 0

    for i in range(len(m) - 2):
        first = check[0][0] * check[0][1] * check[1][1] + check[0][0] * check[1][1] * check[2][1]
        sec = check[1][0] * check[1][1] * check[2][1] + check[0][0] * check[0][1] * check[2][1]

        if first < sec:
            result += check[0][0] * check[0][1] * check[1][1]
            new = [check[0][0], check[1][1]]
            check.popleft()
            check.popleft()
            check.appendleft(new)

        else:
            result += check[1][0] * check[1][1] * check[2][1]
            new = [check[1][0], check[2][1]]
            k = check.popleft()
            check.popleft()
            check.popleft()
            check.appendleft(new)
            check.appendleft(k)

    result += check[0][0] * check[0][1] * check[1][1]

    return result
# 내 풀이_ 개선 중
import copy


def solution(matrix_sizes):
    m = matrix_sizes
    m.append(0)
    q = [copy.deepcopy(m)]
    count = 1

    new_q = []

    while count < len(m) - 1:

        while q:
            k = q.pop()
            num = k.pop()

            for i in range(len(k) - 1):

                x1, y1 = k[i][0], k[i][1]
                x2, y2 = k[i + 1][0], k[i + 1][1]

                front = copy.deepcopy(k[:i])
                back = copy.deepcopy(k[i + 2:])

                if len(k) - 1 == 1:
                    new_q.append([[x1, y2], num + x1 * y1 * y2])
                else:
                    new = front + [[x1, y2]] + back
                    new_q.append(new + [num + x1 * y1 * y2])

        count += 1
        q += new_q
        new_q = []

    result = float("inf")

    for i, j in q:
        result = min(result, j)

    return result
# 내 풀이_개선 중
"""
큰 수를 여러 번 안쓰게 소거
"""
from collections import defaultdict, deque
import copy


def solution(matrix_sizes):
    m = matrix_sizes

    front = copy.deepcopy(m)
    back = copy.deepcopy(m)

    front = deque(sorted(front, key=lambda x: (-x[0])))
    back = deque(sorted(back, key=lambda x: (-x[1])))

    m = deque(m)

    result = []

    while len(front) > 1 and len(back) > 1:
        x, y = back.popleft()
        v, w = front.popleft()

        i = front.index([x, y])
        del front[i]
        j = back.index([v, w])
        del back[j]

        result.append(x * y * w)

        front.append([x, w])
        back.append([x, w])
        front = deque(sorted(front, key=lambda x: (-x[0])))
        back = deque(sorted(back, key=lambda x: (-x[1])))

        print(front, back)

    return sum(result)

# 다른 사람 풀이
import sys


def solution(matrix_sizes):
    answer = 0
    L = len(matrix_sizes)
    dp = [[0 for _ in range(L)] for _ in range(L)]

    for dist in range(1, L):  # dist는 곱할 두 행렬간의 간격
        for start in range(L - dist):  # start는 행렬곱의 시작 행렬
            a = start
            b = start + dist
            dp[a][b] = sys.maxsize
            for k in range(a, b):
                middle_product = matrix_sizes[a][0] * matrix_sizes[k][1] * matrix_sizes[b][1]
                dp[a][b] = min(dp[a][b], dp[a][k] + middle_product + dp[k + 1][b])
    return dp[0][-1]