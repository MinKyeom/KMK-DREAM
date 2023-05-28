#예제 3_1
n=int(input())

coin=[500,100,50,10]

count=0

while True:
    if n>=500:
        n-=500
        count+=1
        continue
    elif 100<=n<500:
        n-=100
        count+=1
        continue
    elif 50<=n<100:
        n-=50
        count+=1
        continue
    elif 10<=n<50:
        n-=10
        count+=1
        continue
    elif n==0:
        break

print(count)

