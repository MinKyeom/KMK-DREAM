# 내 풀이

def solution(my_string, index_list):
    result=[]
    for x in index_list:
        result.append(my_string[x])
    return "".join(result)

# 다른 사람 풀이
def solution(my_string, index_list):
    return ''.join([my_string[idx] for idx in index_list])