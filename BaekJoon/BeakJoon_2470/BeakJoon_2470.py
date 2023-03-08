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
"""

"""
#4번 풀이

from sys import stdin
from itertools import combinations

N=int(stdin.readline())

Liquid=list(map(int,stdin.readline().split()))

Liquid_sum=[]

for x,y in combinations(Liquid,2):
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



"""
#5번 풀이 정답을 보고 난 후 풀이

N=int(input())
liquid=list(map(int,input().split()))
left=0
right=N-1
l=left #1
r=right #2
liquid.sort()

result=liquid[left]+liquid[right]

while left<right:
    tmp=liquid[left]+liquid[right]
    if abs(tmp)<abs(result):
        result=tmp
        l=left
        r=right
        if abs(result)==0:
            break
    if tmp>=0:
        right-=1

    else:
        left+=1

print(liquid[l],liquid[r])

#1,#2를 정의를 안했을 시에 왜 오류가 발생하는지 여부 
# 모든 경우의 수를 커버 할 수 있는가 여부 
"""



"""
#6번째 풀이
N=int(input())
liquid=list(map(int,input().split()))

left=0
right=N-1

liquid.sort()

result=liquid[left]+liquid[right]

t=1

l=left
r=right

while t<N-1:
        for x in range(N)[t:N]:
               tmp=liquid[left]+liquid[x]
               if abs(tmp) <= abs(result):
                   result=tmp
                   l=left
                   r=right
                   if abs(result)==0:
                       break
        t+=1
        left+=1

print(liquid[l],liquid[r])
"""

#최적일 수 밖에 없는 이유는 무엇일까?