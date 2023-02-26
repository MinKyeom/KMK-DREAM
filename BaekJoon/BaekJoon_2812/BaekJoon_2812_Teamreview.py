"""stack=[]

while k > 0 and stack and stack[-1] < num[i]:

    break

"""

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

stack=[] # 이게 비어있는게 아니다

print(bool(stack))

stack=[1]

print(bool(stack))

#pycharm-ipython



# while stack and stack[-1]

