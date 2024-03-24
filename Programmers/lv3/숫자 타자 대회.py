# 내 풀이
# 목표: 최소한의 시간으로 타이핑을 하는 경우의 가중치
# 이동하지 않고 제자리 누르기:1 상하좌우 이동 후 누르기:2 대각선:3

# 왼손 오른손 중 가중치가 제일 적은 경우의 수들의 합
# 같은 번호에 두 손가락 놓는거 불가
# 상하좌우 두 번 가는것보다 대각선 한 번이 더 이득
# 최솟값+최솟값 = 최솟값 명제는 항상 성립
# 번호판을 dp로 생각 후 마지막 번호의 dp값이 가중치 최솟값으로 생각접근해보기

# 다시 정리하는 dic.items(): key,value 둘다
# dic.keys(): key 값
# dic.values(): values 모두 키값에 관계없이 모두
from collections import deque


# 왼손 가중치 계산
def left_hand(new_x, new_y):
    l = 0
    while True:
        if new_x > 0 and new_y > 0:
            l += 3
            new_x -= 1
            new_y -= 1
        elif new_x > 0 and new_y == 0:
            l += 2
            new_x -= 1
        elif new_x == 0 and new_y > 0:
            l += 2
            new_y -= 1
        elif new_x == 0 and new_y == 0:
            l += 1
            break
        if new_x == 0 and new_y == 0:
            break
    return l


# 오른손 가중치 계산
def right_hand(new_x, new_y):
    r = 0
    while True:
        if new_x > 0 and new_y > 0:
            r += 3
            new_x -= 1
            new_y -= 1
        elif new_x > 0 and new_y == 0:
            r += 2
            new_x -= 1
        elif new_x == 0 and new_y > 0:
            r += 2
            new_y -= 1
        elif new_x == 0 and new_y == 0:
            r += 1
            break
        if new_x == 0 and new_y == 0:
            break

    return r


# 숫자 위치
def point(k, i):
    # i의 번호 찾기
    for a in range(4):
        for b in range(3):
            if k[a][b] == i:
                x = a
                y = b
                break
    return x, y


from collections import deque


def solution(numbers):
    k = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]

    num = list("123456789*0#")

    n = list(numbers)

    last = n[-1]

    # 이전 가중치
    # 이전에 해당번호에 도달했을때 가중치가 가장 적은 경우를 저장한 후 after의 최솟값으로 재갱신
    # before={"1":0, "2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"*":0,"#":7}

    # m 각 그래프 위치에 따른 가중치

    m = [[0] * 12 for _ in range(12)]

    # i>j
    for i in range(12):
        x, y = point(k, num[i])
        for j in range(12):
            dx, dy = point(k, num[j])
            new_x = abs(x - dx)
            new_y = abs(y - dy)
            m[i][j] = right_hand(new_x, new_y)

    w = 0
    left = "4"
    right = "6"

    # 현재 들어있는 손 가중치
    now = {}

    hand = (left, right)

    now[hand] = w

    # p: numbers num:위치 인덱스 담은 배열

    for c in n:
        after = {}  # 다음 손 가중치
        c_num = num.index(c)
        # c: 누를 번호

        # h:손 n_w:손 가중치 (이전 손 위치로부터 온 가중치)
        # 이전 위치에서 온 가중치들을 저장함과 동시에 도착할 위치중 중복 위치시 최솟값으로 매 번 갱신 그 뿐만 아니라
        # 중복된 위치는 dic으로 제거하기에 최대 갯수는 12**2로 유지된다 그 이상으로 늘어나지 않는다
        for h, n_w in now.items():
            l, r = h  # 왼손, 오른손

            l_num = num.index(l)
            r_num = num.index(r)

            if r == c:
                if not (l, c) in after.keys() or now[(l, c)] > n_w + 1:
                    # 이해 과정: or 뒤의 두 번째 조건은 최소값일 경우 재갱신을 위해서이다!
                    after[(l, c)] = n_w + 1

            elif l == c:
                if not (c, r) in after.keys() or now[(c, r)] > n_w + 1:
                    after[(c, r)] = n_w + 1

            else:
                if not (l, c) in after.keys() or after[(l, c)] > n_w + m[r_num][c_num]:
                    after[(l, c)] = n_w + m[r_num][c_num]
                if not (c, r) in after.keys() or after[(c, r)] > n_w + m[l_num][c_num]:
                    after[(c, r)] = n_w + m[l_num][c_num]

            now = after

    return min(list(now.values()))

