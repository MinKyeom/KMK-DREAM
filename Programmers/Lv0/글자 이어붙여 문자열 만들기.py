"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/181915
"""
# 내 풀이

def solution(my_string, index_list):
    result=[]
    for x in index_list:
        result.append(my_string[x])
    return "".join(result)

# 다른 사람 풀이
def solution(my_string, index_list):
    return ''.join([my_string[idx] for idx in index_list])