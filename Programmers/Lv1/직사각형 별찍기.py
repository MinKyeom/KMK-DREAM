# 내 풀이
a, b = map(int, input().strip().split(' '))
k=["*"*a for x in range(b)]
for y in k:
    print(y)


# 다른 사람 풀이
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)