# 내 풀이(개선 중)
# 목표: 최소한의 시간으로 타이핑을 하는 경우의 가중치
# 이동하지 않고 제자리 누르기:1 상하좌우 이동 후 누르기:2 대각선:3

# 왼손 오른손 중 가중치가 제일 적은 경우의 수들의 합
# 같은 번호에 두 손가락 놓는거 불가
# 상하좌우 두 번 가는것보다 대각선 한 번이 더 이득
# 최솟값+최솟값 = 최솟값 명제는 항상 성립
# 번호판을 dp로 생각 후 마지막 번호의 dp값이 가중치 최솟값으로 생각접근해보기

# 행렬로 접근 후 메모제이션을 지속적으로 해주는 방향에서 고민의 방향 접근!

from collections import deque


# 왼손 가중치 계산
def left_hand(new_x, new_y):
    l = 0
    while True:
        if new_x > 0 and new_y > 0:
            l += 3
            new_x -= 1
            new_y -= 1
        elif new_x > 0 and new_y == 0:
            l += 2
            new_x -= 1
        elif new_x == 0 and new_y > 0:
            l += 2
            new_y -= 1
        elif new_x == 0 and new_y == 0:
            l += 1
            break
        if new_x == 0 and new_y == 0:
            break
    return l


# 오른손 가중치 계산
def right_hand(new_x, new_y):
    r = 0
    while True:
        if new_x > 0 and new_y > 0:
            r += 3
            new_x -= 1
            new_y -= 1
        elif new_x > 0 and new_y == 0:
            r += 2
            new_x -= 1
        elif new_x == 0 and new_y > 0:
            r += 2
            new_y -= 1
        elif new_x == 0 and new_y == 0:
            r += 1
            break
        if new_x == 0 and new_y == 0:
            break

    return r


# 숫자 위치
def point(k, i):
    # i의 번호 찾기
    for a in range(4):
        for b in range(3):
            if k[a][b] == i:
                x = a
                y = b
                break
    return x, y


from collections import deque


def solution(numbers):
    k = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]

    num = list("123456789*0#")
    n = list(numbers)

    last = n[-1]

    # 이전 가중치
    # 이전에 해당번호에 도달했을때 가중치가 가장 적은 경우를 저장한 후 after의 최솟값으로 재갱신
    # before={"1":0, "2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"*":0,"#":7}

    # m 각 그래프 위치에 따른 가중치

    m = [[0] * 12 for _ in range(12)]

    # i>j
    for i in range(12):
        x, y = point(k, num[i])
        for j in range(12):
            dx, dy = point(k, num[j])
            new_x = abs(x - dx)
            new_y = abs(y - dy)
            m[i][j] = right_hand(new_x, new_y)

    t = list("123456789*0#")

    now_weight = 0
    left = 4
    right = 6
    all_dict = {}

    hand = (left, right)
    all_dict[hand] = now_weight

    for str_num in n:
        num = int(str_num)
        # num=int(str_num)
        curr_dict = {}

        for hand, weight in all_dict.items():
            left, right = hand
            if right == num:
                if not (left, num) in curr_dict.keys() or curr_dict[(left, num)] > weight + 1:
                    curr_dict[(left, num)] = weight + 1

            elif left == num:
                if not (num, right) in curr_dict.keys() or curr_dict[(num, right)] > weight + 1:
                    curr_dict[(num, right)] == weight + 1

            else:
                if not (left, num) in curr_dict.keys() or curr_dict[(left, num)] > weight + m[right][num]:
                    curr_dict[(left, num)] = weight + m[right][num]

                if not (num, right) in curr_dict.keys() or curr_dict[(num, right)] > weight + m[left][num]:
                    curr_dict[(num, right)] = weight + m[left][num]

        all_dict = curr_dict

    return min(all_dict.values())
