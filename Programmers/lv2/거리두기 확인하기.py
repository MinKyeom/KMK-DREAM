# 내 풀이(갱신중)
def solution(places):
    result = []

    # bfs
    from collections import deque
    # dx=[1,-1,0,0]
    # dy=[0,0,1,-1]

    for a in places:
        # visited=[[False]*5 for k in range(5)]
        q = []

        dx = [-2, -1, 1, 2, 0, 0, 0, 0, -1, -1, 1, 1]
        dy = [0, 0, 0, 0, -2, -1, 1, 2, 1, -1, 1, -1]

        for c in range(5):
            for d in range(5):
                if a[c][d] == "P":
                    q.append([c, d])
        q = deque(q)

        while q:
            e, f = q.popleft()

            flag = False

            for x, y in zip(dx, dy):
                if 0 <= e + x < 5 and 0 <= f + y < 5:
                    if a[e + x][f + y] == "P":
                        # case1 ## 중요 케이스
                        if abs(x) == 2 or abs(y) == 2:
                            if abs(x) == 2:
                                if x > 0 and a[e + x - 1][f + y] == "X":
                                    continue
                                elif x < 0 and a[e + x + 1][f + y] == "X":
                                    continue
                                else:
                                    print(1)
                                    flag = True
                                    break

                            elif abs(y) == 2:
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

            if flag == True:
                break

        if flag == False:
            result.append(1)
        else:
            result.append(0)

    return result
