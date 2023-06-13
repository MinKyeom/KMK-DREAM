# 내 풀이
def solution(my_string):
    result=[]
    for x in range(0,len(my_string)):
        result.append(my_string[x:len(my_string)+1])
    result.sort()
    return result

# 다른 사람 풀이

def solution(my_string):
    return sorted(my_string[i:] for i in range(len(my_string)))
