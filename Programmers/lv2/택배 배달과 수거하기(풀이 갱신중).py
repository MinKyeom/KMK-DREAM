# 내 풀이
def solution(cap, n, deliveries, pickups):
    # 택배 배달 후 빈 택배 상자 수거
    # cap:담을 수 있는 최대 상자 개수
    # 목표:배달+수거 최소 거리 구하기

    dis = 0  # 이동거리
    """
    아이디어 변화 과정

    #최대 개수를 가져가야한다

    #최대 개수를 가져가고 최대 개수를 가져오고(갈 떄 다 비워야 많은 걸 수거 가능)

    # 멀리있는걸 먼저 최대한 없애야한다 그래야 더 멀리 갈 필요가 없다

    # 수거와 배달을 같이 생각! 돌아가면서 가져가니까 따로 생각?

    #배달만 수거만 생각 후 모두 최대로 생각
    """
    check_1 = []
    check_2 = []
    k = cap
    while deliveries:
        print(deliveries, "del")

        if deliveries and deliveries[-1] == 0:
            deliveries.pop()
            continue

        if deliveries[-1] <= cap:
            dis = len(deliveries)
            check_1.append(dis)
            a = deliveries.pop()
            k = k - a
            while deliveries:
                if deliveries[-1] >= k:
                    deliveries[-1] = deliveries[-1] - k
                    break
                else:
                    b = deliveries.pop()
                    k = k - b
        else:
            deliveries[-1] = deliveries[-1] - k
            dis += len(deliveries)
            check_1.append(dis)

        if sum(deliveries) == 0 or len(deliveries) == 0:
            break

        k = cap

    dis = 0

    while pickups:
        print(pickups, "pick")
        if pickups and pickups[-1] == 0:
            pickups.pop()
            continue

        if pickups[-1] <= cap:
            dis = len(pickups)
            check_2.append(dis)
            a = pickups.pop()
            k = k - a
            while pickups:
                if pickups[-1] >= k and k != 0:
                    pickups[-1] = pickups[-1] - k
                    break
                elif pickups[-1] < k and k != 0:
                    b = pickups.pop()
                    k = k - b
        else:
            pickups[-1] = pickups[-1] - k
            dis = len(pickups)
            check_2.append(dis)

        if sum(pickups) == 0 or len(pickups) == 0:
            break

        k = cap

    print(check_1)
    print(check_2)

    return 0
# 갱신 풀이(시간 초과 발생)
def solution(cap, n, deliveries, pickups):
    import math
    import time
    start = time.time()
    math.factorial(100000)
    end = time.time()
    print(f"{end - start:.5f} sec")
    from collections import deque

    # 택배 배달 후 빈 택배 상자 수거
    # cap:담을 수 있는 최대 상자 개수
    # 목표:배달+수거 최소 거리 구하기

    # 이동거리
    """
    아이디어 변화 과정

    #최대 개수를 가져가야한다

    #최대 개수를 가져가고 최대 개수를 가져오고(갈 떄 다 비워야 많은 걸 수거 가능)

    # 멀리있는걸 먼저 최대한 없애야한다 그래야 더 멀리 갈 필요가 없다

    # 수거와 배달을 같이 생각! 돌아가면서 가져가니까 따로 생각?

    #배달만 수거만 생각 후 모두 최대로 생각
    """
    check_1 = []
    check_2 = []

    k = cap
    result = 0
    pic_f = 0
    del_f = 0
    dis_1 = 0
    dis_2 = 0

    while True:
        while True:
            if deliveries and deliveries[-1] == 0:
                deliveries.pop()
            else:
                break

        if deliveries and deliveries[-1] <= cap:
            dis = len(deliveries)
            check_1.append(dis)
            dis_1 = dis
            a = deliveries.pop()
            k = k - a
            while deliveries:
                if deliveries[-1] >= k:
                    deliveries[-1] = deliveries[-1] - k
                    break
                else:
                    b = deliveries.pop()
                    k = k - b
        elif deliveries and deliveries[-1] > cap:
            deliveries[-1] = deliveries[-1] - k
            dis = len(deliveries)
            dis_1 = dis
            check_1.append(dis)

        if sum(deliveries) == 0 or len(deliveries) == 0:
            del_f = 1

        k = cap

        # pickups start
        while True:
            if pickups and pickups[-1] == 0:
                pickups.pop()
            else:
                break

        if pickups and pickups[-1] <= cap:
            dis = len(pickups)
            check_2.append(dis)
            dis_2 = dis
            a = pickups.pop()
            k = k - a
            while pickups:
                if pickups[-1] >= k:
                    pickups[-1] = pickups[-1] - k
                    break
                elif pickups[-1] < k:
                    b = pickups.pop()
                    k = k - b
        elif pickups and pickups[-1] > cap:
            pickups[-1] = pickups[-1] - k
            dis = len(pickups)
            dis_2 = dis
            check_2.append(dis)

        if sum(pickups) == 0 or len(pickups) == 0:
            pic_f = 1

        print(dis_1, dis_2)
        r = max([dis_1, dis_2])
        result += r
        dis_1 = 0
        dis_2 = 0

        if pic_f == 1 and del_f == 1:
            return result * 2

        k = cap

        # ------------ 개선 될 부분-------------#

    result_1, result_2 = deque(check_1), deque(check_2)

    print(result_1, result_2)
    result = 0

    while True:
        if result_1 and result_2:
            r_1 = result_1.popleft()
            r_2 = result_2.popleft()
            if r_1 >= r_2:
                result += r_1 * 2
            else:
                result += r_2 * 2
        elif not result_1 and result_2:
            r_2 = result_2.popleft()
            result += r_2 * 2

        elif not result_2 and result_1:
            r_1 = result_1.popleft()
            result += r_1 * 2
        else:
            return result
# 다른 사람 풀이