# 풀이 1
def solution(s):
    answer = ''
    a=[]
    b=[]
    for x in list(s):
        if not x in a and not x in b:
            a.append(x)
        elif x in a:
            a.remove(x)
            b.append(x)
    a.sort()
    answer="".join(a)
    return answer

# 내 풀이 2
def solution(s):
    x=list(s)
    result=[]
    for a in x:
        if s.count(a)==1:
            result.append(a)
    y=result.sort()
    answer ="".join(result)
    return answer


# 다른 사람 풀이
def solution(s):
    answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
    return answer



# count 활용 