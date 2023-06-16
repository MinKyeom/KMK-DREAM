# 내 풀이
def solution(num_list, n):
    x = num_list[n:] + num_list[:n]

    return x
# 다른 사람 풀이
def solution(num_list, n):
    return num_list[n:] + num_list[:n]