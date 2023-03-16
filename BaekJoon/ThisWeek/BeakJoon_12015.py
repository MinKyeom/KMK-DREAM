import sys
n=int(input())
a=list(map(int,sys.stdin.readline().split()))
num=[]

b=0
for x in range(len(a)-1):
    b=a[x]
    count=0
    for y in range(x+1,len(a)):
        if b<a[y]:
            count+=1
            b=a[y]

        num.append(count)

print(max(num)+1)



