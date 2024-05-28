"""
프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/87391
"""
# 내 풀이(개선 중)
# command 0,1:열 y
i = []

# command 2,3:행 x
j = []

for command, dx in queries:
    if command == 0:
        i.append(-dx)
    elif command == 1:
        i.append(dx)
    elif command == 2:
        j.append(-dx)
    elif command == 3:
        j.append(dx)
# 열
one = []

# 행
two = []

q = [y]

for a in range(len(i) - 1, -1, -1):
    b = i[a]
    new = []

    while q:
        c = q.pop()

        if c == 0 or c == m - 1:
            # 0쪽에 가까움
            if c == 0:
                for d in range(m):
                    if d + b <= 0:
                        new.append(d)
                    else:
                        break
            else:
                for d in range(m - 1, -1, -1):
                    if d + b >= m - 1:
                        new.append(d)
                    else:
                        break
        else:
            new.append(c + b * (-1))

    new = list(set(new))
    q += new

one += q

q = [x]

for a in range(len(j) - 1, -1, -1):
    b = j[a]
    new = []

    while q:
        c = q.pop()

        if c == 0 or c == n - 1:
            # 0쪽에 가까움
            if c == 0:
                for d in range(n):
                    if d + b <= 0:
                        new.append(d)
                    else:
                        break
            else:
                for d in range(n - 1, -1, -1):
                    if d + b >= n - 1:
                        new.append(d)
                    else:
                        break
        else:
            new.append(c + b * (-1))

    new = list(set(new))
    q += new
two += q

return len(one) * len(two)

# 내 풀이(개선 중)
"""
명령어: 0:열 번호 감소 1:열 번호 증가 2:행 번호 감소 3:행 번호 증가

생각방향:
도착점에서 역으로 쿼리를 시행 후 멈추는 점들의 개수를 구하면 시작점의 개수라는 생각 접근
>생각 정리 모호

일반적인 생각 n,m에 해당되는 모든 번호를 실행 후 도착점에 도착하는지 확인
>10**9라 불가능 

#역순으로 구하면서 행과 열을 구분지어 각각의 수를 구한 후 동시라는 확률을 구하기위해 각각을 모두 곱해져구면서 접근 순서쌍을 구하기 위해서
# 도착 지점을 역순으로 한다해도 도착 지점 또한 원래 목적지가 다른데 멈춰서 거기에 도달할 가능성 생각
"""
from collections import deque


def solution(n, m, x, y, queries):
    # 명령어: 0:열 번호 감소 1:열 번호 증가 2:행 번호 감소 3:행 번호 증가
    result = 0
    v, w = x, y

    # sol: 틀린 풀이
    """
    for i in range(len(queries)-1,-1,-1):
        command=queries[i][0]
        dx=queries[i][1]

        if command==0:
            w+=dx

            if w>m-1:
                result+=min(w-(m-1),m-1)
                w=m-1

            print(0,result)

        elif command==1:
            w-=dx

            if w<0:
                result+=min(abs(w),m)
                w=0

            print(1,result)

        elif command==2:
            v+=dx

            if v>n-1:
                result+=min(v-(n-1),n)
                v=n-1

            print(2,result)

        elif command==3:
            v-=dx

            if v<0:
                result+=min(abs(v),n)
                v=0

            print(3,result)

        print("v",v,"w",w)
        """

    # sol2: 시간 초과
    """
    # command 0,1:열
    i=[]

    # command 2,3:행
    j=[]

    for command,dx in queries:
        if command==0:
            i.append(-dx)
        elif command==1:
            i.append(dx)
        elif command==2:
            j.append(-dx)
        elif command==3:
            j.append(dx)

    one=[]

    for a in range(m):
        v=a
        for b in i:
            v+=b
            if v<0:
                v=0
            elif v>m-1:
                v=m-1

        if v==y:
            one.append(a)

    two=[]

    for a in range(n):
        w=a
        for b in j:
            w+=b
            if w<0:
                w=0
            elif w>n-1:
                w=n-1

        if w==x:
            two.append(a)

    return len(one)*len(two)
    """

    # sol3 도착점에 대한 생각부족 도착점 또한 목적지가 다름에도 멈춰서 거기에 있을 가능성 생각
    """
    # command 0,1:열
    i=[]

    # command 2,3:행
    j=[]

    for command,dx in queries:
        if command==0:
            i.append(-dx)
        elif command==1:
            i.append(dx)
        elif command==2:
            j.append(-dx)
        elif command==3:
            j.append(dx)

    one=[y]

    for a in range(len(i)-1,-1,-1):
        v=i[a]*(-1)
        new=[]

        while one:
            b=one.pop()
            b+=v

            if b<0:
                for c in range(abs(b)+1):
                    if c<m:
                        new.append(c)
                    else:
                        break

            elif b>m-1:
                for c in range(m-1,b+1):
                    if m-1-(c-m-1)>=0:
                        new.append(m-1-(c-m-1))
                    else:
                        break

            else:
                new.append(b)

            print(new)

        new=list(set(new))

        one+=new
        """

    return 0

