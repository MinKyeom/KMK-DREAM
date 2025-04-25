"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/12949
"""
# 풀이 과정
from collections import deque


def solution(arr1, arr2):
    result = []

    new = []
    count = 0
    while count < len(arr2[0]):
        check = []
        for k in range(len(arr2)):
            check.append(arr2[k][count])
        new.append(check)
        count += 1

    arr1 = deque(arr1)

    while arr1:
        check = []
        i = arr1.popleft()

        for j in new:
            count = 0
            for v, w in zip(i, j):
                count += v * w
            check.append(count)

        result.append(check)

    return result

# 다른 사람 풀이
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [ [ 1, 2 ], [ 2, 3 ]];
b = [[ 3, 4], [5, 6]];
print("결과 : {}".format(productMatrix(a,b)));