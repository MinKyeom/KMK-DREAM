# 내 풀이
def solution(numLog):
    result=[]
    for x in range(0,len(numLog)-1):
        if numLog[x+1]-numLog[x]==1:
            result.append("w")
        elif numLog[x+1]-numLog[x]==-1:
            result.append("s")
        elif numLog[x+1]-numLog[x]==10:
            result.append("d")
        elif numLog[x+1]-numLog[x]==-10:
            result.append("a")
    return "".join(result)


# 다른 사람풀이

def solution(log):
    res=''
    joystick=dict(zip([1,-1,10,-10],['w','s','d','a']))
    for i in range(1,len(log)):
        res+=joystick[log[i]-log[i-1]]
    return res