#14502_연구소_bfs_gold5

# 1
from itertools import combinations
from copy import deepcopy

# 0: 빈 칸, 1: 벽, 2: 바이러스, 2이상 10미만
dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]
"""
상,하, 좌,우를 모두 확인하기 위하여
"""

# N: 세로, M: 가로
N, M = map(int, input().split())

W = 3  # 벽의 수

# 배열 입력
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))


def cnt_sf(_arr):
    _cnt = 0
    for _i in range(N):
        for _j in range(M):
            if _arr[_i][_j] == 0:
                _cnt += 1
    return _cnt
"""
내가 이해한 정도:안전지대 개수 찾기
"""

def virus_spread(x, y):
    # if virus then spread
    if arr[x][y] == 2:
        # spread recursively
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            """
            내가 이해한 정도:현재 위치에서 상하좌우를 의미"""
            # in range
            if 0 <= nx < N and 0 <= ny < M:
                """
                내가 이해한 정도:배열을 넘지 않게 if문 설정
                """
                # if not spread before and empty space
                if arr[nx][ny] == 0:
                    # spread
                    arr[nx][ny] = 2
                    virus_spread(nx, ny)


empty_space = []  # empty space
for i in range(N):
    for j in range(M):
        # possible wall space
        if arr[i][j] == 0:
            empty_space.append((i, j))

# possible wall zone
pos = combinations(empty_space, W)
"""
빈 영역 안에서 벽을 세우기 위하여 그것들 중 세개를 조합해서 뽑는다!
"""
answer = 0
tmp = deepcopy(arr)
"""
원래 배열을 보존하기 위하여 복사해놓는다.
"""

for state in pos:
    arr = deepcopy(tmp)
    # build new wall
    for x, y in state:
        """
        state는 (i,j)의 형태로 받았으니 for을 통해 할 시 x는 i를 y는 j를 받는다!
        
        """
        arr[x][y] = 1

    # virus spread
    for i in range(N):
        for j in range(M):
            virus_spread(i, j)
    answer = max(answer, cnt_sf(arr))

    # 0 0 2 2                 (0,3) 0,2
    # 0 0 0 1
    # 1 0 0 2


    """
    내가 이해한 정도:answer이라는 수를 통하여 수 많이 나오는 안전지대 개수(cnt_sf(arr)의 경우의 수 중 가장 큰 걸 지속적으로 받아서 변화시켜
    cnt_sf(arr)의 최대값을 찾아냈다. 
    즉 첫번쨰 cnt_sf(arr)=1 이었을 때 answer의 값은 1로 변함 
    하지만 그 다음의 조합에서는 cnt_sf(arr)의 값이 3이 나오면 answer의 값은 3이된다 바로 다음에 세번째에서 
    다시 cnt_sf(arr)=1 이었을때 answer의 값은 현재 3이므로 변하지 않는다. 이런 방식으로 계속 비교 후 가장 큰 값을 찾아내는것이다.
    """
    # print(cnt_sf(arr)) #내가 추가한 부분

print(answer)