# 목표: 최소한의 시간으로 타이핑을 하는 경우의 가중치
# 이동하지 않고 제자리 누르기:1 상하좌우 이동 후 누르기:2 대각선:3

# 왼손 오른손 중 가중치가 제일 적은 경우의 수들의 합
# 같은 번호에 두 손가락 놓는거 불가
# 상하좌우 두 번 가는것보다 대각선 한 번이 더 이득
# 최솟값+최솟값 = 최솟값 명제는 항상 성립
# 번호판을 dp로 생각 후 마지막 번호의 dp값이 가중치 최솟값으로 생각접근해보기


from collections import deque


# 왼손 가중치 계산
def left_hand(new_x, new_y):
    l = 0
    while True:
        if new_x > 0 and new_y > 0:
            l += 3
            new_x -= 1
            new_y -= 1
        elif new_x > 0 and new_y == 0:
            l += 2
            new_x -= 1
        elif new_x == 0 and new_y > 0:
            l += 2
            new_y -= 1
        elif new_x == 0 and new_y == 0:
            l += 1
            break
        if new_x == 0 and new_y == 0:
            break
    return l


# 오른손 가중치 계산
def right_hand(new_x, new_y):
    r = 0
    while True:
        if new_x > 0 and new_y > 0:
            r += 3
            new_x -= 1
            new_y -= 1
        elif new_x > 0 and new_y == 0:
            r += 2
            new_x -= 1
        elif new_x == 0 and new_y > 0:
            r += 2
            new_y -= 1
        elif new_x == 0 and new_y == 0:
            r += 1
            break
        if new_x == 0 and new_y == 0:
            break

    return r


# 숫자 위치
def point(k, i):
    # i의 번호 찾기
    for a in range(4):
        for b in range(3):
            if k[a][b] == i:
                x = a
                y = b
                break
    return x, y


from collections import deque


def solution(numbers):
    k = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]

    num = list("123456789*0#")
    n = list(numbers)

    last = n[-1]

    # 이전 가중치
    # 이전에 해당번호에 도달했을때 가중치가 가장 적은 경우를 저장한 후 after의 최솟값으로 재갱신
    # before={"1":0, "2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"*":0,"#":7}

    # m 각 그래프 위치에 따른 가중치

    m = [[0] * 12 for _ in range(12)]

    # i>j
    for i in range(12):
        x, y = point(k, num[i])
        for j in range(12):
            dx, dy = point(k, num[j])
            new_x = abs(x - dx)
            new_y = abs(y - dy)
            m[i][j] = right_hand(new_x, new_y)

    t = list("123456789*0#")

    now_weight = 0
    left = 4
    right = 6
    all_dict = {}

    hand = (left, right)
    all_dict[hand] = now_weight

    for str_num in n:
        num = int(str_num)
        # num=int(str_num)
        curr_dict = {}

        for hand, weight in all_dict.items():
            left, right = hand
            if right == num:
                if not (left, num) in curr_dict.keys() or curr_dict[(left, num)] > weight + 1:
                    curr_dict[(left, num)] = weight + 1

            elif left == num:
                if not (num, right) in curr_dict.keys() or curr_dict[(num, right)] > weight + 1:
                    curr_dict[(num, right)] == weight + 1

            else:
                if not (left, num) in curr_dict.keys() or curr_dict[(left, num)] > weight + m[right][num]:
                    curr_dict[(left, num)] = weight + m[right][num]

                if not (num, right) in curr_dict.keys() or curr_dict[(num, right)] > weight + m[left][num]:
                    curr_dict[(num, right)] = weight + m[left][num]

        all_dict = curr_dict

    return min(all_dict.values())


# 내 풀이(개선 중 숫자 번호는 12개라는 점 고려해서 개선하려고 함)
# 목표: 최소한의 시간으로 타이핑을 하는 경우의 가중치
# 이동하지 않고 제자리 누르기:1 상하좌우 이동 후 누르기:2 대각선:3

# 왼손 오른손 중 가중치가 제일 적은 경우의 수들의 합
# 같은 번호에 두 손가락 놓는거 불가
# 상하좌우 두 번 가는것보다 대각선 한 번이 더 이득
# 최솟값+최솟값 = 최솟값 명제는 항상 성립
# 번호판을 dp로 생각 후 마지막 번호의 dp값이 가중치 최솟값으로 생각접근해보기


