"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/120849
"""
# 내 풀이
def solution(my_string):
    minus="aeiou"
    new=[]
    for a in list(my_string):
        if a in minus:
            continue
        else:
            new.append(a)
    answer="".join(new)
    return answer

# 다른 사람 풀이
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])