# 내 풀이
def solution(my_string, overwrite_string, s):
    x = list(my_string)
    y = list(overwrite_string)
    for a in range(s, s + len(overwrite_string)):
        x[a] = y[a - s]

    answer = "".join(x)
    return answer

# 다른 사람 풀이

def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]