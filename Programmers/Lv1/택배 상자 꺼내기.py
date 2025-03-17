"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/389478?language=python3
"""

"""
2줄마다 나머지*2차이가 나는 사실을 생각하여 좀 더 효율적으로 개선이 될 거 같다
하지만 시간복잡도 효율상 좋진 않으나, 전체 택배 물건들을 리스트 내로 배열한 후 찾고자 하는 택배 위치를 찾은 후
해당 위치를 이동하여 택배 여부를 확인하는 방식으로 1차적으로 답을 구해낼 수 있었다.
"""


# 풀이과정
def solution(n, w, num):
    if n % w == 0:
        floor = (n // w)

    else:
        floor = (n // w) + 1

    block = [[False] * w for _ in range(floor)]

    for i in range(n):
        now = i // w
        where = ((i + 1) % w) - 1

        if where == -1:
            where = w - 1

        if now % 2 == 0:
            block[now][where] = i + 1

        else:
            block[now][w - where - 1] = i + 1

    for i in range(floor):
        for j in range(w):
            if block[i][j] == num:
                nx, ny = i, j
                break

    result = 1

    while True:
        if nx + 1 > floor - 1:
            break
        else:
            if block[nx + 1][ny] != False:
                nx += 1
                result += 1
            else:
                break

    return result