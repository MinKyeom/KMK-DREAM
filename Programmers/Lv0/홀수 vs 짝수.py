# 내 풀이
def solution(num_list):
    x=num_list[::2]
    y=num_list[1::2]
    if sum(x)==sum(y):
        return sum(x)
    return sum(x) if sum(x)>sum(y) else sum(y)
# 다른 사람 풀이
def solution(num_list):
    return max(sum(num_list[0: len(num_list): 2]), sum(num_list[1: len(num_list): 2]))