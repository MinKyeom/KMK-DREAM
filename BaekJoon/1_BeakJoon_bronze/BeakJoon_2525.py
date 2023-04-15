a,b= map(int,input().split())
c=int(input())

if c+b<60:
    print(a,b+c)

elif c+b>=60:
    d=(c+b)%60
    h=int((c+b)/60)

    if a+h>23:
        new_a=(a+h)-24
        print(new_a,d)
    elif a+h<=23:
        print(a+h,d)