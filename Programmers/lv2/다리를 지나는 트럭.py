# 내 풀이
"""
def solution(bridge_length, weight, truck_weights):
    from collections import deque

    b_l=bridge_length #최대 수용 가능 차량 수
    w=weight #무게
    t_w=deque(truck_weights)

    now=0  #시간
    count_w=0 #다리 위 차량 무게
    count_c=0 #차량 수

    check=deque([])

    finish=[] #완료 확인

    while t_w:

        k=t_w.popleft()

        if len(check)==0:
            check.append([now,k])
            count_w+=k
            count_c+=1
            now+=1
            continue

        while check:
            t,c=check.popleft()

            if now-t==b_l:
                count_w-=c
                count_c-=1

            else:
                check.appendleft([t,c])
                break

        if count_w+k<=w and count_c+1<=b_l:
            count_w+=k
            count_c+=1
            check.append([now,k])
        else:
            t_w.appendleft(k)

        now+=1


    while check:
        t,c=check.popleft()

        if now-t==b_l:

            if len(check)==0:
                return now+1
            else:
                now+=1
        else:
            check.appendleft([t,c])
            now+=1

    return now
"""


def solution(bridge_length, weight, truck_weights):
    from collections import deque

    b_l = bridge_length  # 최대 수용 가능 차량 수
    w = weight  # 무게
    t_w = deque(truck_weights)

    now = 0  # 시간
    count_w = 0  # 다리 위 차량 무게
    count_c = 0  # 차량 수

    check = deque([])

    while t_w:
        k = t_w.popleft()

        if len(check) == 0:
            check.append([now, k])
            count_w += k
            count_c += 1

        else:
            if now - check[0][0] == b_l:  # 차가 다리를 벗어나는 시점
                i, j = check.popleft()
                count_w -= j
                count_c -= 1

                if count_w + k <= w and count_c + 1 <= b_l:
                    check.append([now, k])
                    count_w += k
                    count_c += 1

                else:
                    t_w.appendleft(k)

                now += 1
                # print(check)
                continue

            if count_w + k <= w and count_c + 1 <= b_l:
                check.append([now, k])
                count_w += k
                count_c += 1

            else:
                t_w.appendleft(k)

        now += 1

        # print(check)

    return check[-1][0] + b_l + 1

# 다른 사람 풀이
import collections

DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count


def main():
    print(solution(2, 10, [7, 4, 5, 6]), 8)
    print(solution(100, 100, [10]), 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


if __name__ == '__main__':
    main()