"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/43165
"""

# 풀이 과정
def cal(check, a):
    new = []

    if len(check) == 0:
        new.append(a)
        new.append(-a)

    else:
        for k in check:
            t_1 = k + a
            t_2 = k - a
            new.append(t_1)
            new.append(t_2)

    return new


def solution(numbers, target):
    answer = 0
    check = []

    for a in numbers:
        check = cal(check, a)

    for b in check:
        if b == target:
            answer += 1

    return answer

# 다른 사람 풀이
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])