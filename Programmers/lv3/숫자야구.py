"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/451808?language=python3
"""

# 풀이 과정
"""
조건:
숫자가 비밀번호에 포함되어 있지 않다면 : OUT
숫자가 비밀번호에 포함되어 있지만, 위치가 틀렸다면 : BALL
숫자가 비밀번호에 포함되어 있고, 위치까지 정확하다면 : STRIKE

목표: 비밀번호 맞추기
"""
def solution(n, submit):
    
    for i in range(1000, 10000):
        if submit(i) == "4S 0B": return i
    
    return 0