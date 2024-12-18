"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/340199
"""

#풀이과정
def solution(wallet, bill):
    count = 0

    while True:
        x, y = bill[0], bill[1]

        if wallet[0] >= x and wallet[1] >= y:
            break
        elif wallet[1] >= x and wallet[0] >= y:
            break

        else:
            bill[0], bill[1] = min(x, y), max(x, y) // 2
            count += 1

    return count