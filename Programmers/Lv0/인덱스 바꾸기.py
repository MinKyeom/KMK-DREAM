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

# 팀원 풀이
def solution(my_string, num1, num2):
    ml = list(my_string)
    ml[num1], ml[num2] = ml[num2], ml[num1]
    return "".join(ml)
# 위의 풀이가 가능한 이유: 평가가 오른쪽부터 되기 때문이다.
# 다른 사람 풀이
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)