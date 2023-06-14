# 내 풀이
def solution(my_string, is_suffix):
    result=[]
    for x in range(0,len(my_string)):
        result.append(my_string[x:len(my_string)+1])
    return 1 if is_suffix in result else 0

# 다른 사람 풀이
def solution(m, s):
    if m[-len(s):]==s: return 1
    return 0