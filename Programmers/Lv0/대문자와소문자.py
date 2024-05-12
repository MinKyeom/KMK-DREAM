"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/120893
"""
#풀이 1
def solution(my_string):
    answer = ''
    a = list(my_string)

    for x in range(len(a)):
        if a[x] == my_string.lower()[x]:
            a[x] = my_string.upper()[x]

        else:
            a[x] = my_string.lower()[x]
    answer = "".join(a)
    return answer
# 풀이 2

def solution(my_string):
    x=list(my_string)
    for a in range(len(x)):
        if x[a]==x[a].upper():
            x[a]=x[a].lower()
        else:x[a]=x[a].upper()
    answer = "".join(x)
    return answer

#다른 사람 풀이, 팀원 풀이

def solution(my_string):
    return my_string.swapcase()



# 임시 변수 개념 잘알아두기