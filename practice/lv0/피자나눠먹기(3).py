# 내 풀이
def solution(slice, n):
    pizza=0
    while True:
        if int(slice*pizza/n)>=1:
            return pizza
        else:pizza+=1


# 다른 사람 풀이

def solution(slice, n):
    return ((n - 1) // slice) + 1