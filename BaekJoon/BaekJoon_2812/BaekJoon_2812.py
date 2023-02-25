"""
import heapq
n=int(input())
k=int(input())
num=int(input())
count=0
list=[]
"""


"""
# 내가 푼 풀이1

for x in range(n):
    a=(num%10)
    list.append(a)
    num=int(num/10) #여기까지가 리스트에 숫자분리!
list.reverse()
print(list)

for y in range(k-2):
    heapq.heapify(list)
    del list[0]


print(list)"""

#위의 풀이 의논해보기

"""
내가 푼 풀이2
for x in range(n):
    if x==0:
        a=(num%10)
        list.append(a)
        num=int(num/10) #여기까지가 리스트에 숫자분리!
    if x>0:
        a=(num%10)
print(list)

for y in range(k-2):
    heapq.heapify(list)
    del list[0]


print(list)"""


"""
정답 예시 풀이

N, K = map(int, input().split())
num = list(input())
k, stack = K, []

for i in range(N):
    while k > 0 and stack and stack[-1] < num[i]: #의미가 잘 이해가 안됨
        stack.pop()
        k -= 1
    stack.append(num[i])

print(''.join(stack[:N-K]))
"""

#join 써보기

#이해 안된 코딩 구문 확인
"""n,k =map(int,input().split())

print(n,k)"""

"""num=list(input())

print(num)"""
num=[3,1,5]
stack=[]
print(stack[-1])
for i in range(3):
    while stack and stack[-1]<num[i]:
        stack.pop()
        print(stack)
        print()
        stack.append(num[i])
        print(stack)













