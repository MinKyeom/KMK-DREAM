# 내 풀이
from collections import deque
c=int(input())
check=int(input())
g={}

for t in range(1,c+1):
    g[t]=[]


for k in range(check):
    i,j=list(map(int,input().split()))
    if not j in g[i]:
        g[i].append(j)
    if not i in g[j]:
        g[j].append(i)

visit=[1]
q=deque([1])

def dfs():
    v=q.popleft()

    for w in g[v]:
        if not w in visit:
            visit.append(w)
            q.append(w)
            dfs()
        else:
            continue

dfs()

print(len(visit)-1)