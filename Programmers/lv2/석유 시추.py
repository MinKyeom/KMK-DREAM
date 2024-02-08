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

