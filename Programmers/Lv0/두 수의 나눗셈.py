"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/120806
"""
# 내 풀이
def solution(num1, num2):
    x=float(num1/num2)*1000
    return int(x)
# 다른 사람 풀이
def solution(num1, num2):
    return int(num1 / num2 * 1000)