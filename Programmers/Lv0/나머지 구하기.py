"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/120810
"""
# 내 풀이
def solution(num1, num2):
    return num1 % num2

# 다른 사람 풀이
def solution(num1, num2):
    return divmod(num1, num2)[1]