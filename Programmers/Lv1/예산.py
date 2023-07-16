# 내 풀이
def solution(d, budget):
    count=0
    num=0
    d.sort()
    for x in d:
        if count+x<=budget:
            count+=x
            num+=1
    return num
# 다른 사람 풀이
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
