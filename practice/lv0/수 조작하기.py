# 내 풀이

def solution(n, control):
    for x in control:
        if x=="w":
            n+=1
        elif x=="s":
            n-=1
        elif x=="d":
            n+=10
        elif x=="a":
            n-=10
    return n


# 다른 사람 풀이

def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])
