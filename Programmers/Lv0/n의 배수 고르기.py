"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/120905
"""

# 내 풀이

def solution(n, numlist):
    answer = []
    for x in numlist:
        if x % n == 0:
            answer.append(x)
    return answer


# 내 풀이 2

def solution(n, numlist):
    answer = []
    for x in numlist:
        if x%n==0:
            answer.append(x)
        else:continue
    return answer

# 팀원 풀이

def solution(n, numlist):
    return [num for num in numlist if num % n == 0]

# 다른 사람들 풀이

def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))