# 풀이 1

def solution(num, k):
    answer = 0
    a=str(num).find(str(k))
    if not a==-1:
        return a+1
    elif a==-1:
        return a
    return answer


# 다른 사람 풀이

def solution(num, k):
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1