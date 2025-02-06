"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/81302?language=python3
"""
# 풀이 과정
def solution(places):
    result = []

    # bfs
    from collections import deque
    flag = False

    for a in places:
        q = []
        dx = [-2, -1, 1, 2, 0, 0, 0, 0, -1, -1, 1, 1]
        dy = [0, 0, 0, 0, -2, -1, 1, 2, 1, -1, 1, -1]

        for c in range(5):
            for d in range(5):
                if a[c][d] == "P":
                    q.append([c, d])
        q = deque(q)

        if len(q) == 0:
            result.append(1)
            continue

        while q:
            e, f = q.popleft()

            flag = False

            for x, y in zip(dx, dy):
                if 0 <= e + x < 5 and 0 <= f + y < 5:
                    if a[e + x][f + y] == "P":
                        # case1 ## 중요 케이스

                        if abs(x) == 2 or abs(y) == 2:

                            if abs(x) == 2 and abs(y) == 0:
                                if x > 0 and a[e + x - 1][f + y] == "X":
                                    continue
                                elif x < 0 and a[e + x + 1][f + y] == "X":
                                    continue
                                else:
                                    print(1)
                                    flag = True
                                    break

                            elif abs(y) == 2 and abs(x) == 0:
                                if y > 0 and a[e + x][f + y - 1] == "X":
                                    continue
                                elif y < 0 and a[e + x][f + y + 1] == "X":
                                    continue
                                else:
                                    print(2)
                                    flag = True
                                    break

                                    # case2 ## 중요 케이스

                        elif abs(x) == 1 and abs(y) == 1:
                            if x == 1 and y == 1:
                                if a[e + x][f] == "X" and a[e][f + y] == "X":
                                    continue
                                else:
                                    flag = True
                                    print(3)
                                    break

                            elif x == 1 and y == -1:
                                if a[e + x][f] == "X" and a[e][f + y] == "X":
                                    continue
                                else:
                                    flag = True
                                    print(4)
                                    break

                            elif x == -1 and y == 1:
                                if a[e + x][f] == "X" and a[e][f + y] == "X":
                                    continue
                                else:
                                    flag = True
                                    print(5)
                                    break

                            elif x == -1 and y == -1:
                                if a[e + x][f] == "X" and a[e][f + y] == "X":
                                    continue
                                else:
                                    flag = True
                                    print(6)
                                    break

                                    # case3

                        elif abs(x) == 1 and abs(y) == 0:
                            flag = True
                            print(7)
                            break

                        # case4

                        elif abs(x) == 0 and abs(y) == 1:
                            flag = True
                            print(8)
                            break

            else:
                continue

            if flag == True:
                break

        if flag == False:
            result.append(1)
        else:
            result.append(0)

    return result


# 다른 사람 풀이
def check(place):
    for irow, row in enumerate(place):
        for icol, cell in enumerate(row):
            if cell != 'P':
                continue
            if irow != 4 and place[irow + 1][icol] == 'P':
                return 0
            if icol != 4 and place[irow][icol + 1] == 'P':
                return 0
            if irow < 3 and place[irow + 2][icol] == 'P' and place[irow + 1][icol] != 'X':
                return 0
            if icol < 3 and place[irow][icol + 2] == 'P' and place[irow][icol + 1] != 'X':
                return 0
            if irow != 4 and icol != 4 and place[irow + 1][icol + 1] == 'P' and (place[irow + 1][icol] != 'X' or place[irow][icol + 1] != 'X'):
                return 0
            if irow != 4 and icol != 0 and place[irow + 1][icol - 1] == 'P' and (place[irow + 1][icol] != 'X' or place[irow][icol - 1] != 'X'):
                return 0
    return 1

def solution(places):
    return [check(place) for place in places]


# 다른 사람 풀이
def solution(places):
    result = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def f(i, j, cnt):
        nonlocal good
        if cnt >2 : return
        if -1<i<5 and -1<j<5:
            if graph[i][j] == 'X':
                return

            if cnt != 0 and graph[i][j] == 'P':
                good = 0
                return

            graph[i][j] = 'X'

            for w in range(4):
                ni = i+dx[w]
                nj = j+dy[w]
                f(ni, nj, cnt+1)

    for case in places:
        graph = [list(r) for r in case]
        good = 1
        for i in range(5):
            for j in range(5):
                if graph[i][j]=='P':
                    f(i,j,0)

        result.append(good)
    return result