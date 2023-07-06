# 내 풀이
def solution(number):
    from itertools import combinations
    result=0
    k=list(combinations(number,3))
    for x in range(len(k)):
        k[x]=list(k[x])
        if sum(k[x])==0:
            result+=1
    return result

# 다른 사람 풀이
def solution (number) :
    from itertools import combinations
    cnt = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt