#빈 칸, 집 , 치킨집, 집

#치킨거리:집으로부터의 거리

#도시의 치킨거리: 모든 집의 치킨 거리의 합

#수익을 가장 많이 내면서 각 집에서 거리가 최솟값인 치킨집의 갯수: M

from itertools import combinations



N,M =map(int,input().split())

#I:도시정보
I =[]
house=[]
chick=[]

row=N  # 가로 즉 행
colume=N #세로 즉 열
I=[list(map(int,input().split())) for a in range(N)]

for b in range(N):
    for c in range(N):
        if I[b][c]==1: house.append([b,c])
        elif I[b][c]==2: chick.append([b,c])
result=0

for e in combinations(chick,M):
    c_distance= 0
    for g in house:
        h_distance=0
        for h in e:
            h_distance=min(h_distance,abs(g[0]-h[0])+abs(g[1])-h[1])
        c_distance += h_distance
    result=min(result,c_distance)

print(result)


# idea의 출발: 컴퓨터에서의 행렬은 가로부터 생성이라 렬부터 곱해줘야한다!!


#abs 함수를 활용하여 절댓값!
#a=-5 일때 abs(a)는 절댓값을 씌우는 의미!




