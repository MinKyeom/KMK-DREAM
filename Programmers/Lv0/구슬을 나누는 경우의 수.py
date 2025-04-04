"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/120840
"""
# 내 풀이
def solution(balls, share):
    x=1
    y=1
    for a in range(balls-share+1,balls+1):
        x*=a
    for b in range(1,share+1):
        y*=b
    return x/y


# 다른 사람 풀이
import math


def solution(balls, share):
    return math.comb(balls, share)