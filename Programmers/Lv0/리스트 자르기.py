"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/181897
"""
# 내 풀이
def solution(n, slicer, num_list):
    a = slicer[0]
    b = slicer[1]
    c = slicer[2]

    if n == 1:
        return num_list[0:b + 1]
    elif n == 2:
        return num_list[a:]
    elif n == 3:
        return num_list[a:b + 1]
    elif n == 4:
        return num_list[a:b + 1:c]
# 다른 사람 풀이
def solution(n, slicer, num_list):
    a, b, c = slicer
    return [num_list[:b + 1], num_list[a:], num_list[a:b + 1], num_list[a:b + 1:c]][n - 1]




