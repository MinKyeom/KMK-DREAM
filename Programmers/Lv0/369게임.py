"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/120891
"""
#풀이1
def solution(order):
    answer = 0
    a=list(str(order))
    count=0
    for x in a:
        if not int(x)==0 and int(x)%3==0:
            count+=1
    answer=count
    return answer


#다른 사람 풀이

def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))