R,C = map(int,input().split())

map=[] #초기 보드의 모양

for i in range(R):
    map.append(list(map(int,input().split())))

#내가 떠오른 idea: 이동하고 재귀함수로 이동하는거 반복해서 움직인 숫자의 max 또는 len

dx=[-1,0,1,0]
dy=[0,-1,0,1]

horse=[]
horse_arrive_list=[]

horse[0]=map[0][0]

def horse_move(x,y):
    horse[x][y]=map[x][y]
    for a,b in zip(dx,dy):
        if 0<=x+a<=R-1 and 0<=y+b<=C-1:
            c=map[x+a][y+b]
            if c not in horse:
                horse_arrive_list.append(c)



