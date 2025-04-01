"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/12941
"""
# 풀이 과정
def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)

    result = 0

    print(A, B)
    for k in range(len(A)):
        result += A[k] * B[k]

    return result


# 다른 사람 풀이
def getMinSum(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])

print(getMinSum([1, 2], [3, 4]))
