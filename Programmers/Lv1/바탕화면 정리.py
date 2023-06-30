# 내 풀이
def solution(wallpaper):
    file_1 = []
    file_2 = []
    for x in range(len(wallpaper)):
        k = list(wallpaper[x])
        for y in range(len(wallpaper[0])):
            if k[y] == "#":
                file_1.append(x)
                file_2.append(y)
    a = max(file_1)
    b = min(file_1)
    c = max(file_2)
    d = min(file_2)
    print(a, b, c, d)

    return [b, d, a + 1, c + 1]
# 다른 사람 풀이
def solution(wall):
    a, b = [], []
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]
