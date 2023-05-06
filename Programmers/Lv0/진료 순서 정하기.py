# 내 풀이
def solution(emergency):
    num=[]
    for x in range(len(emergency)):
        count=1
        for y in emergency:
            if emergency[x]<y:
                count+=1
            else:continue
        num.append(count)
    return num

# 다른 사람 풀이

def solution(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]