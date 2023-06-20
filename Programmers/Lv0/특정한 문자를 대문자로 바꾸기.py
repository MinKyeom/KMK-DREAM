# 내 풀이
def solution(my_string, alp):
    x = alp.upper()
    my_string = my_string.replace(alp, x)

    return my_string
# 다른 사람 풀이
def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())