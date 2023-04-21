# 풀이 1
def solution(my_string):
    answer = ''
    a=list(my_string)
    b=[]
    for x in range(len(my_string)):
        if not a[x] in b:
            b.append(a[x])
        elif a[x] in b:
            continue
    answer="".join(b)
    return answer

# 풀이 2

def solution(my_string):
    return ''.join(dict.fromkeys(my_string))


