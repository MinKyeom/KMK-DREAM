"""N,K=map(int,input().split()) #보석의 갯수, 가방의 갯수
list_m=[] #보석 무게
list_v=[] #보석 가격
list_c=[] #가방에 담는 최대 무게
result_list=[] #보석값

#목표:가격이 최대로 각 가방 당 보석 한 개

for x in range(N):
    M,V=map(int,input().split())
    list_m[x]=M
    list_v[x]=V

for y in range(K):
    C=int(input())
    list_c[y]=C

list_c.sort() #올림차순 정렬
list_c.reverse() # 그리고 내림차순을 위해 가방의 무게가 무거운부터 들어오게 정렬

for z in range(K):
    for r in range[N]:0
        if list_c[z]>=list_m[r]:
            a=list_v[r]
            if result_list[-1]>list_v[r]:
                result_list.pop()
                result_list.append(a)
                if len(result_list)==1:
                    break

"""


"""
 풀이1
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




