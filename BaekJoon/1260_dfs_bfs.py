# 내 풀이
from collections import deque

n, m, v = list(map(int, input().split()))
g = {}

for j in range(1,n+1):
    g[j]=[]

for i in range(m):
    a, b = list(map(int, input().split()))
    if not a in g:
        g[a] = [b]
    elif a in g and not b in g[a]:
        g[a].append(b)
    if not b in g:
        g[b] = [a]
    elif b in g and not b in g[b]:
        g[b].append(a)

for k in g:
    g[k].sort()


visit_dfs = [v]
visit_bfs = [v]

q_dfs=deque([v])
q_bfs=deque([v])

def dfs(g):
    q=q_dfs.popleft()
    for a in g[q]:
        if not a in visit_dfs:
            visit_dfs.append(a)
            q_dfs.append(a)
            dfs(g)

        else:
            continue

def bfs(g):
    while q_bfs:
        q=q_bfs.popleft()
        for b in g[q]:
            if not b in visit_bfs:
                visit_bfs.append(b)
                q_bfs.append(b)
            else:
                continue



dfs(g)
bfs(g)

visit_dfs=list(map(str,visit_dfs))
visit_dfs=" ".join(visit_dfs)
visit_bfs=list(map(str,visit_bfs))
visit_bfs=" ".join(visit_bfs)

print(visit_dfs)
print(visit_bfs)

