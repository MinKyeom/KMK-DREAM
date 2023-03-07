#1번째 풀이 방법
"""
from itertools import combinations

N=int(input())

Liquid=list(map(int,input().split()))

a=combinations(Liquid,2)

Liquid_sum=[]

for x,y in a:
    z=x+y
    b=abs(z)
    Liquid_sum.append((x,y,b))
    if len(Liquid_sum)>1:
        if Liquid_sum[0][2]>=Liquid_sum[1][2]:
            del Liquid_sum[0]

        elif Liquid_sum[0][2]<Liquid_sum[1][2]:
            del Liquid_sum[1]


if Liquid_sum[0][0]>=Liquid_sum[0][1]:
    print(Liquid_sum[0][1],Liquid_sum[0][0])
elif Liquid_sum[0][0]<Liquid_sum[0][1]:
    print(Liquid_sum[0][0],Liquid_sum[0][1])
"""

#2번째 풀이
"""
from sys import stdin
from itertools import combinations

N=int(stdin.readline())

Liquid=list(map(int,stdin.readline().split()))

a=combinations(Liquid,2)

Liquid_sum=[]

for x,y in a:
    z=x+y
    b=abs(z)
    Liquid_sum.append((x,y,b))
    if len(Liquid_sum)>1:
        if Liquid_sum[0][2]>=Liquid_sum[1][2]:
            del Liquid_sum[0]

        elif Liquid_sum[0][2]<Liquid_sum[1][2]:
            del Liquid_sum[1]


if Liquid_sum[0][0]>=Liquid_sum[0][1]:
    print(Liquid_sum[0][1],Liquid_sum[0][0])
elif Liquid_sum[0][0]<Liquid_sum[0][1]:
    print(Liquid_sum[0][0],Liquid_sum[0][1])
"""

#3번 풀이
import time
from sys import stdin
from itertools import combinations

N=int(stdin.readline())

Liquid=list(map(int,stdin.readline().split()))

sum_list=[]

start_time=time.time()
for x in range(N):
    a=Liquid[x]
    if x<N-1:
        for y in range(N)[x+1:N]:
            b=Liquid[y]
            c=a+b
            s=abs(c)
            sum_list.append((a,b,s))
            if len(sum_list) > 1:
                if sum_list[0][2] >= sum_list[1][2]:
                    del sum_list[0]

                elif sum_list[0][2] < sum_list[1][2]:
                    del sum_list[1]

if sum_list[0][0]>=sum_list[0][1]:
    print(sum_list[0][1],sum_list[0][0])
elif sum_list[0][0]<sum_list[0][1]:
    print(sum_list[0][0],sum_list[0][1])

end_time=time.time()
print("총 걸린 시간은",end_time-start_time)
