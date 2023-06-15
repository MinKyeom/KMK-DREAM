# 내 풀이
def solution(my_string, indices):
    result=[]
    for x in range(len(my_string)):
        if x in indices:
            continue
        else:result.append(my_string[x])
    answer = ''.join(result)
    return answer

# 다른 사람 풀이
def solution(my_string, indices):
    answer = ''
    for i in range(len(my_string)):
        if i not in indices:answer+=my_string[i]
    return answer