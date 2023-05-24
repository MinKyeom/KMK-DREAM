# 내 풀이
def solution(num_list):
    x = sum(num_list)
    count = 1
    for a in range(len(num_list)):
        count *= num_list[a]

    if count < x ** 2:
        return 1
    else:
        return 0
# 다른 사람 풀이
def solution(num_list):
    s=sum(num_list)**2
    m=eval('*'.join([str(n) for n in num_list]))
    return 1 if s>m else 0

