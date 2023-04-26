#내 풀이 1

def solution(num, k):
    answer = 0
    a=str(num).find(str(k))
    if not a==-1:
        return a+1
    elif a==-1:
        return a
    return answer
# 내 풀이 2

def solution(num, k):
    if str(num).count(str(k)):
        a = list(str(num)).index(str(k))
        return a + 1
    else:
        return -1

# 팀원 풀이
def solution(num, k):
    x = str(num).find(str(k))
    return x+1 if x >= 0 else x


# 다른 사람 풀이

def solution(num, k):
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1