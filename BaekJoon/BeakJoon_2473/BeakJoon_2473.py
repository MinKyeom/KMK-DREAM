from itertools import combinations

N=int(input())

num=list(map(int,input().split()))

sum=[]
for x,y,z in combinations(num,3):
    b=x+y+z
    c=abs(b)
    sum.append((x,y,z,c))
    if len(sum)>1:
        if sum[0][3]>=sum[1][3]:
            del sum[0]
        elif sum[0][3]<sum[1][3]:
            del sum[1]
result_sub=[sum[0][0],sum[0][1],sum[0][2]]

result=sorted(result_sub)

print(result)

#답은 나오나 시간에러
