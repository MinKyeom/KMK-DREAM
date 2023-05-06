# 내 풀이
def solution(my_string, letter):
    x=list(my_string)
    result=[]
    for a in x:
        if not a==letter:
            result.append(a)
    result="".join(result)
    return result

# 다른 사람 풀이

def solution(my_string, letter):
    return my_string.replace(letter, '')
