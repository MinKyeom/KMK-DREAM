# 내 풀이
def solution(arr):
    result=[]
    for x in arr:
        count=0
        while x>count:
            result.append(x)
            count+=1
    answer = result
    return answer
# 다른 사람 풀이
def solution(arr):
    answer = []
    for num in arr:
        answer += [num] * num
    return answer
