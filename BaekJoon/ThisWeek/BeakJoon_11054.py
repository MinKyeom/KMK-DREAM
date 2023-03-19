x = int(input())
#o(1)

case = list(map(int, input().split()))
#o(1)

increase = [1 for i in range(x)]
#o(x-1)

for i in range(x): #x-1      #(x-1)*(i-1)
    for j in range(i): #j-1
        if case[i] > case[j]:
            increase[i] = max(increase[i], increase[j]+1)
# o(n^2):n*n (x-1)(i-1)

decrease2 = [1 for i in range(x)]
for i in range(x-1, -1, -1):
    for j in range(x-1, i, -1):
        if case[i] > case[j]:
            decrease2[i] = max(decrease2[i], decrease2[j]+1)
#o(n^2)*o(log())

result = [0 for i in range(x)]
for i in range(x):
    result[i] = increase[i] + decrease2[i] -1

#o(n)

print(max(result))
