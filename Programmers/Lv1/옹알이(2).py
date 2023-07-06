# 내 풀이
def solution(babbling):
    mal=["aya", "ye", "woo", "ma"]
    mal_2=[(d+d) for d in mal]
    print(mal_2)
    count=0
    for x in babbling:
        check=0
        for c in mal_2:
            if c in x:
                check=1
                break
        if check==1:
            continue
        k=list(x)
        check=[]
        for y in k:
            check.append(y)
            if "".join(check[-2:]) in mal:
                for z in range(2):
                    check.pop()
                if len(check)!=0:
                    break
            elif "".join(check[-3:]) in mal:
                for z in range(3):
                    check.pop()
                if len(check)!=0:
                    break
        if len(check)==0:
            count+=1
    return count
# 다른 사람 풀이
def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer
