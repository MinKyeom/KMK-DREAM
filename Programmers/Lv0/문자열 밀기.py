"""
출처: 프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/120921
"""

# 풀이 과정
def solution(A, B):
    a = list(A)
    b = []
    count = 0
    answer = 0
    if A == B:
        return answer

    for y in range(1, len(a)):
        for x in range(len(a)):
            b.append(a[x - y])
        c = "".join(b)
        print(c)
        count += 1
        if c == B:
            answer = count
            break
        else:
            b.clear()
    if not c == B:
        answer = -1

    return answer

# 풀이2 (Team)
def solution(A, B):
    for i in range(len(A)):
        if A[-i:] + A[:-i] == B:
            return i
    return -1

# "a" + "b" == "ab" # Immutatble Sequence
# [1, 2] + [3, 4] = [1, 2, 3, 4] # list Mutable Sequence



# return을 하면 바로 함수 밖으로 나온다 return for문의 break 이다.