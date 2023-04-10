import heapq
a=[(1,2),(3,4),(5,6)]
b=[]
c=heapq.heappop(a)[1]
print(c)
print(a)

if not b:
    print("확인")
else:
    print("확인불가")


