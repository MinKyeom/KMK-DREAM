"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/181865
"""
# 내 풀이
def solution(binomial):
    return eval(binomial)

# 다른 사람 풀이
def solution(binomial):
    a, op, b = binomial.split()

    a = int(a)
    b = int(b)

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b

    return result
