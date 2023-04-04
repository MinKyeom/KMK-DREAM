n,k=map(int,input().split())
j_num=[list(map(int,input().split())) for _ in range(n)]
bag=[int(input()) for _ in range(k)]
bag.sort()

price=[]

count=0

while j_num and count==k:
    for a in bag:
        for b in range(len(j_num)):
            if a>=j_num[b][0] :
                if len(price)==count-1:
                    price.append(j_num[b][1])
                    del j_num[b]
                if len(price)==count and price[-1]<j_num[b][1]:
                    c=price.pop()
                    price.append(j_num[b][1])
                    price







"""
import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jew = []
for _ in range(N):
    heapq.heappush(jew, list(map(int, sys.stdin.readline().split())))
bags = []
for _ in range(K):
    bags.append(int(sys.stdin.readline()))
bags.sort()

answer = 0
tmp_jew = []
for bag in bags:
    while jew and bag >= jew[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(jew)[1])
    if tmp_jew:
        answer -= heapq.heappop(tmp_jew)
    elif not jew:
        break
print(answer)
"""