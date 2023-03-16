from itertools import combinations
N=int(input())
Scale=list(map(int,input().split()))
list_weight=[]
count=0
for x in range(1,len(Scale)+1):
    for y in list(combinations(Scale,x)):
        for z in range(x):
            count+=y[z]
        list_weight.append(count)
        #print(list_weight)
        count=0

for a in range(1,1000000+1):
    if a not in list_weight:
        print(a)
        break




