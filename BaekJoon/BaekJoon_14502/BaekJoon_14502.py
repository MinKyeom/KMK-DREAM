from itertools import combinations #1로 만들걸 0중에 뽑기 위하여

#N :가로 크기 ,M:세로 크기

N,M= map(int,input().split()) #N ,M N행*M열

spot=[list(map(int,input().split())) for a in range(N)] #현재 연구소의 모양 입력

#0: 빈 칸, 1: 벽 ,2: 바이러스

#벽 최대 3개 세우는거 가능!
no_virus=[]
count =[]
no_virus_new=[]

for b in range(N):
    for c in range(M): #모든 요소를 한 번씩 확인
        if spot[b][c]==0:
            no_virus.append([b,c])
            #if spot[b-1][c]==2 or spot[b+1][c]==2 or spot[b][c+1]==2 or spot[b][c-1]==2: # 사방위중 한군데라도 바이러스가 있을떄
            #    spot[b][c]=2
#print("for 전",no_virus)
#print(list(combinations(no_virus,3))) #1로 만들 0인곳 선정!

for e in list(combinations(no_virus,3)):
    for f in no_virus:
        for g in range(3):
            spot[no_virus[g][0]][no_virus[g][1]]=1  # 수 많은 0인 빈 칸들중 세 개를 뽑아 벽으로 만듬
            for h in range(N):
                for i in range(M):
                    if spot[h][i]==0:
                        if h - 1 >= 0 and spot[h - 1][c] == 2:
                            spot[h][i] = 2
                        elif i - 1 >= 0 and spot[h][i - 1] == 2:
                            spot[b][c] = 2
                        elif i + 1 <= M - 1 and spot[h][i + 1] == 2:
                            spot[b][c] = 2
                        elif h + 1 <= N - 1 and spot[h + 1][i] == 2:
                            spot[b][c] = 2



                        no_virus_new.append([h,i])
            count.append(len(no_virus_new))      #새롭게 생성된 빈 칸의 갯수


count.sort()  #오름차순으로 정렬

print(count[-1])


#for e in list(combinations(no_virus,3)):
#    print("for 후",no_virus)

"""
for d in combinations(no_virus, 3):
    no_virus=1
        for e in range:
        """

""" if b-1>=0 and spot[b-1][c]==2 :
                spot[b][c] = 2
            elif c-1>=0 and spot[b][c-1]==2:
                spot[b][c] = 2
            elif c+1<=M-1 and spot[b][c+1]==2:
                spot[b][c] =2
            elif b+1<=N-1 and spot[b+1][c]==2 :
                spot[b][c] = 2
                 """
#여기까지의 spot은 벽을 전혀 새로 세우지 않았을떄의 모습이다.

"""
print(spot)
for d in range(N):
    for e in range(M):
        if spot[d][e]==0:
            count +=1
            # no_virus.append([d,e])
print(count)
# print(len(no_virus))
"""