"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/388352
"""

# 풀이 과정
from itertools import combinations

"""
n: 가능한 자연수 개수 
q: 시도한 자연수 배열 집합
ans: 맞춘 자연수 개수 집합
> 스무고개 아이디어 생각!
"""


def solution(n, q, ans):
    check = [k + 1 for k in range(n)]

    num_list = list(combinations(check, len(q[0])))
    num_list = list(map(list, num_list))
    result = 0

    for n in num_list:
        for count, q_ in enumerate(q):
            if len(q[0]) * 2 - len(set(q_ + n)) == ans[count]:
                pass
            else:
                break
        else:
            result += 1

    return result
