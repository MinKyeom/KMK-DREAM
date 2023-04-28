# 내 풀이
def solution(dots):
    from itertools import permutations
    for a,b in list(permutations(dots,2)):
        if a[0]==b[0]:
            y=abs(b[1]-a[1])
            break
    for c,d in list(permutations(dots,2)):
        if c[1]==d[1]:
            x=abs(d[0]-c[0])
            break
    return x*y

# 다른 사람 풀이

def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])