from collections import deque


# 왼손 가중치 계산
def left_hand(new_x, new_y):
    l = 0
    while True:
        if new_x > 0 and new_y > 0:
            l += 3
            new_x -= 1
            new_y -= 1
        elif new_x > 0 and new_y == 0:
            l += 2
            new_x -= 1
        elif new_x == 0 and new_y > 0:
            l += 2
            new_y -= 1
        elif new_x == 0 and new_y == 0:
            l += 1
            break
        if new_x == 0 and new_y == 0:
            break
    return l


# 오른손 가중치 계산
def right_hand(new_x, new_y):
    r = 0
    while True:
        if new_x > 0 and new_y > 0:
            r += 3
            new_x -= 1
            new_y -= 1
        elif new_x > 0 and new_y == 0:
            r += 2
            new_x -= 1
        elif new_x == 0 and new_y > 0:
            r += 2
            new_y -= 1
        elif new_x == 0 and new_y == 0:
            r += 1
            break
        if new_x == 0 and new_y == 0:
            break

    return r


# 숫자 위치
def point(k, i):
    # i의 번호 찾기
    for a in range(4):
        for b in range(3):
            if k[a][b] == i:
                x = a
                y = b
                break
    return x, y


def solution(numbers):
    k = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]

    #     result=0

    #     left=k[1][0]

    #     l_x=1
    #     l_y=0

    #     right=k[1][2]

    #     r_x=1
    #     r_y=2

    n = list(numbers)

    dp = [0 for _ in range(12)]

    dp_num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "0", "#"]

    check = deque([["4", "6"]])  # 왼손 오른손 가중치

    for t in range(len(n)):
        i = n[t]
        x, y = point(k, i)
        new = []
        d = []  # 거리 가중치값들 모음

        # j=dp_num.index(i)

        while check:
            left, right = check.popleft()
            # dx,dy=point(k,num)
            if not [right, i] in new and not [i, right] in new:
                new.append([right, i])
            if not [left, i] in new and not [i, left] in new:
                new.append([left, i])

        # 이전 길에 따른 가중치 기록이 필요하다!!

        check += new

        print(check)

    return 0
# 내 풀이(개선 중 뒤를 돌아본 후 이전꺼 재결정 풀이)
# 목표: 최소한의 시간으로 타이핑을 하는 경우의 가중치
# 이동하지 않고 제자리 누르기:1 상하좌우 이동 후 누르기:2 대각선:3

# 왼손 오른손 중 가중치가 제일 적은 경우의 수들의 합
# 같은 번호에 두 손가락 놓는거 불가
# 상하좌우 두 번 가는것보다 대각선 한 번이 더 이득
# 최솟값+최솟값 = 최솟값 명제는 항상 성립


from collections import deque


# 왼손 가중치 계산
def left_hand(new_x, new_y):
    l = 0
    while True:
        if new_x > 0 and new_y > 0:
            l += 3
            new_x -= 1
            new_y -= 1
        elif new_x > 0 and new_y == 0:
            l += 2
            new_x -= 1
        elif new_x == 0 and new_y > 0:
            l += 2
            new_y -= 1
        elif new_x == 0 and new_y == 0:
            l += 1
            break
        if new_x == 0 and new_y == 0:
            break
    return l


# 오른손 가중치 계산
def right_hand(new_x, new_y):
    r = 0
    while True:
        if new_x > 0 and new_y > 0:
            r += 3
            new_x -= 1
            new_y -= 1
        elif new_x > 0 and new_y == 0:
            r += 2
            new_x -= 1
        elif new_x == 0 and new_y > 0:
            r += 2
            new_y -= 1
        elif new_x == 0 and new_y == 0:
            r += 1
            break
        if new_x == 0 and new_y == 0:
            break

    return r


# 숫자 위치
def point(k, i):
    # i의 번호 찾기
    for a in range(4):
        for b in range(3):
            if k[a][b] == i:
                x = a
                y = b
                break
    return x, y


