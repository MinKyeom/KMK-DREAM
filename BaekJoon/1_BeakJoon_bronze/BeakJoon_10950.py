t=int(input())
num=[]
for x in range(t):
    a,b= map(int,input().split())
    num.append((a,b))

for y in range(len(num)):
    print(num[y][0]+num[y][1])




