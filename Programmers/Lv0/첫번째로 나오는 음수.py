# 내 풀이
def solution(num_list):
    for x in range(len(num_list)):
        if num_list[x]<0:
            return x
    return -1
# 다른 사람 풀이
def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i]<0:return i
    return -1