x=int(input())
n=int(input())
r=0
for a in range(n):
    c,d=map(int,input().split())
    r+=(c*d)
print(r)
print(type(r))

if x==r:
    print("Yes")

elif not x==r:
    print("No")

