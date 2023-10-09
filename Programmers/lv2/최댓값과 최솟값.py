# 내 풀이
def solution(s):
    k=s.split(" ")
    k=list(map(int,k))
    answer=str(min(k))+" "+str(max(k))
    return answer

# 다른 사람 풀이
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))
