"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/250125
"""


# 풀이 과정
def solution(board, h, w):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    answer = 0

    for x, y in zip(dx, dy):
        if 0 <= h + x < len(board) and 0 <= w + y < len(board[0]):
            if board[h + x][w + y] == board[h][w]:
                answer += 1

    return answer

# 다른 사람 풀이
def solution(board, h, w):
    count = 0
    n = len(board)
    dh, dw = [0,1,-1,0],[1,0,0,-1]
    for i in range(4):
        h_check, w_check = h+dh[i], w+dw[i]
        if 0<=h_check<n and 0<=w_check<n:
            if board[h][w] == board[h_check][w_check]:
                count += 1
    return count