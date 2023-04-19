import sys

t=int(sys.stdin.readline())
list=[]
for a in range(t):
    x,y=map(int,sys.stdin.readline().split())
    list.append((x,y))
count=0
for b,c in list:
    count+=b+c
    print(count)
    count=0



