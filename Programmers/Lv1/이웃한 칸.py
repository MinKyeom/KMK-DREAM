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