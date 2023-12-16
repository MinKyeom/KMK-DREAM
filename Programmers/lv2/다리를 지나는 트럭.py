# 내 풀이(개선 중)
def solution(bridge_length, weight, truck_weights):
    from itertools import combinations
    from collections import deque
    now = 0  # 경과 시간

    b_l = bridge_length  # 다리 위 차량 최대 대수
    w = weight  # 다리 감당 가능 무게
    t_w = truck_weights  # 트럭들 무게
    t_w.sort(reverse=True)  # 높은 순으로 나열
    t_w = deque(t_w)

    check = deque([])  # 현재 차량 확인

    count = 0  # 현재 무게 측정

    finish = []  # 완료 차량 체크

    while t_w:
        k = t_w.popleft()

        if len(t_w) > 0:
            start = now

            if len(check) == 0:
                check.append([k, start])
                count += k
                now += 1
                continue
            else:
                if count + k <= w and len(check) + 1 <= b_l:
                    check.append([k, start])
                    count += k

                    while check:  # 도착 차량 빼기
                        i, j = check.popleft()
                        if now - j == b_l:
                            finish.append([i, j])
                            continue
                        else:
                            check.appendleft([i, j])
                            break
                    now += 1
                    continue

                else:
                    t_w.appendleft(k)

                if count + t_w[-1] <= w and len(check) + 1 <= b_l:
                    k_s = t_w.pop()
                    count += k_s
                    check.append([k_s, start])

                    while check:  # 도착 차량 빼기
                        i, j = check.popleft()

                        if now - j == b_l:
                            finish.append([i, j])
                            continue
                        else:
                            check.appendleft([i, j])
                            break
                    now += 1
                    continue

                else:
                    while check:  # 도착 차량 빼기
                        i, j = check.popleft()

                        if now - j == b_l:
                            finish.append([i, j])
                            continue
                        else:
                            check.appendleft([i, j])
                            break
                    now += 1
                    continue

        else:  # 모든 차량이 다리 위에 이미 존재

            while check:  # 도착 차량 빼기
                i, j = check.popleft()

                if now - j == b_l:
                    finish.append([i, j])
                    now += 1
                    continue
                else:
                    check.appendleft([i, j])
                    now += 1
                    continue
            print(finish)
            return now

    return "check"


# 다른 사람 풀이
