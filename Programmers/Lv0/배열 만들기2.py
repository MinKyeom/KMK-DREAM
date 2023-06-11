# 내 풀이
def solution(l, r):
    result=[]
    count=1
    while True:
        x=str(bin(count))
        y=x.replace("0b","")
        z=y.replace("1","5")
        if int(z)<l:
            count+=1
        elif int(z)>=1 and int(z)<=r:
            result.append(int(z))
            count+=1
        elif int(z)>r:
            break
    return result if len(result)>0 else [-1]

# 다른 사람 풀이

def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        if not set(str(num)) - set(['0', '5']):
            answer.append(num)
    return answer if answer else [-1]