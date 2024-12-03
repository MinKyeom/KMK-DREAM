"""
출처: 프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/181871
"""
# 풀이 과정
def solution(myString, pat):
    result = []
    for x in range(len(myString)):
        k = myString.find(pat, x)
        result.append(k)

    return len(set(result) - {-1})
# 다른 사람 풀이
def solution(myString, pat):
    answer = 0
    for i, x in enumerate(myString) :
        if myString[i:].startswith(pat) :
            answer += 1
    return answer
