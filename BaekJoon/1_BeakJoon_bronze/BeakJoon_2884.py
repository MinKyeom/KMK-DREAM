n,m=map(int,input().split())

if m>=45:
    print(n,m-45)

elif m<45:
    if n==0:
        n=24-1
        m=60-abs(m-45)
        print(n,m)
    else:
        n=n-1
        m=60-abs(m-45)
        print(n,m)