a=list(map(int,input().split()))
c=0
if a[0]==a[1]==a[2]:
    result=10000+a[0]*1000
    print(result)

elif a[0]==a[1] and not a[0]==a[2]:
    result=1000+a[0]*100
    print(result)

elif a[1]==a[2] and not a[0]==a[1]:
    result=1000+a[1]*100
    print(result)

elif a[0]==a[2] and not a[0]==a[1]:
    result=1000+a[0]*100
    print(result)

elif not a[0]==a[1] and not a[0]==a[2] and not a[1]==a[2]:
    result=max(a)*100
    print(result)