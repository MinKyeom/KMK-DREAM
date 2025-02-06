"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/87390

"""

# 풀이 과정
def solution(n, left, right):
    """
    #1
    #my idea:bfs
    from collections import deque

    k=[ [False for a in range(n)] for b in range(n) ]

    k[0][0]=1

    q=deque([[0,0]])

    while q:
        c,d=q.popleft()

        if c+1<n and d+1<n:
            if k[c+1][d+1]==False:
                k[c+1][d+1]=k[c][d]+1
                q.append([c+1,d+1])
        if c+1<n:
            if k[c+1][d]==False:
                k[c+1][d]=k[c][d]+1
                q.append([c+1,d])
        if d+1<n:
            if k[c][d+1]==False:
                k[c][d+1]=k[c][d]+1
                q.append([c,d+1])
    check=[]
    for e in k:
        check+=e

    return check[left:right+1]
    """

    """
    #2
    result=0

    k=[a+1 for a in range(n)]

    for b in range(n):
        k=k+[b+2]*(b+1)+[c+1 for c in range(b+1,n) ]


    return k[left:right+1]
    """
    """
    #3
    #idea: n이 10만 그러므로 한 번의 루프안에 답까지 나와야한다! 
    # def solution(n, left, right):
    count=0 

    v,w=left%n, int((left)/n)
    x,y=right%n , int((right)/n)

    #print(v,w)

    k=[]
    #left
    if v<=w:
        k=[w+1]*(w-v)

    else:
        pass


    k=k+[a+1 for a in range(0,n) if a>(w+1)]

    #print(k,"left")

    #middle

    for b in range(w+1,y):
        k=k+[b+1]*(b+1)+[c+1 for c in range(b+1,n)]

    print(k,"middle")

    #right
    r=[]
    if x<y:
        r=[y+1]*(x+1)
    else:
        r=[y+1]*(x)+[c for c in range(1,n+1) if c>x]

    #print(r,"right")

    result=k+r

    #print(result)
    """

    # 4
    count = left
    result = []
    k = 1  # 내부에 들어갈 수
    num = left % n + 1  # 내부 체크 수

    while count <= right:
        if int(count / n) + 1 >= num and num <= n:
            k = int(count / n) + 1
            if count >= left and count <= right:
                result.append(k)
            num += 1
            count += 1

        elif int(count / n) + 1 < num and num <= n:
            if count >= left and count <= right:
                result.append(num)
            num += 1
            count += 1

        if num > n:
            num = 1

    return result

# 다른 사람 풀이
    def solution(n, left, right):
        answer = []
        for i in range(left, right + 1):
            answer.append(max(i // n, i % n) + 1)
        return answer