# 내 풀이 (개선 중)
# bfs 활용
from collections import deque


def solution(board):
    result = []
    q = deque([])

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                q.append([i, j])

    if len(q) == 0:
        return 0
    elif len(q) == len(board) * len(board[0]):
        return len(q)

    dx = [1, 0, 1]
    dy = [0, 1, 1]

    while q:
        x, y = q.popleft()
        new_q = deque([[x, y]])

        count = 1
        new = []

        while True or new_q:
            new_x, new_y = new_q.popleft()

            for v, w in zip(dx, dy):
                if 0 <= new_x + v < len(board) and 0 <= new_y + w < len(board[0]) and board[new_x + v][new_y + w] == 1:
                    if [new_x + v, new_y + w] not in new:
                        new.append([new_x + v, new_y + w])
                else:
                    break
            else:
                if len(new_q) == 0:
                    count += 1
                    new_q += new
                    new = []
                    continue
                else:
                    continue
            break

        result.append(count ** 2)

    return max(result)


"""
# sol2  정확도 100 효율성 0
from collections import deque
def solution(board):
    result=0
    q=deque([])

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==1:
                q.append([i,j])

    if len(q)==0:
        return 0

    elif 0<len(q)<4:
        return 1


    dx=[1,0,1]
    dy=[0,1,1]

    while q:
        x,y=q.popleft()
        count=1

        while True:
            for a in range(0,count+1):
                for b in range(0,count+1):
                    if 0<=x+a<len(board) and 0<=y+b<len(board[0]) and board[x+a][y+b]==1:
                        continue
                    else:
                        break
                else:
                    continue
                break        

            else:
                count+=1
                continue

            break

        if count**2>result:
            result=(count)**2

    return result
"""