def solution(numbers):
    k = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]

    result = 0

    left = k[1][0]

    l_x = 1
    l_y = 0

    right = k[1][2]

    r_x = 1
    r_y = 2

    n = deque(list(numbers))

    while n:
        i = n.popleft()

        # i의 번호 찾기
        x, y = point(k, i)

        # 왼손으로 하였을 떄 가중치
        l = 0  # 왼손 가중치
        new_x = abs(l_x - x)
        new_y = abs(l_y - y)
        l = left_hand(new_x, new_y)

        # 오른손으로 하였을 때 가중치
        r = 0  # 오른손 가중치
        new_x = abs(r_x - x)
        new_y = abs(r_y - y)
        r = right_hand(new_x, new_y)

        if r < l:
            result += r
            right = i
            r_x = x
            r_y = y

        elif l < r:
            result += l
            left = i
            l_x = x
            l_y = y

        # 그 다음 수를 향하는 가중치를 비교하여 이전 것을 선택
        elif l == r and len(n) == 0:
            result += l

        else:
            # print("check",i)
            check_count = 0
            while check_count < len(n):
                j = n[check_count]
                check_x, check_y = point(k, j)

                result_x = 0  # x가 옮겨졌을 떄의 최소 가중치
                result_y = 0  # y가 옮겨졌을 때의 최소 가중치

                # x가 옮겨지고 y는 그대로 가중치

                # 왼손
                one_r = 0  # 오른손 가중치
                new_x = abs(check_x - x)
                new_y = abs(check_y - y)
                one_r = right_hand(new_x, new_y)

                # 오른손
                one_l = 0  # 왼손 가중치
                new_x = abs(check_x - l_x)
                new_y = abs(check_y - l_y)
                one_l = left_hand(new_x, new_y)

                if one_l < one_r:
                    result_x = one_l
                else:
                    result_x = one_r

                # y가 옮겨지고 x는 그대로 가중치

                # 왼손
                one_r = 0  # 오른손 가중치
                new_x = abs(check_x - r_x)
                new_y = abs(check_y - r_y)
                two_r = right_hand(new_x, new_y)

                # 오른손
                one_l = 0  # 왼손 가중치
                new_x = abs(check_x - x)
                new_y = abs(check_y - y)
                two_l = left_hand(new_x, new_y)

                if two_l < two_r:
                    result_y = two_l
                else:
                    result_y = two_r

                if result_y < result_x:
                    # y를 옮기는게 맞아진다
                    left = i
                    l_x = x
                    l_y = y
                    result += l
                    break
                elif result_x < result_y:
                    right = i
                    r_x = x
                    r_y = y
                    result += r
                    break
                else:
                    check_count += 1

        print(result)

    return result
# 내 풀이(개선 중)
# 목표: 최소한의 시간으로 타이핑을 하는 경우의 가중치
# 이동하지 않고 제자리 누르기:1 상하좌우 이동 후 누르기:2 대각선:3

# 왼손 오른손 중 가중치가 제일 적은 경우의 수들의 합
# 같은 번호에 두 손가락 놓는거 불가
# 상하좌우 두 번 가는것보다 대각선 한 번이 더 이득
# 최솟값+최솟값 = 최솟값 명제는 항상 성립


from collections import deque

# 왼손 가중치 계산
def left_hand(new_x, new_y):
    while True:
        l = 0
        if new_x > 0 and new_y > 0:
            l += 3
            new_x -= 1
            new_y -= 1
        elif new_x > 0 and new_y == 0:
            l += 2
            new_x -= 1
        elif new_x == 0 and new_y > 0:
            l += 2
            new_y -= 1
        elif new_x == 0 and new_y == 0:
            l += 1
            break
        if new_x == 0 and new_y == 0:
            break
    return l


# 오른손 가중치 계산
def right_hand(new_x, new_y):
    while True:
        r = 0
        if new_x > 0 and new_y > 0:
            r += 3
            new_x -= 1
            new_y -= 1
        elif new_x > 0 and new_y == 0:
            r += 2
            new_x -= 1
        elif new_x == 0 and new_y > 0:
            r += 2
            new_y -= 1
        elif new_x == 0 and new_y == 0:
            r += 1
            break
        if new_x == 0 and new_y == 0:
            break

    return r


