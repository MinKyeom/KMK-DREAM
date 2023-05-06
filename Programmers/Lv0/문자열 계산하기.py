# 풀이 1
def solution(my_string):
    answer = 0
    a = eval(my_string)
    answer = a

    return answer

# 풀이 2
def solution(my_string):
    x=eval(my_string)
    answer = x
    return answer

#팀원 풀이
def solution(my_string):
    return eval(my_string)

#다른 사람 풀이
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))
