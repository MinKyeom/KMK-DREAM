# 풀이 1

def solution(my_string, num1, num2):
    answer = ''
    a=list(my_string)
    b=a[num1]
    c=a[num2]
    a[num1]=c
    a[num2]=b
    answer="".join(a)
    return answer


# 다른 사람 풀이
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)