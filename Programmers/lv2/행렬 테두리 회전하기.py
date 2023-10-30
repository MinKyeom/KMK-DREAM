# 내 풀이(개선 중)
def solution(rows, columns, queries):
    import copy
    from collections import deque
    result = []
    map = [[False for col in range(columns)] for a in range(rows)]
    count = 1

    # 기본 맵
    for a in range(rows):
        for b in range(columns):
            map[a][b] = count
            count += 1

    # 맵 모양 변경
    for c in queries:
        check = copy.deepcopy(map)
        # check=map.copy()
        num_list = []

        x_1 = c[0]
        y_1 = c[1]
        x_2 = c[2]
        y_2 = c[3]

        # 맨 윗줄 ok

        for d in range(y_1, y_2):
            check[x_1 - 1][d] = map[x_1 - 1][d - 1]
            num_list.append(check[x_1 - 1][d])

        # num_list.append("first")

        # 맨 오른쪽 ok

        for e in range(x_1, x_2):
            check[e][y_2 - 1] = map[e - 1][y_2 - 1]
            num_list.append(check[e][y_2 - 1])

        # num_list.append("second")

        # 맨 아랫줄 ok

        for f in range(y_1 - 1, y_2 - 1):
            check[x_2 - 1][f] = map[x_2 - 1][f + 1]
            num_list.append(check[x_2 - 1][f])

        # num_list.append("third")

        # 맨 왼쪽

        for g in range(x_1 - 1, x_2 - 1):
            check[g][y_1 - 1] = map[g + 1][y_1 - 1]
            num_list.append(check[g][y_1 - 1])

        # num_list.append("fourth")

        result.append(min(num_list))

        map = check

    return result
# 다른 사람 풀이
