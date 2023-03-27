n,k=map(int,input().split())
num=list(input())

count=0
stack=[]

for i in range(n):
    while stack and stack[-1]<num[i]:
        stack.pop()
        count+=1
        print(count)
        if count==k:
            break
    stack.append(num[i])
print("".join(stack))

