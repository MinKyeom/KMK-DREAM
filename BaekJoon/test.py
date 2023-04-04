import heapq
list=[(1,2),(3,4),(5,6)]
list_2=[]
for x in list:
    heapq.heappush(list_2,x)
print(list_2)
print(list_2[0][1])

print(heapq.heappop(list_2))
