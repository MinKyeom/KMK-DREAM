# 내 풀이
from itertools import combinations, product
from collections import deque, Counter

# 각각의 주사위의 모든 경우의 수를 구한 후 승패 비교후 A가 이긴 걸 고르기!
def num(A, B):
    A_num = []
    B_num = []
    for i in range(len(A)):
        c = len(A_num)
        for j in range(len(A[i])):
            if i == 0:
                A_num.append(A[i][j])
                B_num.append(B[i][j])
            else:
                for d in range(c):
                    v = A_num[d]
                    w = B_num[d]
                    new_v = v + A[i][j]
                    new_w = w + B[i][j]
                    A_num.append(new_v)
                    B_num.append(new_w)

            A_num = deque(A_num)
            B_num = deque(B_num)

        for e in range(c):
            A_num.popleft()
            B_num.popleft()

    return Counter(A_num), Counter(B_num)


def solution(dice):
    d = [i for i in range(len(dice))]  # 주사위 번호
    # d_num=[j for j in range(len(dice[0]))]#주사위 면 번호
    k = deque(list(combinations(dice, len(dice) // 2)))  # A의 주사위
    # dice_num=list(product(d_num,repeat=len(dice)//2)) # 뽑는 주사위 면 순서
    check = []  # 이긴 주사위 모음
    result = []  # 이긴 주사위 번호
    check_num = []
    rate = 0

    while k:
        A = list(k.popleft())
        B = []
        A_num = []  # a주사위에서 나오는 모든 수
        B_num = []  # b주사위에서 나오는 모든 수

        # b 주사위 구하기
        for b in dice:
            if not b in A:
                B.append(b)

        # a,b의 숫자 모음
        A_num, B_num = num(A, B)
        win = 0
        for a in A_num:
            for b in B_num:
                if a > b:
                    win += (A_num[a] * B_num[b])

        if win > rate:
            rate = win
            check = A

    for r in check:
        t = dice.index(r)
        result.append(t + 1)

    return result


# 내 풀이(개선 중)
from itertools import combinations
from itertools import product
from collections import deque


# 각각의 주사위의 모든 경우의 수를 구한 후 승패 비교후 A가 이긴 걸 고르기!

def solution(dice):
    d = [i for i in range(len(dice))]  # 주사위 번호
    d_num = [j for j in range(len(dice[0]))]  # 주사위 면 번호
    k = deque(list(combinations(dice, len(dice) // 2)))  # A의 주사위
    dice_num = list(product(d_num, repeat=len(dice) // 2))  # 뽑는 주사위 면 순서
    check = []  # 이긴 주사위 모음
    result = []  # 이긴 주사위 번호
    rate = 0

    while k:
        A = list(k.popleft())
        B = []
        A_num = []  # a주사위에서 나오는 모든 수
        B_num = []  # b주사위에서 나오는 모든 수

        # b 주사위 구하기
        for b in dice:
            if not b in A:
                B.append(b)

        # a,b의 숫자 모음
        for i in dice_num:
            count_a = 0
            count_b = 0
            for n, j in enumerate(list(i)):
                count_a += A[n][j]
                count_b += B[n][j]
            A_num.append(count_a)
            B_num.append(count_b)

        # 숫자 비교
        # A_num.sort(reverse=True)
        # B_num.sort()
        A_num = deque(A_num)

        win = 0
        tie = 0
        lose = 0

        while A_num:
            a_num = A_num.popleft()
            for b_num in B_num:
                if a_num > b_num:
                    win += 1
                # elif a_num<b_num:
                #     break
                #     lose+=1
                # else:
                #     break
                #     tie+=1

        if win > rate:
            rate = win
            check = []
            check += A

    for r in check:
        t = dice.index(r)
        result.append(t + 1)

    return result
# 내 풀이 (개선 중)_2
from itertools import combinations
from itertools import product
from collections import deque


# 각각의 주사위의 모든 경우의 수를 구한 후 승패 비교후 A가 이긴 걸 고르기!

def solution(dice):
    d = [i for i in range(len(dice))]  # 주사위 번호
    d_num = [j for j in range(len(dice[0]))]  # 주사위 면 번호
    k = deque(list(combinations(dice, len(dice) // 2)))  # A의 주사위
    # dice_num=list(product(d_num,repeat=len(dice)//2)) # 뽑는 주사위 면 순서
    check = []  # 이긴 주사위 모음
    result = []  # 이긴 주사위 번호
    rate = 0

    while k:
        A = list(k.popleft())
        B = []
        A_num = []  # a주사위에서 나오는 모든 수
        B_num = []  # b주사위에서 나오는 모든 수

        # b 주사위 구하기
        for b in dice:
            if not b in A:
                B.append(b)

        # a,b의 숫자 모음
        for i in range(len(A)):
            c = len(A_num)
            for j in range(len(A[i])):
                if i == 0:
                    A_num.append(A[i][j])
                    B_num.append(B[i][j])
                else:
                    A_num = deque(A_num)
                    B_num = deque(B_num)
                    d = 0
                    while d < c:  # pop no for
                        v = A_num.popleft()
                        w = B_num.popleft()
                        new_v = v + A[i][j]
                        new_w = w + B[i][j]
                        A_num.append(new_v)
                        B_num.append(new_w)
                        d += 1
        print(A_num)

        # #a,b의 숫자 모음
        # for i in dice_num:
        #     count_a=0
        #     count_b=0
        #     for n,j in enumerate(list(i)):
        #         count_a+=A[n][j]
        #         count_b+=B[n][j]
        #     A_num.append(count_a)
        #     B_num.append(count_b)

        # 숫자 비교
        # A_num.sort(reverse=True)
        # B_num.sort()
        A_num = deque(A_num)

        win = 0
        tie = 0
        lose = 0

        while A_num:
            a_num = A_num.popleft()
            for b_num in B_num:
                if a_num > b_num:
                    win += 1
                # elif a_num<b_num:
                #     break
                #     lose+=1
                # else:
                #     break
                #     tie+=1

        if win > rate:
            rate = win
            check = []
            check += A

    for r in check:
        t = dice.index(r)
        result.append(t + 1)

    return

# 개선 중3
from itertools import combinations
from itertools import product
from collections import deque


# 각각의 주사위의 모든 경우의 수를 구한 후 승패 비교후 A가 이긴 걸 고르기!

def solution(dice):
    d = [i for i in range(len(dice))]  # 주사위 번호
    # d_num=[j for j in range(len(dice[0]))]#주사위 면 번호
    k = deque(list(combinations(dice, len(dice) // 2)))  # A의 주사위
    # dice_num=list(product(d_num,repeat=len(dice)//2)) # 뽑는 주사위 면 순서
    check = []  # 이긴 주사위 모음
    result = []  # 이긴 주사위 번호
    rate = 0

    while k:
        A = list(k.popleft())
        B = []
        A_num = []  # a주사위에서 나오는 모든 수
        B_num = []  # b주사위에서 나오는 모든 수

        # b 주사위 구하기
        for b in dice:
            if not b in A:
                B.append(b)

        # a,b의 숫자 모음
        for i in range(len(A)):
            c = len(A_num)
            for j in range(len(A[i])):
                if i == 0:
                    A_num.append(A[i][j])
                    B_num.append(B[i][j])
                else:
                    A_num = deque(A_num)
                    B_num = deque(B_num)

                    for d in range(c):
                        v = A_num[d]
                        w = B_num[d]
                        new_v = v + A[i][j]
                        new_w = w + B[i][j]
                        A_num.append(new_v)
                        B_num.append(new_w)
            for e in range(c):
                A_num.popleft()
                B_num.popleft()

        # #a,b의 숫자 모음
        # for i in dice_num:
        #     count_a=0
        #     count_b=0
        #     for n,j in enumerate(list(i)):
        #         count_a+=A[n][j]
        #         count_b+=B[n][j]
        #     A_num.append(count_a)
        #     B_num.append(count_b)

        # 숫자 비교
        # A_num.sort(reverse=True)
        # B_num.sort()
        A_num = deque(A_num)

        win = 0
        tie = 0
        lose = 0

        while A_num:
            a_num = A_num.popleft()
            for b_num in B_num:
                if a_num > b_num:
                    win += 1
                # elif a_num<b_num:
                #     break
                #     lose+=1
                # else:
                #     break
                #     tie+=1

        if win > rate:
            rate = win
            check = []
            check += A

    for r in check:
        t = dice.index(r)
        result.append(t + 1)

    return result
# 다른 사람 풀이

from itertools import combinations, product
from bisect import bisect_left


def solution(dice):
    dices = dice
    dice_indexes = range(len(dices))
    result = []
    for first_comb in combinations(dice_indexes, len(dice_indexes) // 2):
        first_dice_indexes = set(first_comb)
        second_dice_indexes = set(dice_indexes) - first_dice_indexes
        first_point_set = calcPointSet([dices[i] for i in first_dice_indexes])
        second_point_set = calcPointSet([dices[i] for i in second_dice_indexes])

        first_wins = 0
        for first_point in first_point_set:
            first_wins += bisect_left(second_point_set, first_point)

        result.append((first_comb, first_wins / 6 ** len(dice_indexes)))

    most_win_dice_indexes = list(sorted(result, key=lambda x: x[1], reverse=True))[0][0]

    return list(map(lambda x: x + 1, most_win_dice_indexes))


def calcPointSet(dices):
    point_set = []
    for _comb in product(*[range(6) for _ in range(len(dices))]):
        _sum = 0
        for index, dice in zip(_comb, dices):
            _sum += dice[index]
        point_set.append(_sum)

    return sorted(point_set)

