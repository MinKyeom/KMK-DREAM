n,k=map(int,input().split())

trip=[]

for a in range(n):
    trip.append(list(map(int,input().split())))
trip_cost=[]
for x,y in trip:
    z=y/x
    trip_cost.append((z,x,y))

trip_cost.sort()
trip_cost.reverse()
count_weight=0
count_cost=0
for b in range(n):
    if count_weight+trip_cost[b][1]<=7:
        count_weight+=trip_cost[b][1]
        count_cost+=trip_cost[b][2]

print(count_cost)