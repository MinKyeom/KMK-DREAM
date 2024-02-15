# 내 풀이
from collections import deque

# bfs
# 두 수레를 동시에 사방위로 이동시킨 후의 위치를 조합하여 그 위치를 동시에 다시 bfs를 실행하여 최솟값을 구하기

def solution(maze):
    m = len(maze)  # 세로
    n = len(maze[0])  # 가로
    v_r = [[False for _ in range(n)] for _ in range(m)]
    v_b = [[False for _ in range(n)] for _ in range(m)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    result = 0

    # 장애물 및 현 위치 및 도착지점 확인
    for i in range(m):
        for j in range(n):
            if maze[i][j] == 5:
                v_r[i][j] = True
                v_b[i][j] = True
            elif maze[i][j] == 1:
                r_s = [i, j]
                v_r[i][j] = True
            elif maze[i][j] == 2:
                b_s = [i, j]
                v_b[i][j] = True

    q = deque([[[r_s, [r_s]], [b_s, [b_s]]]])
    new = []  # q가 끝났을 때 더해줄 큐
    count = 0

    while q:
        r, b = q.popleft()
        # r[1]: 각각의 red가 지나온 길 b[1]: 각각의 blue가 지나온 길
        new_r = []
        new_b = []
        if maze[r[0][0]][r[0][1]] == 3:
            new_r = [r[0]]
        if maze[b[0][0]][b[0][1]] == 4:
            new_b = [b[0]]

        r_x, r_y = r[0][0], r[0][1]
        b_x, b_y = b[0][0], b[0][1]

        if maze[r_x][r_y] == 3 and maze[b_x][b_y] == 4:
            return result

        for x, y in zip(dx, dy):
            if 0 <= r_x + x < m and 0 <= r_y + y < n and maze[r_x][r_y] != 3 and maze[r_x + x][r_y + y] != 5 and not [
                                                                                                                         r_x + x,
                                                                                                                         r_y + y] in \
                                                                                                                     r[
                                                                                                                         1]:
                new_r.append([r_x + x, r_y + y])

            if 0 <= b_x + x < m and 0 <= b_y + y < n and maze[b_x][b_y] != 4 and maze[b_x + x][b_y + y] != 5 and not [
                                                                                                                         b_x + x,
                                                                                                                         b_y + y] in \
                                                                                                                     b[
                                                                                                                         1]:
                new_b.append([b_x + x, b_y + y])

        # 새로운 큐 제한 조건에 따른 분류
        for i in new_r:
            for j in new_b:
                road_r = []
                road_b = []
                if i != j:  # 같은 위치 불가
                    if j == r[0] and i == b[0]:  # 자리만 바꾼 경우
                        continue
                    else:
                        road_r += r[1]
                        road_r += [i]
                        road_b += b[1]
                        road_b += [j]
                        new.append([[i, road_r], [j, road_b]])

        if len(q) == 0:
            result += 1
            q = list(q)
            q += new
            q = deque(q)
            new = []

    return 0
# 내 풀이(개선 중)
from collections import deque
from itertools import combinations
# bfs
# 두 수레를 동시에 사방위로 이동시킨 후의 위치를 조합하여 그 위치를 동시에 다시 bfs를 실행하여 최솟값을 구하기

def solution(maze):
    m = len(maze)  # 세로
    n = len(maze[0])  # 가로
    v_r = [[False for _ in range(n)] for _ in range(m)]
    v_b = [[False for _ in range(n)] for _ in range(m)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    # 장애물 및 현 위치 및 도착지점 확인
    for i in range(m):
        for j in range(n):
            if maze[i][j] == 5:
                v_r[i][j] = True
                v_b[i][j] = True
            elif maze[i][j] == 1:
                r_s = [i, j]
                v_r[i][j] = True
            elif maze[i][j] == 2:
                b_s = [i, j]
                v_b[i][j] = True
            elif maze[i][j] == 3:
                v_r[i][j] = "red"
            elif maze[i][j] == 4:
                v_b[i][j] = "blue"

    q = deque([[r_s, b_s]])
    new = []  # q가 끝났을 때 더해줄 큐

    while q:
        r, b = q.popleft()
        r_x, r_y = r[0], r[1]
        b_x, b_y = b[0], b[1]
        new_r = []
        new_b = []

        for x, y in zip(dx, dy):
            if 0 <= r_x + x < m and 0 <= r_y + y < n and v_r[r_x + x][r_y + y] == False:
                new_r.append([r_x + x, r_y + y])
            if 0 <= b_x + x < m and 0 <= b_y + y < n and v_b[b_x + x][b_y + y] == False:
                new_b.append([b_x + x, b_y + y])

        # 새로운 큐 제한 조건에 따른 분류
        for i in new_r:
            for j in new_b:
                if i != j:
                    if j == r and i == b:
                        continue
                    else:
                        new.append([i, j])
        print(new)
        break
    answer = 0
    return answer

# 내 풀이(개선 중)
from collections import deque
from itertools import combinations


# bfs
# 두 수레를 동시에 사방위로 이동시킨 후의 위치를 조합하여 그 위치를 동시에 다시 bfs를 실행하여 최솟값을 구하기

def solution(maze):
    m = len(maze)  # 세로
    n = len(maze[0])  # 가로
    v_r = [[False for _ in range(n)] for _ in range(m)]
    v_b = [[False for _ in range(n)] for _ in range(m)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    # 장애물 및 현 위치 및 도착지점 확인
    for i in range(m):
        for j in range(n):
            if maze[i][j] == 5:
                v_r[i][j] = True
                v_b[i][j] = True
            elif maze[i][j] == 1:
                r_s = [i, j]
                v_r[i][j] = True
            elif maze[i][j] == 2:
                b_s = [i, j]
                v_b[i][j] = True
            elif maze[i][j] == 3:
                v_r[i][j] = "red"
            elif maze[i][j] == 4:
                v_b[i][j] = "blue"

    q = deque([[r_s, b_s]])
    new = []  # q가 끝났을 때 더해줄 큐

    while q:
        r, b = q.popleft()
        r_x, r_y = r[0], r[1]
        b_x, b_y = b[0], b[1]
        new_r = []
        new_b = []

        for x, y in zip(dx, dy):
            if 0 <= r_x + x < m and 0 <= r_y + y < n and v_r[r_x + x][r_y + y] == False:
                new_r.append([r_x + x, r_y + y])
            if 0 <= b_x + x < m and 0 <= b_y + y < n and v_b[b_x + x][b_y + y] == False:
                new_b.append([b_x + x, b_y + y])

        # 새로운 큐 제한 조건에 따른 분류
        for i in new_r:
            for j in new_b:
                if i != j:
                    if j == r and i == b:
                        continue
                    else:
                        new.append([i, j])
        print(new)
        break
    answer = 0
    return answer

# 내 풀이 (개선 중)
from collections import deque
from itertools import combinations


# bfs
# 두 수레를 동시에 사방위로 이동시킨 후의 위치를 조합하여 그 위치를 동시에 다시 bfs를 실행하여 최솟값을 구하기

def solution(maze):
    m = len(maze)  # 세로
    n = len(maze[0])  # 가로
    v_r = [[False for _ in range(n)] for _ in range(m)]
    v_b = [[False for _ in range(n)] for _ in range(m)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    result = 0

    # 장애물 및 현 위치 및 도착지점 확인
    for i in range(m):
        for j in range(n):
            if maze[i][j] == 5:
                v_r[i][j] = True
                v_b[i][j] = True
            elif maze[i][j] == 1:
                r_s = [i, j]
                v_r[i][j] = True
            elif maze[i][j] == 2:
                b_s = [i, j]
                v_b[i][j] = True

    q = deque([[[r_s, [r_s]], [b_s, [b_s]]]])
    new = []  # q가 끝났을 때 더해줄 큐
    flag_r = False  # 빨간 수레 도착 여부
    flag_b = False  # 파란 수레 도착 여부

    while q:
        r, b = q.popleft()
        # r[1]: 각각의 red가 지나온 길 b[1]: 각각의 blue가 지나온 길

        if maze[r[0][0]][r[0][1]] == 3:
            flag_r = True
            new_r = [r[0]]
        if maze[b[0][0]][b[0][1]] == 4:
            flag_b = True
            new_b = [b[0]]

        if flag_r == False:
            r_x, r_y = r[0][0], r[0][1]
            new_r = []
        if flag_b == False:
            b_x, b_y = b[0][0], b[0][1]
            new_b = []

        for x, y in zip(dx, dy):
            if 0 <= r_x + x < m and 0 <= r_y + y < n and flag_r == False and maze[r_x + x][r_y + y] != 5 and not [
                                                                                                                     r_x + x,
                                                                                                                     r_y + y] in \
                                                                                                                 r[1]:
                new_r.append([r_x + x, r_y + y])
            if 0 <= b_x + x < m and 0 <= b_y + y < n and flag_b == False and maze[b_x + x][b_y + y] != 5 and not [
                                                                                                                     b_x + x,
                                                                                                                     b_y + y] in \
                                                                                                                 b[1]:
                new_b.append([b_x + x, b_y + y])

        # 새로운 큐 제한 조건에 따른 분류
        if len(new_r) > 0 and len(new_b) > 0:
            for i in new_r:
                for j in new_b:
                    road_r = []
                    road_b = []
                    if i != j:  # 같은 위치 불가
                        if j == r and i == b:  # 자리만 바꾼 경우
                            continue
                        else:
                            road_r += r[1]
                            road_r += [i]
                            road_b += b[1]
                            road_b += [j]
                            new.append([[i, road_r], [j, road_b]])

        if len(q) == 0:
            if flag_r == True and flag_b == True:
                break

            else:
                result += 1
                q = list(q)
                q += new
                q = deque(q)
                new = []

        # q=deque([[[r_s,[r_s]],[b_s,[b_s]]]])

    return result if flag_r == True and flag_b == True else 0


# 내 풀이 (개선 중)
from collections import deque
from itertools import combinations


# bfs
# 두 수레를 동시에 사방위로 이동시킨 후의 위치를 조합하여 그 위치를 동시에 다시 bfs를 실행하여 최솟값을 구하기

def solution(maze):
    m = len(maze)  # 세로
    n = len(maze[0])  # 가로
    v_r = [[False for _ in range(n)] for _ in range(m)]
    v_b = [[False for _ in range(n)] for _ in range(m)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    result = 0

    # 장애물 및 현 위치 및 도착지점 확인
    for i in range(m):
        for j in range(n):
            if maze[i][j] == 5:
                v_r[i][j] = True
                v_b[i][j] = True
            elif maze[i][j] == 1:
                r_s = [i, j]
                v_r[i][j] = True
            elif maze[i][j] == 2:
                b_s = [i, j]
                v_b[i][j] = True

    q = deque([[[r_s, [r_s]], [b_s, [b_s]]]])
    new = []  # q가 끝났을 때 더해줄 큐
    flag_r = False  # 빨간 수레 도착 여부
    flag_b = False  # 파란 수레 도착 여부

    while q:
        r, b = q.popleft()
        # r[1]: 각각의 red가 지나온 길 b[1]: 각각의 blue가 지나온 길

        if maze[r[0][0]][r[0][1]] == 3:
            flag_r = True
            new_r = [r[0]]
        if maze[b[0][0]][b[0][1]] == 4:
            flag_b = True
            new_b = [b[0]]

        if flag_r == False:
            r_x, r_y = r[0][0], r[0][1]
            new_r = []
        if flag_b == False:
            b_x, b_y = b[0][0], b[0][1]
            new_b = []

        for x, y in zip(dx, dy):
            if 0 <= r_x + x < m and 0 <= r_y + y < n and flag_r == False and maze[r_x + x][r_y + y] != 5 and not [
                                                                                                                     r_x + x,
                                                                                                                     r_y + y] in \
                                                                                                                 r[1]:
                new_r.append([r_x + x, r_y + y])
            if 0 <= b_x + x < m and 0 <= b_y + y < n and flag_b == False and maze[b_x + x][b_y + y] != 5 and not [
                                                                                                                     b_x + x,
                                                                                                                     b_y + y] in \
                                                                                                                 b[1]:
                new_b.append([b_x + x, b_y + y])

        # 새로운 큐 제한 조건에 따른 분류
        if len(new_r) > 0 and len(new_b) > 0:
            for i in new_r:
                for j in new_b:
                    road_r = []
                    road_b = []
                    if i != j:  # 같은 위치 불가
                        if j == r and i == b:  # 자리만 바꾼 경우
                            continue
                        else:
                            road_r += r[1]
                            road_r += [i]
                            road_b += b[1]
                            road_b += [j]
                            new.append([[i, road_r], [j, road_b]])

        if len(q) == 0:
            if flag_r == True and flag_b == True:
                break

            else:
                result += 1
                q = list(q)
                q += new
                q = deque(q)
                new = []

        # q=deque([[[r_s,[r_s]],[b_s,[b_s]]]])

    return result if flag_r == True and flag_b == True else 0