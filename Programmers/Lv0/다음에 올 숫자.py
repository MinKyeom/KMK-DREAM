"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/120924
"""
#1 풀이 (정답 나옴!)
"""

common=[1, 2, 3, 4]
def solution(common):
    for x in range(3):
        if x == 0:
            a = common[0]
        elif x == 1:
            b = common[1]
        elif x == 2:
            c = common[2]
    r=0
    d=0
    if b - a == c - b:
        d = b - a
    elif (b / a) == (c / b):
        r = b / a
    if not r == 0:
        result = (common[len(common) - 1] * r)
    else:
        result = (common[len(common) - 1] + d)

    answer = result
    return answer
z=solution(common)
print(z)

"""

#2 풀이 (team sol)
# def solution(common):
#     answer = 0
#     x = common[1]-common[0]
#     y = common[-1]-common[-2]
#
#     if x != y:
#         answer = common[-1]*(common[-1]//common[-2])
#     else:
#         answer = common[-1]+x
#     return answer


