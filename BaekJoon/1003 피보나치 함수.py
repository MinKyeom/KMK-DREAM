# 내 풀이
from collections import deque
n=int(input())
k=deque([])
for i in range(n):
    j=int(input())
    k.append(j)
while k:
    l=k.popleft()
    dp=[1]*(l+1)
    t=2
    while t<=l:
        dp[t]+=dp[t-1]+dp[t-2]


# 내 풀이(개선 중)
# 0과 1출력하는 횟수
# f(n)=f(n-1)+f(n-2)

"""
from collections import deque
n=int(input())
k=deque([])
for i in range(n):
    j=int(input())
    k.append(j)

while k:
    l=k.popleft()
    count_0=0
    count_1=0
    new=deque([l])
    while new:
        c=new.popleft()
        if c>=2:
            new.append(c-1)
            new.append(c-2)
        else:
            if c==1:
                count_1+=1
            elif c==0:
                count_0+=1

    print(count_0, count_1)
"""