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
"""
import sys
R,C =map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]
dx=[-1,0,1,0]
dy=[0,-1,0,1]
answer =1

def BFS(x,y):
    global answer
    q =set([(x,y,board[x][y])])  #set은 집합과 비슷한 개념!
    print("처음 시작할 때 q",q)
    print("while문 시작")
    print()
    while q: #q가 참일때까지 반복
        x,y,ans =q.pop() # 처음 넣은 q값을 제거하여 무한루프를 제거!

        # 예시
        # a=set()
        # print(bool(a)) #false 출력
        #
        # a=set([1])
        # print(bool(a)) #true 출력
        # 공집할일때는 거짓으로 출력
        print()
        print(q)
        print("이거 넣어서 while 시작할 때 구분")
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            print(nx,ny) #들어간 방향 체크
            if((0<=nx<R) and (0<=ny<C)) and (board[nx][ny] not in ans):
                q.add((nx,ny,ans + board[nx][ny])) #set의 add는 원소 추가!
                answer= max(answer,len(ans)+1)
                print(q)
                print(answer)
BFS(0,0)
print(answer)
"""

R,C =map(int,input().split())
horse_map=[]
for a in range(R):
    horse_map.append(list(map(int,input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def BFS(x, y):
    global answer
    q = set([(x, y, horse_map[x][y])])
    while q:
        x, y, ans = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ((0 <= nx < R) and (0 <= ny < C)) and (horse_map[nx][ny] not in ans):
                q.add((nx,ny,ans + horse_map[nx][ny]))
                answer = max(answer, len(ans)+1)

BFS(0, 0)
print(answer)