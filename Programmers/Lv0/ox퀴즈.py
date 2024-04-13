"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/120907
"""
#
#풀이1

#(아예 못품)

#풀이2

def solution(quiz):
    return ["O" if x else "X" for x in map(eval, map(lambda x: x.replace("=", "=="), quiz))]