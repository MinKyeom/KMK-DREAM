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

import math
def solution(fees, records):
    basic_minute = fees[0]
    basic_fee = fees[1]
    minute = fees[2]
    unit = fees[3]

    car = list(set(map(lambda x: x.split()[1], records)))
    total_fees = {k : 0 for k in car}
    check = {}
    for record in records:
        tmp = record.split(' ')
        if tmp[1] not in check.keys():
            check[tmp[1]]= tmp[0]
        else:
            if tmp[-1] == 'OUT':
                out_time = int(tmp[0].split(':')[0]) * 60 + int(tmp[0].split(':')[1])
                in_time = int(check[tmp[1]].split(':')[0]) * 60 + int(check[tmp[1]].split(':')[1])
                total_fees[tmp[1]] = total_fees[tmp[1]] + out_time - in_time
                del check[tmp[1]]

    if check:
        for i in check.keys():
            out_time = 1439
            in_time = int(check[i].split(':')[0]) * 60 + int(check[i].split(':')[1])
            total_fees[i] = total_fees[i] + out_time - in_time

    result = []
    for i in total_fees.items():
        if i[1] <= basic_minute :
            result.append((i[0], basic_fee))
        else:
            result.append((i[0], basic_fee + (math.ceil((i[1] - basic_minute) / minute) * unit)))

    return list(map(lambda x: x[1], sorted(result)))