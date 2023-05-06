# 내 풀이
def solution(num_list):
    count_1=0
    count_2=0
    for a in num_list:
        if a%2==0:
            count_1+=1
        else:count_2+=1
    return [count_1,count_2]

# 다른 사람 풀이
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer