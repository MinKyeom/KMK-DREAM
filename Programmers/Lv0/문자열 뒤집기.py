"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/120822
"""
# 풀이 과정
def solution(my_string):
    result=list(my_string)
    result.reverse()
    result="".join(result)
    return result

# 다른 사람 풀이
def solution(my_string):
    return my_string[::-1]