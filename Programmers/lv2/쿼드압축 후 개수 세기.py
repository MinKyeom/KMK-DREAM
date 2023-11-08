# 내 풀이
def solution(arr):
    from collections import deque
    k = len(arr)
    result = []
    q = deque([arr[0][0], arr[0][1]])
    count_0 = 0
    count_1 = 0
    visit = []

    flag = False

    while flag == False and k >= 2:
        new = [[0 for v in range(int(k / 2))] for w in range(int(k / 2))]
        count = 0
        c = 0
        d = 0
        for a in range(0, k, 2):
            if a != 0:
                c += 1
                d = 0
            for b in range(0, k, 2):
                if arr[a][b] == arr[a + 1][b] == arr[a + 1][b + 1] == arr[a][b + 1] == 1:
                    count += 1
                    new[c][d] = 1
                elif arr[a][b] == arr[a + 1][b] == arr[a + 1][b + 1] == arr[a][b + 1] == 0:
                    count += 1
                    new[c][d] = 0
                else:
                    new[c][d] = "x"
                    check = 0
                    if arr[a][b] == 1:
                        count_1 += 1
                    elif arr[a][b] == 0:
                        count_0 += 1
                    if arr[a][b + 1] == 1:
                        count_1 += 1
                    elif arr[a][b + 1] == 0:
                        count_0 += 1
                    if arr[a + 1][b + 1] == 1:
                        count_1 += 1
                    elif arr[a + 1][b + 1] == 0:
                        count_0 += 1
                    if arr[a + 1][b] == 1:
                        count_1 += 1
                    elif arr[a + 1][b] == 0:
                        count_0 += 1

                d += 1
                # print(new,count_0,count_1)

        if count == 0:
            flag = True

        else:
            if k >= 2:
                k = int(k / 2)
                arr = new
            else:
                arr = new
                break

    # 마지막 배열 체크
    for v in range(len(new)):
        for w in range(len(new)):
            if new[v][w] == 0:
                count_0 += 1
            elif new[v][w] == 1:
                count_1 += 1

    return [count_0, count_1]


# 다른 사람 풀이
def solution(arr):
    answer = [0, 0]

    def check(size, x, y):
        if size == 1:
            answer[arr[y][x]] += 1
            return
        else:
            first = arr[y][x]

            for dy in range(size):
                for dx in range(size):
                    if first != arr[y + dy][x + dx]:
                        check(size // 2, x, y)
                        check(size // 2, x + size // 2, y)
                        check(size // 2, x, y + size // 2)
                        check(size // 2, x + size // 2, y + size // 2)
                        return
            answer[first] += 1
    check(len(arr),0,0)


    return answer