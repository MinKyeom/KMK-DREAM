# 내 풀이
# 틀린 이유 pop을 해버리면 도중에 다른 곳으로 이동할 때 A로 변한 부분을 거쳐갈 때 거리 커서 계산이 안됨
# 좌우 이동을 dfs로 풀이
# dfs
from collections import deque
import copy

eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# 커서 옮기는 방향 _ 왼쪽
def left(x, y, z):
    if len(x) == x.count("A"):
        return x, y, z

    while True:
        y += 1
        z -= 1

        if x[z] != "A":
            t = eng.find(x[z])
            break

    if t >= 13:
        t = 26 - t
    y += t

    x[z] = "A"

    return x, y, z


# 커서 옮기는 방향 _ 오른쪽
def right(x, y, z):
    if len(x) == x.count("A"):
        return x, y, z

    while True:
        y += 1
        z += 1

        if x[z] != "A":
            t = eng.find(x[z])
            break

    if t >= 13:
        t = 26 - t
    y += t

    x[z] = "A"

    return x, y, z


def solution(name):
    start = "A" * len(name)
    check = deque(list(name))
    result = []

    # 첫번째_커서 시작 위치
    k = eng.find(check[0])

    if k >= 13:
        k = 26 - k

    count = k

    check[0] = "A"

    if len(check) == check.count("A"):
        return count

    q = deque([check])
    count_q = deque([k])
    point_q = deque([0])  # 방향키 위치

    while q:
        one = q.popleft()
        two = count_q.popleft()
        three = point_q.popleft()

        one_right = copy.deepcopy(one)
        two_right = copy.deepcopy(two)
        three_right = copy.deepcopy(three)

        left_q, left_num, left_p = left(one, two, three)
        right_q, right_num, right_p = right(one_right, two_right, three_right)

        if len(left_q) == left_q.count("A"):
            result.append(left_num)
        else:
            q.append(left_q)
            count_q.append(left_num)
            point_q.append(left_p)

        if len(right_q) == right_q.count("A"):
            result.append(right_num)
        else:
            q.append(right_q)
            count_q.append(right_num)
            point_q.append(right_p)

    return min(result) if len(result) > 0 else 0
# 다른 사람 풀이
def solution(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    for ch in name:
        answer += alphabet_to_num(ch)

    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer
