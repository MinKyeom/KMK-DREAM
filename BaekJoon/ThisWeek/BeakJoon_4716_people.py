#point 사고:거리가 최소화 가장 길이가 긴 곳이 풍선을 적게 가져가야한다.
while 1:
    n, a, b = map(int, input().split())
    if n == a == b == 0: break
    arr = sorted([[*map(int, input().split())]for _ in range(n)], key=lambda x: -abs(x[1]-x[2]))
    ans = 0
    for k, x, y in arr:
        if x <= y: val = min(k, a)
        else: val = k - min(k, b)
        ans += val * x + (k - val) * y
        a -= val
        b -= k - val
    print(ans)

#sol2

while True:
    n, a, b = map(int, input().split())
    if n == a == b == 0:
        break
    array = [list(map(int, input().split())) for _ in range(n)]
    array.sort(key=lambda x: abs(x[1] - x[2]), reverse=True)
    total_distance = 0
    equal_dis = []
    for ballon, distanceA, distanceB in array:
        if distanceA > distanceB:
            if b >= ballon:
                b -= ballon
                total_distance += distanceB * ballon
            else:
                ballon -= b
                total_distance += distanceB * b
                b = 0
                total_distance += distanceA * ballon
        elif distanceA < distanceB:
            if a >= ballon:
                a -= ballon
                total_distance += distanceA * ballon
            else:
                ballon -= a
                total_distance += distanceA * a
                a = 0
                total_distance += distanceB * ballon
        else:
            equal_dis.append([ballon, distanceA, distanceB])

    for i in range(len(equal_dis)):
        total_distance += equal_dis[i][0] * equal_dis[i][1]

    print(total_distance)