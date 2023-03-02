# M:상자 가로 칸 N:상자 세로 칸
M,N=map(int,input().split())

# 현재 담겨있는 토마토 상자의 배열
box=[]

for a in range(N):
    box.append(list(map(int,input().split()))) #박스 배열 입력

# 1: 익은 토마토, 0: 안익은 토마토, -1: 빈 상자

day=0 # 날짜 카운트

# 상,하,좌,우를 위하여
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 과일을 익게만드는 과정
def ripe_spread(x,y):
    if box[x][y]==1:
        for a,b in zip(dx,dy):
            if x+a<=N-1 and x+a >=0 and y+b<M-1 and y+b>=0 :
                new_x=x+a
                new_y=y+b
                if box[new_x][new_y]==0:
                    box[new_x][new_y]=1
def find_ripe():
    find_1=0
    for x in range(M):
        for y in range(N):
            if box[x][y]==1:
                find_1+=1


day1_ripen_T=[] #첫 날에 익은 토마토 찾기 위한 리스트

non_box=[] # 빈 상자

for c in range(N):
    for d in range(M):
        if box[c][d]==1:
            day1_ripen_T.append((c,d)) #첫 날에 익은 토마토 찾기
        elif box[c][d]==-1:
            non_box.append((c,d)) # 빈 상자 찾기
non_box_conunt= len(non_box)

full_ripen=(M*N)-non_box_conunt #상자안의 과일이 모두 익었을 경우 1의 합

while 0 in box:
    for e,f in day1_ripen_T:
        ripe_spread(e,f)
    day+=1


print(day)