# 숫자 위치
def point(k, i):
    # i의 번호 찾기
    for a in range(4):
        for b in range(3):
            if k[a][b] == i:
                x = a
                y = b
                break
    return x, y


def solution(numbers):
    k = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]

    result = 0

    left = k[1][0]

    l_x = 1
    l_y = 0

    right = k[1][2]

    r_x = 1
    r_y = 2

    n = deque(list(numbers))

    while n:
        i = n.popleft()

        # i의 번호 찾기
        x, y = point(k, i)

        # 왼손으로 하였을 떄 가중치
        l = 0  # 왼손 가중치
        new_x = abs(l_x - x)
        new_y = abs(l_y - y)

        l = left_hand(new_x, new_y)

        r = 0  # 오른손 가중치
        new_x = abs(r_x - x)
        new_y = abs(r_y - y)

        r = right_hand(new_x, new_y)

        # if r<l:
        #     right=i
        #     r_x=x
        #     r_y=y
        #     result+=r
        # elif l<r:
        #     left=i
        #     l_x=x
        #     l_y=y
        #     result+=l

        print(r, l)
        break

    # # 같을 경우는 다음 수를 바탕으로 정해야한다.
    # elif l==r:
    #     j=n.popleft()

    return 0
# 내 풀이(개선 중)
# 목표: 최소한의 시간으로 타이핑을 하는 경우의 가중치
# 이동하지 않고 제자리 누르기:1 상하좌우 이동 후 누르기:2 대각선:3

# 왼손 오른손 중 가중치가 제일 적은 경우의 수들의 합
# 같은 번호에 두 손가락 놓는거 불가
# 상하좌우 두 번 가는것보다 대각선 한 번이 더 이득
# 최솟값+최솟값 = 최솟값 명제는 항상 성립


from collections import deque


# 왼손 가중치 계산
def left_hand(new_x, new_y):
    while True:
        l = 0
        if new_x > 0 and new_y > 0:
            l += 3
            new_x -= 1
            new_y -= 1
        elif new_x > 0 and new_y == 0:
            l += 2
            new_x -= 1
        elif new_x == 0 and new_y > 0:
            l += 2
            new_y -= 1
        elif new_x == 0 and new_y == 0:
            l += 1
            break
        if new_x == 0 and new_y == 0:
            break
    return l


# 오른손 가중치 계산
def right_hand(new_x, new_y):
    while True:
        r = 0
        if new_x > 0 and new_y > 0:
            r += 3
            new_x -= 1
            new_y -= 1
        elif new_x > 0 and new_y == 0:
            r += 2
            new_x -= 1
        elif new_x == 0 and new_y > 0:
            r += 2
            new_y -= 1
        elif new_x == 0 and new_y == 0:
            r += 1
            break
        if new_x == 0 and new_y == 0:
            break

    return r


# 숫자 위치
def point(k, i):
    # i의 번호 찾기
    for a in range(4):
        for b in range(3):
            if k[a][b] == i:
                x = a
                y = b
                break
    return x, y


def solution(numbers):
    k = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]

    result = 0

    left = k[1][0]

    l_x = 1
    l_y = 0

    right = k[1][2]

    r_x = 1
    r_y = 2

    n = deque(list(numbers))

    while n:
        i = n.popleft()

        # i의 번호 찾기
        x, y = point(k, i)

        # 왼손으로 하였을 떄 가중치
        l = 0  # 왼손 가중치
        new_x = abs(l_x - x)
        new_y = abs(l_y - y)

        l = left_hand(new_x, new_y)

        r = 0  # 오른손 가중치
        new_x = abs(r_x - x)
        new_y = abs(r_y - y)

        r = right_hand(new_x, new_y)

        # if r<l:
        #     right=i
        #     r_x=x
        #     r_y=y
        #     result+=r
        # elif l<r:
        #     left=i
        #     l_x=x
        #     l_y=y
        #     result+=l

        print(r, l)
        break

    # # 같을 경우는 다음 수를 바탕으로 정해야한다.
    # elif l==r:
    #     j=n.popleft()

    return 0

