# 내 풀이
def solution(my_string, is_prefix):
    result=[]
    for x in range(len(my_string)):
        result.append(my_string[0:x])
    return 1 if is_prefix in result else 0
# 다른 사람 풀이
def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))


