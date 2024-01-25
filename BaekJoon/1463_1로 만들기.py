# 내 풀이
import heapq
from collections import deque
n=int(input())
count=0
check=deque([n])
flag=False
heap=[]

while True:
    i=check.popleft()
    if i==1:
        print(count)
        break
    if i%3==0:
        heapq.heappush(heap,i//3)
    if i%2==0:
        heapq.heappush(heap,i//2)
    if i>1:
        heapq.heappush(heap,i-1)

    if len(check)==0:
        check=[]
        check+=heap
        check=deque(check)
        heap=[]
        count+=1

# 다른 사람 풀이
