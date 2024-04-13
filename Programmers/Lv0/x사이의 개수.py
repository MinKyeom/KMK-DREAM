"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/181867
"""
# 내 풀이
def solution(myString):
    k=myString.split("x")
    result=[]
    for x in k:
        z=len(x)
        result.append(z)
    return result

# 다른 사람 풀이
def solution(myString):
    return [len(w) for w in myString.split('x')]