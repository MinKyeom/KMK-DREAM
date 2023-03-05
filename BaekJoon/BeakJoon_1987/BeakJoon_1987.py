# R,C = map(int,input().split())
#
# map=[] #초기 보드의 모양
#
# for i in range(R):
#     map.append(list(map(int,input().split())))
#
# #내가 떠오른 idea: 이동하고 재귀함수로 이동하는거 반복해서 움직인 숫자의 max 또는 len
#
# dx=[-1,0,1,0]
# dy=[0,-1,0,1]
#
# horse=[]
# horse_arrive_list=[]
#
# horse[0]=map[0][0]
#
# def horse_move(x,y):
#     horse[x][y]=map[x][y]
#     for a,b in zip(dx,dy):
#         if 0<=x+a<=R-1 and 0<=y+b<=C-1:
#             c=map[x+a][y+b]
#             if c not in horse:
#                 horse_arrive_list.append(c)

#연습 및 사고 과정 따라가기
import sys
R,C =map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]
dx=[-1,0,1,0]
dy=[0,-1,0,1]
answer =1

def BFS(x,y):
    global answer
    q =set([(x,y,board[x][y])])  #set은 집합과 비슷한 개념!
    while q:
        x,y,ans =q.pop()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            print(nx,ny)
            if((0<=nx<R) and (0<=ny<C)) and (board[nx][ny] not in ans):
                q.add((nx,ny,ans + board[nx][ny])) #set의 add는 원소 추가!
                answer= max(answer,len(ans)+1)
                print(q)
                print(answer)
BFS(0,0)
print(answer)

