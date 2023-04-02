import sys
n=int(input())
pic=[]
for a in range(n):
    pic.append(list(map(str,sys.stdin.readline())))
dx=[-1,0,1,0]
dy=[0,-1,0,1]

def find (x,y): #주변 탐지
    count=0
    for e,f in dx,dy:
        if pic[x+e][y+f]==pic[x][y]:
            count+=1
    return count

for b in range(n):
    for c in range(n):
        z=find(b,c)
        if z>0:
            continue




