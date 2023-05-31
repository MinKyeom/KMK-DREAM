# 내 풀이
def solution(num_list):
    num_1=[]
    num_2=[]
    for x in num_list:
        if x%2==0:
            num_2.append(str(x))
        else:num_1.append(str(x))
    sum_2="".join(num_2)
    sum_1="".join(num_1)
    return int(sum_2)+int(sum_1)

# 다른 사람 풀이
def solution(num_list):
    return int(''.join([str(x) for x in num_list if x % 2])) + int(''.join([str(x) for x in num_list if not x % 2]))

