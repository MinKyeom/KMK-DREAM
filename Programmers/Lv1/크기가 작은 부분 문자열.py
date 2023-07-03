# 내 풀이
def solution(t, p):
    num=[]

    count=0
    while True:
        l=""
        for x in range(count,count+len(p)):
            l+=t[x]
        if int(l)<=int(p):
            num.append(l)
        count+=1
        if (count+len(p))>len(t):
            break
    return len(num)
# 다른 사람 풀이
def solution(t, p):
    answer = 0

    for i in range(len(t) - len(p) + 1):
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1

    return answer
