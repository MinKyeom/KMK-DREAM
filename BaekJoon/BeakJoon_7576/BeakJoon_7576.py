# M:상자 가로 칸 N:상자 세로 칸
M,N=map(int,input().split())

# 현재 담겨있는 토마토 상자의 배열
box=[]
for a in range(N):
    box.append(list(map(int,input().split()))) #박스 배열 입력

# 1: 익은 토마토, 0: 안익은 토마토, -1: 빈 상자

day=0 # 날짜 카운트

ripen_T=[] #익은 토마토를 담을 리스트
ripen_T_new=[]

# 상,하,좌,우를 위하여
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 과일을 익게만드는 과정 및 익은 토마토 위치 찾기
def ripe_spread(x,y):
    if box[x][y]==1:
        for a,b in zip(dx,dy): #4방위를 비교
            if 0<=x+a<=N-1 and 0<=y+b<=M-1:
                new_x=x+a
                new_y=y+b
                if box[new_x][new_y]==0:
                    box[new_x][new_y]=1
                    ripen_T.append((new_x,new_y))


# 익은 과일의 개수를 찾는 함수
# def find_ripe():
#     find_1=0
#     for x in range(M):
#         for y in range(N):
#             if box[x][y]==1:
#                 find_1+=1

# 빈상자 찾기



non_box=[] #빈상자

#첫 날에 익은 토마토 찾기 및 처음 빈상자 위치 찾기
for c in range(N):
    for d in range(M):
        if box[c][d]==1:
            ripen_T.append((c,d)) #첫 날에 익은 토마토 찾기
        elif box[c][d]==-1:
            non_box.append((c,d)) # 빈 상자 찾기


# for e in range(len(ripen_T)):
#     ripe_spread(ripen_T[e][0],ripen_T[e][1])
# print("함수 실행 후",ripen_T)




num_t=[] #익은 토마토
t=len(num_t)

# non_box_conunt= len(non_box)

#full_ripen=(M*N)-non_box_conunt #상자안의 과일이 모두 익었을 경우 1의 합

entire_element= int(M*N) # 전체 원소의 개수

num=0
# print("처음 시작 전",ripen_T)
# ripe_spread(3,5)
# print("임의로 넣은 후 ",ripen_T)
while num <= entire_element: #전체원소만큼 일단
    if t<len(ripen_T):
        t = len(ripen_T)  # t값 갱신
        for e in range(len(ripen_T)):
            ripe_spread(ripen_T[e][0],ripen_T[e][1])
        #print(ripen_T)
        day+=1

        # if num_t<len(ripen_T): #익히는걸 실행 전후로 개수 비교
        #     num_t=len(ripen_T) #익은 토마토의 개수 갱신
        #     day+=1
    num +=1

day= day-1

# #----여기까지가--- 익히기
# print(day)
if len(non_box)+len(ripen_T)==M*N:
    print(day)

else:
    print(-1)

# for g in range(N):
#     for h in range(M):
#         if box[g][h] ==0:
#             non_box.append((g,h))
# if len(non_box)==0:
#     print(day)
# else:
#     print(-1)
