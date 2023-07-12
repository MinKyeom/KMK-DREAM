# 내 풀이
def solution(numbers):
    from itertools import combinations
    result=[]
    k=list(combinations(numbers,2))
    for x in range(len(k)):
        p=sum(list(k[x]))
        result.append(p)
    result= list(set(result))
    result.sort()
    return result

# 다른 사람 풀이
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))
