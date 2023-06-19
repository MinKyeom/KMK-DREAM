# 내 풀이
def solution(myString):
    x=list(myString)
    for k in range(len(x)):
        if x[k]=="A" or x[k]=="a":
            x[k]="A"
        else:
            x[k]=x[k].lower()
    return "".join(x)
# 다른 사람 풀이
def solution(myString):
    return myString.lower().replace('a', 'A')
