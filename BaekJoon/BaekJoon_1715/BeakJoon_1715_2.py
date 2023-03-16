import sys
import heapq

n=int(input())

card=[]

for x in range(n):
    card.append(int(sys.stdin.readline()))

heapq.heapify(card)
count=0
a=0
b=0

while len(card)>=2:
        a=heapq.heappop(card)
        b=heapq.heappop(card)
        count+=a+b
        heapq.heappush(card,a+b)
print(count)

# 최대한 줄 수를 줄이자!



