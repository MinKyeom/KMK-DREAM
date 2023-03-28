n,k=map(int,input().split())
num=list(input())

count=k
stack=[]

for i in range(n):
    while stack and stack[-1]<num[i] and count>0:
        stack.pop()
        count-=1
    stack.append(num[i])
print("".join(stack[:n-k]))

