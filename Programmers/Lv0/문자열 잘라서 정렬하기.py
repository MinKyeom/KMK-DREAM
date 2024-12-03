"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/181866
"""
# 풀이 과정
def solution(myString):
    k=myString.split("x")
    result=[]
    for x in k:
        if x=='':
            continue
        else:result.append(x)
    answer = result
    answer.sort()
    return answer
# 다른 사람 풀이
def solution(myString):
    return sorted(ch for ch in myString.split('x') if ch)
