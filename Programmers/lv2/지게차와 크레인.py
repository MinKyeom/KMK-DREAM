"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/388353
"""

# 풀이과정
"""
겉면에서 출발하는 bfs실시 후 도착 가능한 알파벳 제거
두 번 반복된 경우 적용할 필요 없음 모두 그냥 빼버리는게 가능

해당 알파벳 찾은 후 빈공간으로 bfs 적용하는 방식이 좀 더 효율적일거라 생각된다.
"""
"""
겉면에서 출발하는 bfs실시 후 도착 가능한 알파벳 제거
두 번 반복된 경우 적용할 필요 없음 모두 그냥 빼버리는게 가능

해당 알파벳 찾은 후 빈공간으로 bfs 적용하는 방식이 좀 더 효율적일거라 생각된다.

모든 화물에 대해 이동 가능 조사 후 bfs에 나중에 반영 중간중간 반영x

몆 가지 케이스가 시간초과 발생

개선 방법 과정
>수정 방안 고민
> global 맵 생성 후 그 자리를 지나면 지게차로 가능하다 판정 여부 확인
> 없는 알파벳 존재 여부 추가 후 확인

정답 과정: visit한 여부를 이동 직후 바로 도착으로 확인해야 시간을 단축할 수 있다.
"""

from collections import deque, Counter

map = []


def bfs(s, i, j):
    global map
    m = len(s)
    n = len(s[0])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque([(i, j)])

    flag = False

    visit = [[False] * n for _ in range(m)]

    while q:
        x, y = q.popleft()
        visit[x][y] = True

        if map[x][y] == True:
            return True

        for nx, ny in zip(dx, dy):
            if nx + x >= m or nx + x < 0:
                flag = True
                break
            elif ny + y >= n or ny + y < 0:
                flag = True
                break
            else:
                if s[nx + x][ny + y] == "" and visit[nx + x][ny + y] == False:
                    q.append((nx + x, ny + y))
                    visit[nx + x][ny + y] = True

    # 지게차 맵 재갱신
    if flag == True:
        # map[i][j]==True
        for a in range(m):
            for b in range(n):
                if visit[a][b] == True:
                    map[a][b] == True

    return flag


def check_alpha(s, alpha):
    del_alpha = []

    global map

    map = [[False] * len(s[0]) for _ in range(len(s))]

    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == alpha:
                check = bfs(s, i, j)
                if check == True:
                    del_alpha.append((i, j))

    for x, y in del_alpha:
        s[x][y] = ""

    return s, len(del_alpha)


def all_alpha(s, alpha):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == alpha:
                s[i][j] = ""

    return s


def solution(storage, requests):
    s = []
    all_ = ""
    for stor in storage:
        s.append(list(stor))
        all_ += stor

    count_alpha = Counter(all_)

    for r in requests:
        if not r[0] in count_alpha:
            continue

        if count_alpha[r[0]] == 0:
            continue

        if len(r) == 2:
            alpha = r[0]
            count_alpha[alpha] = 0
            s = all_alpha(s, alpha)
        else:
            alpha = r
            s, num = check_alpha(s, alpha)
            count_alpha[alpha] -= num

    count = 0

    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] != "":
                count += 1

    return count

# 다른 사람 풀이
from collections import deque

def solution(storage, requests):
    answer = 0
    n, m = len(storage), len(storage[0])
    dxs, dys = (0, 1, 0, -1), (1, 0, -1, 0)

    new_st = [[0] * (m + 2)]
    for i in range(n):
        new_st.append([0] + list(storage[i]) + [0])
    new_st.append([0] * (m + 2))

    def in_range(x, y):
        return 0 <= x < len(new_st) and 0 <= y < len(new_st[0])

    def check_side():
        queue = deque([(0, 0)])
        visited = set([(0, 0)])
        while queue:
            x, y = queue.popleft()
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and (nx, ny) not in visited:
                    if new_st[nx][ny] == 0:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                    elif new_st[nx][ny] == target:
                        new_st[nx][ny] = 0
                        visited.add((nx, ny))

    for req in requests:
        target = req[0]
        if len(req) == 1:
            check_side()
        elif len(req) == 2:
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if new_st[i][j] == target:
                        new_st[i][j] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if new_st[i][j] != 0:
                answer += 1

    return answer