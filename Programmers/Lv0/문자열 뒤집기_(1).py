# 내 풀이
def solution(my_string, s, e):
    answer=list(my_string)
    answer[s:e+1]=answer[s:e+1][::-1]
    return "".join(answer)

# 다른 사람 풀이
def solution(my_string, s, e):
    return my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:]