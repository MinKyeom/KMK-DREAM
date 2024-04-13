"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/181917
"""
# 내 풀이
def solution(x1, x2, x3, x4):
    if x1==False and x2==False:
        l=False
    else:
        l=True
    if x3==False and x4==False:
        m=False
    else:
        m=True

    return True if l==True and m==True else False


# 다른 사람 풀이
def solution(x1, x2, x3, x4):
    return (x1 | x2) & (x3 | x4)