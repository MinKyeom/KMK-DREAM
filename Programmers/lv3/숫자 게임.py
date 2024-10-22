"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/12987
"""

# 내 풀이
"""
permutations > 시간초과 
A의 가장 작은값 순으로 나열시 B가 이기는 경우가 최대이다 A의 큰 값에 한해선 져주는게 이득이다(승을 가장 많이 챙기기 위해)
A의 순서는 함정이다 어짜피 B는 그에 맞춰 대응할 수 있어 의미가 없다 그러므로 A의 순서는 자유롭게 바꾸고 그에 맞춰 최대 승수만 구하면 된다!
"""
from collections import deque


def solution(A, B):
    A.sort()
    B.sort()

    A = deque(A)
    B = deque(B)

    result = 0

    while A:
        a = A.popleft()

        while B:
            b = B.popleft()

            if b > a:
                result += 1
                break

        if len(B) == 0:
            break

    return result

# 다른 사람 풀이
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    j = 0

    for i in range(len(A)):
        if A[j] < B[i]:
            answer = answer + 1
            j = j+1

    return answer