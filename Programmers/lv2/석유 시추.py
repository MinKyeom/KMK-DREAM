# 내 풀이
# bfs를 한 번 돌린 후 파이프 번호에 내장량을 더해준다!
from collections import deque
def solution(land):
    n = len(land)  # 깊이(세로)
    m = len(land[0])  # 폭(가로)
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    p = [0 for _ in range(m)]  # 파이프 번호

    v = [[False for _ in range(m)] for _ in range(n)]  # 방문

    q = deque([])

    check_p = []  # 파이프 뭉치 체크

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                q.append([i, j])

    # 석유가 들어있는 점 모두 q 시작
    while q:
        count = 0
        new = deque([])
        x, y = q.popleft()
        if v[x][y] == False:
            v[x][y] = True
            check_p.append(y)
            new.append([x, y])

        while new:
            count += 1
            x, y = new.popleft()

            for nx, ny in zip(dx, dy):
                if 0 <= x + nx < len(land) and 0 <= y + ny < len(land[0]) and land[x + nx][y + ny] == 1 and v[x + nx][
                    y + ny] == False:
                    new.append([x + nx, y + ny])
                    v[x + nx][y + ny] = True
                    check_p.append(y + ny)

        for k in list(set(check_p)):
            p[k] += count

        # 초기화
        count = 0
        new = deque([])
        check_p = []

    return max(p)
# 내 풀이 (개선 중)
# bfs > 효율성 0
# bfs를 한 번에 하고 결과값 나오게 연결된 관은 모두 값으로 만들어 풀기 idea 생각해보기
from collections import deque

# sol1
def solution(land):
    n = len(land)  # 깊이
    m = len(land[0])

    result = 0

    check = deque([k for k in range(len(land[0]))])
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    while check:
        p = check.popleft()  # 시추관 번호
        v = []
        count = 0
        q = deque([])

        for i in range(len(land)):
            if land[i][p] == 1:
                # if not [i,p] in v:
                #     q.append([i,p])
                q.append([i, p])
                v.append([i, p])
        while q:
            x, y = q.popleft()
            count += 1

            for nx, ny in zip(dx, dy):
                if 0 <= x + nx < len(land) and 0 <= y + ny < len(land[0]) and land[x + nx][y + ny] == 1 and not [x + nx,
                                                                                                                 y + ny] in v:
                    q.append([x + nx, y + ny])
                    v.append([x + nx, y + ny])

        if count > result:
            result = count

    return result

#sol2
# 내 풀이 (개선 중)
# bfs를 한 번 돌린 후 파이프 번호에 내장량을 더해준다!
from collections import deque


def solution(land):
    n = len(land)  # 깊이(세로)
    m = len(land[0])  # 폭(가로)
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    p = [0 for _ in range(m)]  # 파이프 번호

    v = []  # 방문

    count = 0
    q = deque([])

    check_p = []  # 파이프 뭉치 체크

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not [i, j] in v:
                q.append([i, j])
                v.append([i, j])
                check_p.append(j)

                while q:
                    x, y = q.popleft()
                    count += 1
                    for nx, ny in zip(dx, dy):
                        if 0 <= x + nx < len(land) and 0 <= y + ny < len(land[0]) and land[x + nx][
                            y + ny] == 1 and not [x + nx, y + ny] in v:
                            q.append([x + nx, y + ny])
                            v.append([x + nx, y + ny])
                            check_p.append(y + ny)

                for k in list(set(check_p)):
                    p[k] += count

                # 초기화
                count = 0
                q = deque([])
                check_p = []

    return max(p)

# 다른 사람 풀이
from collections import deque


def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    result = [0 for i in range(m + 1)]
    visited = [[0 for i in range(m)] for j in range(n)]

    def bfs(a, b):
        count = 0
        visited[a][b] = 1
        q = deque()
        q.append((a, b))
        min_y, max_y = b, b
        while q:
            x, y = q.popleft()
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            count += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if visited[nx][ny] == 0 and land[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

        for i in range(min_y, max_y + 1):
            result[i] += count

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and land[i][j] == 1:
                bfs(i, j)
    answer = max(result)
    return answer

# 다른 사람 풀이
def solution(land):
    n, m = len(land), len(land[0])
    visited = [[True]*m for _ in range(n)]
    delta = [(1,0),(-1,0),(0,1),(0,-1)]
    oil_cnt = [0]*m
    for i in range(n):
        for j in range(m):
            if land[i][j] and visited[i][j]:
                visited[i][j] = False
                s = [(i,j)]
                col = set()
                oil = 0
                while s:
                    x, y = s.pop()
                    col.add(y)
                    oil += 1
                    for dx, dy in delta:
                        X, Y = x+dx, y+dy
                        if 0<=X<n and 0<=Y<m and land[X][Y] and visited[X][Y]:
                            visited[X][Y] = False
                            s.append((X,Y))
                for y in col:
                    oil_cnt[y] += oil
    return max(oil_cnt)

