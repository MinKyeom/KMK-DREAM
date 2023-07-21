# 내 풀이
def solution(s):
    k=s.split(" ")
    result=[]
    for x in k:
        y=list(x)
        for z in range(len(y)):
            if z%2==0:
                y[z]=y[z].upper()
            else:
                y[z]=y[z].lower()
        y="".join(y)
        result.append(y)
    return " ".join(result)

# 다른 사람 풀이
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))