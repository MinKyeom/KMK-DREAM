"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/120585
"""
# 내 풀이
def solution(array, height):
    array.append(height)
    array.sort()
    array.reverse()
    return array.index(height)
# 다른 사람 풀이
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)