# 다른 사람 풀이
def solution(numbers):
    now_weight = 0
    left_pos = 4
    right_pos = 6
    all_dict = {}
    finger_pos = (left_pos, right_pos)
    all_dict[finger_pos] = now_weight

    for str_num in numbers:
        num = int(str_num)
        curr_dict = {}
        for finger_pos, weight in all_dict.items():
            left_pos, right_pos = finger_pos
            if right_pos == num:
                if not (left_pos, num) in curr_dict.keys() or curr_dict[(left_pos, num)] > weight + 1:
                    curr_dict[(left_pos, num)] = weight + 1
            elif left_pos == num:
                if not (num, right_pos) in curr_dict.keys() or curr_dict[(num, right_pos)] > weight + 1:
                    curr_dict[(num, right_pos)] = weight + 1
            else:
                if not (left_pos, num) in curr_dict.keys() or curr_dict[(left_pos, num)] > weight + costs[right_pos][
                    num]:
                    curr_dict[(left_pos, num)] = weight + costs[right_pos][num]
                if not (num, right_pos) in curr_dict.keys() or curr_dict[(num, right_pos)] > weight + costs[left_pos][
                    num]:
                    curr_dict[(num, right_pos)] = weight + costs[left_pos][num]
        all_dict = curr_dict

    return min(list(all_dict.values()))

# 다른 사람 풀이
def solution(numbers):
    answer = 0

    costs = [[1, 7, 6, 7, 5, 4, 5, 3, 2, 3]
        , [7, 1, 2, 4, 2, 3, 5, 4, 5, 6]
        , [6, 2, 1, 2, 3, 2, 3, 5, 4, 5]
        , [7, 4, 2, 1, 5, 3, 2, 6, 5, 4]
        , [5, 2, 3, 5, 1, 2, 4, 2, 3, 5]
        , [4, 3, 2, 3, 2, 1, 2, 3, 2, 3]
        , [5, 5, 3, 2, 4, 2, 1, 5, 3, 2]
        , [3, 4, 5, 6, 2, 3, 5, 1, 2, 4]
        , [2, 5, 4, 5, 3, 2, 3, 2, 1, 2]
        , [3, 6, 5, 4, 5, 3, 2, 4, 2, 1]]

    cost = 0
    left = 4
    right = 6
    allDict = {}
    allDict[(left, right)] = cost

    newNumbers = list(numbers)

    for number in newNumbers:
        num = int(number)

        currentDict = {}
        for key, value in allDict.items():
            currentLeft, currentRight = key

            if currentRight == num:
                if (currentLeft, num) not in currentDict or currentDict[(currentLeft, num)] > value + 1:
                    currentDict[(currentLeft, num)] = value + 1
            elif currentLeft == num:
                if (num, currentRight) not in currentDict or currentDict[(num, currentRight)] > value + 1:
                    currentDict[(num, currentRight)] = value + 1
            else:
                if (currentLeft, num) not in currentDict or currentDict[(currentLeft, num)] > value + \
                        costs[currentRight][num]:
                    currentDict[(currentLeft, num)] = value + costs[currentRight][num]

                if (num, currentRight) not in currentDict or currentDict[(num, currentRight)] > value + \
                        costs[currentLeft][num]:
                    currentDict[(num, currentRight)] = value + costs[currentLeft][num]

        allDict = currentDict

    answer = (min(allDict.values()))

    return answer

# 다른 사람 풀이 (dp 활용)
def solution(numbers):
    key = {0:(3,1), **{n:divmod(n-1,3) for n in range(1,10)}}

    ws = [[1]*10 for _ in range(10)]
    for i in range(10):
        x_i, y_i = key[i]
        for j in range(i):
            x_j, y_j = key[j]
            dx , dy = map(abs, (x_i-x_j, y_i-y_j))
            ws[j][i] = ws[i][j] = max(dx,dy)+sum((dx,dy))
    dp = [(4,6,0)]
    for n in numbers:
        n = int(n)
        d = {}
        for l,r,w in dp:
            for nl,nr,dw in [(n,r,ws[l][n]), (l,n,ws[r][n])]:
                if nl==nr:
                    continue
                d[(nl,nr)] = min(d.get((nl,nr),10e9),w+dw)
        dp = [(*k,v) for k,v in d.items()]
    ans = 10e9
    for _,_,w in dp:
        ans = min(ans,w)
    return ans