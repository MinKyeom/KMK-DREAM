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


# 다른 사람 풀이

def solution(wallet, bill):

    wallet, bill = sorted(wallet), sorted(bill)
    cnt = 0
    while wallet[0] < bill[0] or wallet[1] < bill[1]:
        bill[-1] //= 2
        bill = sorted(bill)
        cnt += 1

    return cnt

# 다른 사람 풀이
def solution(wallet, bill):
    result = 0

    while True:
        wallet.sort()
        bill.sort()

        if bill[0] <= wallet[0] and bill[1] <= wallet[1]:
            break

        bill[1] //= 2
        result += 1

    return result

