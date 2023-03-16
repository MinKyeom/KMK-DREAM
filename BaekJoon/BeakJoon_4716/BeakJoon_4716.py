# 핵심 think: 거리가 적은걸 많이+ 두 a,b 거리가 큰 거를 우선으로

# N,A,B=int(input().split())
# ballmap=[]
#
# for a in range(N+1):
#     ballmap.append(map(int,input().split()))
# list_ball=[]
# distance_a=[]
# distance_b=[]
#
# for b in range(N):
#     for c in range(3):
#         if c==0:
#             list_ball.append(ballmap[b][c])
#
#         elif c==1:
#             distance_a.append(ballmap[b][c])
#
#         elif c==2:
#             distance_b.append(ballmap[b][c])
#
# #sol
#
# while True:
#     n,a,b=map(int,input().split())
#     if n == a== b==0:
#         break
#
#     arr =sorted([[map(int,input().split())]for _ in range(n)], key=lambda x:-abs(x[1]-x[2]))
#
#     ans=0
#     for k,x,y in arr:
