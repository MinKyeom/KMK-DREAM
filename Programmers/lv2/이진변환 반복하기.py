"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/70129
"""
# 풀이 과정
def solution(s):
    count = 0
    count_0 = 0

    while True:
        count += 1
        count_0 += s.count("0")
        s = s.replace("0", "")
        s = len(s)
        s = str(bin(s))[2:]

        if s == "1":
            return [count, count_0]

    return 0

# 다른 사람 풀이
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]