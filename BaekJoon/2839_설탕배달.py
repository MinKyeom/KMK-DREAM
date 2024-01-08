# 내 풀이
# 3,5
import heapq
from collections import deque

n = int(input())

q = deque([[n,0]])

count=0
flag=False

while q:
    i,j = q.popleft()

    if i == 0:
        flag=True
        print(j)
        break

    if i>=3:
        b=i-3
        q.appendleft([b,j+1])

    if i>= 5:
        a = i-5
        q.appendleft([a,j+1])

if len(q)==0 and flag==False:
    print(-1)
