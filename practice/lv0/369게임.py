#풀이1
def solution(order):
    answer = 0
    a=list(str(order))
    count=0
    for x in a:
        if not int(x)==0 and int(x)%3==0:
            count+=1
    answer=count
    return answer


#다른 사람 풀이

def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))