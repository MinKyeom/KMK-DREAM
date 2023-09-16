# 내 풀이(개선 중)
def solution(order):
    from collections import deque
    order = deque(order)
    sub = deque([])
    belt = deque([t for t in range(1, len(order) + 1)])
    result = 0

    k = order.popleft()

    while belt:
        x = belt.popleft()
        if x == k:
            result += 1
            break
        else:
            sub.append(x)

    while order:
        k = order.popleft()

        if len(belt) > 0:
            if len(belt) >= 2:
                if k == belt[0] or k == belt[1]:
                    if k == belt[0]:
                        belt.popleft()
                        result += 1
                        continue
                    elif k == belt[1]:
                        c = belt.popleft()
                        sub.append(c)
                        belt.popleft()
                        result += 1
                        continue
                else:
                    if k == belt[0]:
                        belt.popleft()
                        result += 1
                        continue

        if len(sub) > 0:
            if k == sub[-1]:
                result += 1
                sub.pop()
                continue
            else:
                return result
        else:
            return result

    return result

# 다른 사람 풀이
# 1 ~ n 까지의 택배를 재 배열
# 기존 컨베이어 : queue -> 작은 수부터 빼낼 수 있음
# 보조 컨베이어 : Stack -> 큰 수부터 빼낼 수 있음
# 몇 개의 상자를 실을 수 있는지
# order의 상자가 나올 때 까지 pop

from collections import deque


def solution(order):
    order = deque(order)
    # 메인 컨베이어 작업 목록
    main_line = deque(range(order[0], len(order) + 1))
    # 서브 컨베이어 작업 목록
    sub_line = list(range(1, order[0]))
    # 개수 확인
    cnt = 0
    # 꺼낼 main이 있는지 확인
    flag = True
    while flag and order:
        order_now = order.popleft()
        while True:
            # 메인에 있는 경우
            if main_line and main_line[0] == order_now:
                main_line.popleft()
                cnt += 1
                break
            # 서브에 있는 경우
            if sub_line and sub_line[-1] == order_now:
                sub_line.pop()
                cnt += 1
                break
            # 둘 다에 없는 경우
            if not main_line:
                flag = False
                break
            else:
                sub_line.append(main_line.popleft())
    return cnt