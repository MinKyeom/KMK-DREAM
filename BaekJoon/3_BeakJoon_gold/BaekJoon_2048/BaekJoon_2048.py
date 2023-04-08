#4*4 크기의 보드게임
#한 번에 상하좌우 한 번 이동
#같은 값을 갖는 블록 충돌시 합쳐진다
#한 번 합쳐진 블록은 다시 합쳐지지 못한다
N=int(input())
num=[]

for a in range(N):
    num=list(map(int,input().split()))

# 상,하,좌,우 
