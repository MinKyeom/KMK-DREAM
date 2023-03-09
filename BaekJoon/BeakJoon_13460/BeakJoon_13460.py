import sys
N,M=map(int,input().split())
map=[]

for a in range(N):
    map.append(list(sys.stdin.readline().split()))

dx=[-1,0,1,0]
dy=[0,-1,0,1]

list_R=[]
list_B=[]
list_o=[]
list_c=[]
list=[]

for x in range(N):
    for y in range(M):
        if map[x][y]=="R":
            list_R.append((x,y))
        elif map[x][y]=="B":
            list_B.append((x,y))
        elif map[x][y]=="#":
            list_c.append((x,y))
        elif map[x][y]=="0":
            list_o.append((x,y))
        elif map[x][y]==".":
            list.append((x,y))

def direction_left(a,b):
    while a==0:
        if (a,b) in list_c:
            break
        elif (a,b) in list_o:
            break
