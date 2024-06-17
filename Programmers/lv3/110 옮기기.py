"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/77886
"""
# 내 풀이(개선 중)
"""
조건:0과 1로 이루어진 x를 바탕으로 주어진 s를 순서를 바꿔 최소값을 return 

생각방향: 110을 지속적으로 찾아내기
원래 s에 있는 형태의 110이 아니더라도 중간에 변형에 의하여 생긴 110 또한 존재

"""
from collections import deque


def solution(s):
    result = []

    check = []

    for i in s:
        i = i.replace("110", "x")
        print(i)
        num = i.count("x")
        print(num)

    return result