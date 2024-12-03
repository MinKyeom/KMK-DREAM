"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/120850
"""
# 풀이 과정

def solution(my_string):
    a = "abcdefghijklmnopqrstuvwxyz"
    b = a.upper()
    result = []
    x = list(my_string)
    for c in range(len(x)):
        if x[c] in a or x[c] in b:
            continue
        else:
            result.append(x[c])
    result.sort()
    answer = map(int, result)

    return list(answer)


# 다른 사람 풀이

def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])
