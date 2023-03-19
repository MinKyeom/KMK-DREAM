n, k = map(int, input().split())
#o(1)
thing = [[0,0]]
#o(1)
d = [[0]*(k+1) for _ in range(n+1)]
#o(1)
for i in range(n):
    thing.append(list(map(int, input().split())))
#o(n)
for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]
#o(n^2)
        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])

# 참고) 알고리즘 리뷰 https://claude-u.tistory.com/208