# 내 풀이
def solution(x):
    a=list(str(x))
    b=map(int,a)
    c=sum(b)
    return True if x%c==0 else False

# 다른 사람 풀이
def Harshad(n):
    return n%sum(int(x) for x in str(n)) == 0

print(Harshad(18))