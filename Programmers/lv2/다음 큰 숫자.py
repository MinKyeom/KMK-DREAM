"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/12911
"""
# 풀이 과정
def solution(n):
    a = bin(n)
    b = a[2:]
    c = b.count("1")
    k = n

    while True:
        k += 1
        t = bin(k)
        v = t[2:].count("1")
        if v == c:
            return k

    answer = 0
    return answer

# 다른 사람 풀이
def nextBigNumber(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n

#아래 코드는 테스트를 위한 출력 코드입니다.
print(nextBigNumber(78))