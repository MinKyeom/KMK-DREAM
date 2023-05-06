# 내 풀이
def solution(my_string, n):
    x = list(my_string)
    result = []
    for a in x:
        result.append(a * n)

    result = "".join(result)
    return result

# 다른 사람 풀이

def solution(my_string, n):
    return ''.join(i*n for i in my_string)