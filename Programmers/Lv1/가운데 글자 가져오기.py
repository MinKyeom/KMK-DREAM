# 내 풀이
def solution(s):
    if len(s)%2==0:
        k=int(len(s)/2)
        return s[k-1:k+1]
    else:
        k=int(len(s)/2)
        return s[k:k+1]

# 다른 사람 풀이
def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2 + 1]