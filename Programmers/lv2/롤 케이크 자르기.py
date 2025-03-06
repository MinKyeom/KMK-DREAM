"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/132265
"""
# 풀이과정
def solution(topping):
    from collections import Counter
    k = Counter(topping)
    check = set()
    result = 0

    for a in topping:
        k[a] -= 1
        check.add(a)
        if k[a] == 0:
            del k[a]

        if len(k) == len(check):
            result += 1

    return result

# 다른 사람 풀이
def solution(topping):
    answer = 0

    l, r = 0, len(topping)
    idx1 = 0
    while l <= r:
        m = (l + r) // 2
        left = len(set(topping[:m]))
        right = len(set(topping[m:]))
        if left < right:
            l = m + 1
        elif left >= right:
            idx1 = m
            r = m - 1

    l, r = 0, len(topping)
    idx2 = 0
    while l <= r:
        m = (l + r) // 2
        left = len(set(topping[:m]))
        right = len(set(topping[m:]))
        if left <= right:
            idx2 = m
            l = m + 1
        elif left > right:
            r = m - 1

    answer = max(idx2 - idx1 + 1, 0)

    return answer

# 다른 사람 풀이
from collections import Counter

def solution(topping):
    answer = 0
    dic = Counter(topping)
    set_dic = set()
    answer = 0

    for i in topping:
        dic[i] -= 1
        set_dic.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            answer += 1

    return answer
