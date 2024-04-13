"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/181888
"""
# 내 풀이
def solution(num_list, n):
    x=num_list[::n]
    answer = x
    return answer
# 다른 사람 풀이
def solution(num_list, n):
    return num_list[::n]