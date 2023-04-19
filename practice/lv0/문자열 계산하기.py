# 풀이 1
def solution(my_string):
    answer = 0
    a = eval(my_string)
    answer = a

    return answer

#다른 사람 풀이
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))
