import heapq
a=[1,5,3,2,4]
a.sort()
print(a)
count=0

count+=a[0]
print(count)
heapq.heappop(a)
print(a)
count+=a[0]
print(count)

