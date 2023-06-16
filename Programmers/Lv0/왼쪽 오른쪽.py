# 내 풀이
def solution(str_list):
    result=[]
    for x in range(len(str_list)):
        if str_list[x]=="l":
            result=str_list[:x]
            return result
        elif str_list[x]=="r":
            result=str_list[x+1:]
            return result
    return []

# 다른 사람 풀이
def solution(str_list):
    for i in range(len(str_list)):
        if str_list[i]=='l': return str_list[:i]
        elif str_list[i]=='r': return str_list[i+1:]
    return []