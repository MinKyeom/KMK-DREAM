"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/258707
"""

# 풀이 과정
# 최대 라운드의 수
# 미래에 카드가 있을 수도 있지만 그걸 위해 당장의 라운드를 넘겨야한다!
# 당장의 라운드를 넘기는거!!
# 코인을 안쓰고 손 안의 숫자 뭉치부터 써야한다!
from collections import deque


def solution(coin, cards):
    n = max(cards) + 1
    cards = deque(cards)
    hand = []  # 첫 카드 뭉치
    r = 1  # 라운드

    # 손에 든 뭉치 슬라이싱 두 번 사용의 경우 효율 떨어짐!
    for i in range(len(cards) // 3):
        k = cards.popleft()
        hand.append(k)

    check = []

    # game start
    while cards and coin >= 0 and True:

        flag = False  # 라운드 넘긴여부

        for j in range(2):
            new = cards.popleft()
            # # 라운드를 넘기는 수 하나가 손 안에 있는 경우
            # if (n-new) in hand and coin>0:
            #     hand.append(new)
            #     coin-=1
            # # 임시로 넣어두기!
            # else:
            check.append(new)

        # 라운드 통과 여부
        for i in range(1, ((n - 1) // 2) + 1):
            # 1순위 코인 안쓰고 손 안의 수로만!
            if i in hand and (n - i) in hand:
                one = hand.index(i)
                del hand[one]
                two = hand.index(n - i)
                del hand[two]
                flag = True
                r += 1
                break
        if flag == True:
            continue
            # 2순위 코인 한 개 쓰고 손 안의 수 소모
        for i in range(1, ((n - 1) // 2) + 1):
            if i in hand and (n - i) in check and coin > 0:
                one = hand.index(i)
                del hand[one]
                two = check.index(n - i)
                del check[two]
                flag = True
                r += 1
                coin -= 1
                break
            elif i in check and (n - i) in hand and coin > 0:
                one = check.index(i)
                del check[one]
                two = hand.index(n - i)
                del hand[two]
                flag = True
                r += 1
                coin -= 1
                break

        if flag == True:
            continue

        for i in range(1, ((n - 1) // 2) + 1):
            # 새로 뽑은 수를 다 가져오기
            if i in check and (n - i) in check and coin >= 2:
                one = check.index(i)
                del check[one]
                two = check.index(n - i)
                del check[two]
                r += 1
                coin -= 2
                flag = True
                break

        if flag == False:
            break

    return r

# 다른 사람 풀이
def solution(coin, cards):
    N = len(cards)
    hand = dict()
    coin1cnt = coin2cnt = 0
    for i in range(N//3):
        if hand.get(N+1-cards[i], False):
            coin1cnt += 1
        else:
            hand[cards[i]] = True
    draw = dict()
    for i in range(N//3, N, 2):
        for j in range(i, i+2):
            draw[cards[j]] = True
            draw[cards[j]] = True
            if hand.get(N+1-cards[j], False) and coin > 0:
                coin1cnt += 1
                coin -= 1
            if draw.get(N+1-cards[j], False):
                coin2cnt += 1
        if coin1cnt > 0:
            coin1cnt -= 1
        elif coin2cnt > 0 and coin > 1:
            coin2cnt -= 1
            coin -= 2
        else:
            return (i-N//3)//2+1
    return (N-N//3)//2+1