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

## 풀이2
def solution(fees, records):
    parking = dict()
    stack = dict()

    for record in records:
        time, car, cmd = record.split()
        hour, minute = time.split(":")
        minutes = int(hour) * 60 + int(minute)  # 시간 -> 분 환산

        if cmd == 'IN':
            parking[car] = minutes
        elif cmd == 'OUT':
            try:
                stack[car] += minutes - parking[car]
            except:
                stack[car] = minutes - parking[car]
            del parking[car]  # 출차 차량 삭제

    # 출차 기록 없는 차 23:59 출차 처리
    for car, minute in parking.items():
        try:
            stack[car] += 23 * 60 + 59 - minute
        except:
            stack[car] = 23 * 60 + 59 - minute

    return [get_fee(time, fees) for car, time in sorted(list(stack.items()), key=lambda x: x[0])]

## 풀이3
# 차량별 주차 요금 계산
# 00:00 ~ 23:59 까지 누적으로 처리 -> 요금 일괄 정산
# 다음날 출차는 고려 X
# 요금 계산 시 '올림' 처리
# 차량 번호가 작은 자동차부터, 차례대로 return!
import math


# 초과 시간 올림 처리

def solution(fees, records):
    # 차량 정보 : {차량 번호 : 시간, 기록 횟수}
    car_info = {}
    # 정산 정보
    fee_list = []
    # 최대 시간 : 23:59에 나갔다고 가정
    max_time = 23 * 60 + 59
    for record in records:
        t, c, _ = record.split(" ")
        t = int(t[:2]) * 60 + int(t[3:])
        # 차량 정보 등록
        if c not in car_info:
            car_info[c] = [0, 0]
        # 시간 등록
        car_info[c][0] += ((max_time - t) * (-1) ** (car_info[c][1]))
        # 기록 횟수 증가
        car_info[c][1] += 1
    # 번호 순으로 정렬
    for _, t in sorted(car_info.items(), key=lambda x: x[0]):
        # 초과 시간
        extra_t = t[0] - fees[0] if t[0] > fees[0] else 0
        # 요금 계산 : 기본 요금 + (초과 시간) * 추가 요금
        fee = fees[1] + math.ceil((extra_t) / fees[2]) * (fees[3])
        fee_list.append(fee)
    return fee_list

# 다른 풀이
import math
def str2int(date):
    return int(date[:2]) * 60 + int(date[3:5])

def solution(fees, records):
    max_time = 24*60 - 1
    time_dic = {}
    io_dic = {}
    for r in records:
        car_num = r[6:11]
        if r[-3:] == ' IN':
            io_dic[car_num] = str2int(r[:5])
        else:
            if time_dic.get(car_num) == None:
                time_dic[car_num] = str2int(r[:5]) - io_dic[car_num]
            else:
                time_dic[car_num] += str2int(r[:5]) - io_dic[car_num]
            del io_dic[car_num]

    for k,v in io_dic.items():
        if time_dic.get(k) == None:
            time_dic[k] = (max_time - v)
        else:
            time_dic[k] += (max_time - v)
    car_list = sorted([k for k in time_dic.keys()])

    answer = [fees[1] + math.ceil((time_dic[car] - fees[0])/fees[2]) * fees[3]\
                if time_dic[car] > fees[0] else fees[1]\
                for car in sorted([k for k in time_dic.keys()])]
    return answer