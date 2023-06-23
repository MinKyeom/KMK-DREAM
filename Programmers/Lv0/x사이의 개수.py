# 내 풀이
def solution(myString):
    k=myString.split("x")
    result=[]
    for x in k:
        z=len(x)
        result.append(z)
    return result

# 다른 사람 풀이
def solution(myString):
    return [len(w) for w in myString.split('x')]