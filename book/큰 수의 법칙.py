n,m,k= map(int,input().split())
num=list(map(int,input().split()))
num.sort()

num_2=list(reversed(num))

count=0
result=0
print(num_2)

for x in range(m):
    if count<k:
        result+=num_2[0]
        count+=1
    else:
        count=0
        result+=num_2[1]
print(result)