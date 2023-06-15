# 내 풀이
def solution(start, end):
    a=[num for num in range(end,start+1)]
    a.sort(reverse=True)
    return a
# 다른 사람 풀이

def solution(start, end):
    return [i for i in range(start,end-1,-1)]