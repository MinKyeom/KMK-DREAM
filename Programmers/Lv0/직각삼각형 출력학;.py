# 내 풀이
n = int(input())
for a in range(1,n+1):
    print("*"*a)

# 다른 사람 풀이
print('\n'.join('*' * (i + 1) for i in range(int(input()))))