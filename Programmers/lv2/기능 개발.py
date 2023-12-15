# 내 풀이
def solution(progresses, speeds):
    from collections import deque

    p = deque(progresses)
    s = deque(speeds)
    result = []
    count = 0  # 작업 개수
    check = len(p)  # 1사이클

    while p:
        count += 1
        a = p.popleft()
        b = s.popleft()

        a += b

        p.append(a)
        s.append(b)

        if count == check:
            finish = 0
            for f in list(p):
                if f >= 100:
                    p.popleft()
                    s.popleft()
                    finish += 1
                else:
                    break
            if finish != 0:
                result.append(finish)
                check = len(p)
                count = 0
            else:
                check = len(p)
                count = 0

    return result

# 다른 사람 풀이
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]