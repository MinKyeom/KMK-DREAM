# 내 풀이
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
        num_list = []

        x_1 = c[0]
        y_1 = c[1]
        x_2 = c[2]
        y_2 = c[3]

        tmp = map[x_1 - 1][y_1 - 1]

        # 맨 왼쪽

        for g in range(x_1 - 1, x_2 - 1):
            map[g][y_1 - 1] = map[g + 1][y_1 - 1]
            num_list.append(map[g][y_1 - 1])

        # num_list.append("first")

        # 맨 아랫줄 ok

        for f in range(y_1 - 1, y_2 - 1):
            map[x_2 - 1][f] = map[x_2 - 1][f + 1]
            num_list.append(map[x_2 - 1][f])

        # num_list.append("second")

        # 맨 오른쪽 ok
        for e in range(x_2 - 1, x_1 - 1, -1):
            map[e][y_2 - 1] = map[e - 1][y_2 - 1]
            num_list.append(map[e][y_2 - 1])

        # num_list.append("third")

        # 맨 윗줄 ok
        for d in range(y_2 - 1, y_1, -1):
            map[x_1 - 1][d] = map[x_1 - 1][d - 1]
            num_list.append(map[x_1 - 1][d])

        # print(num_list)
        map[x_1 - 1][y_1] = tmp

        num_list.append(map[x_1 - 1][y_1])

        result.append(min(num_list))

        # num_list.append("fourth")

        # print(num_list)
    return result
# 다른 사람 풀이

def solution(rows, columns, queries):
    answer = []

    board = [[i+(j)*columns for i in range(1,columns+1)] for j in range(rows)]
    # print(board)

    for a,b,c,d in queries:
        stack = []
        r1, c1, r2, c2 = a-1, b-1, c-1, d-1


        for i in range(c1, c2+1):

            stack.append(board[r1][i])
            if len(stack) == 1:
                continue
            else:
                board[r1][i] = stack[-2]


        for j in range(r1+1, r2+1):
            stack.append(board[j][i])
            board[j][i] = stack[-2]

        for k in range(c2-1, c1-1, -1):
            stack.append(board[j][k])
            board[j][k] = stack[-2]

        for l in range(r2-1, r1-1, -1):
            stack.append(board[l][k])
            board[l][k] = stack[-2]

        answer.append(min(stack))


    return answer

