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