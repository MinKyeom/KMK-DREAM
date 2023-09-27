# 내 풀이
def solution(fees, records):
    # records:시각 차량 번호 내역
    # fees:주차 요금

    result = []  # 차량 번호가 작은거부터 요금 정산

    from collections import deque

    car_in = []  # 입차
    car_out = []  # 출차

    for a in records:
        k = a.split(" ")
        b = k[0].split(":")
        c = int(b[0]) * 60 + int(b[1])

        if k[2] == "IN":
            car_in.append([int(k[1]), int(c)])

        elif k[2] == "OUT":
            car_out.append([int(k[1]), int(c)])

    car_in.sort(key=lambda x: (x[0], x[1]))
    car_out.sort(key=lambda x: (x[0], x[1]))

    car_in = deque(car_in)

    print(car_in)

    while car_in:
        d, e = car_in.popleft()

        if len(car_out) > 0:
            if car_out[0][0] == d:
                t = e - car_out[0][1]

                if t <= fees[0]:
                    result.append(fees[1])
                    del car_out[0]
                    print(car_out)

    return result

# 다른 사람 풀이