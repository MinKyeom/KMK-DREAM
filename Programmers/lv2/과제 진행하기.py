# 내 풀이
def solution(plans):
    result = []  # 결과
    check = []  # 현재 진행중인 과제
    remain = []  # 남겨둔 과제
    time = 0  # 현재 시간
    plans.sort(key=lambda x: (x[1].split(":")[0], x[1].split(":")[1]))  # 시작 시간에 따른 정렬
    print(plans)

    for x in plans:
        if len(check) < 1:
            check.append(x)
            work_start = check[0][1].split(":")
            work_minute = int(work_start[0]) * 60 + int(work_start[1])
            time = work_minute
            work_check = int(work_start[0]) * 60 + int(work_start[1]) + int(check[0][2])

        else:
            new_work = x[1].split(":")
            new_work_time = int(new_work[0]) * 60 + int(new_work[1])

            if new_work_time < work_check:
                remain_work_time = work_check - new_work_time
                remain.insert(0, [check[0][0], remain_work_time])
                check.pop()
                check.append(x)
                work_start = check[0][1].split(":")
                work_minute = int(work_start[0]) * 60 + int(work_start[1])
                time = work_minute
                work_check = int(work_start[0]) * 60 + int(work_start[1]) + int(check[0][2])

            else:
                result.append(check[0][0])
                check.pop()
                time = work_check

                while True:  # 공백 시간 과제 가능한지 체크
                    if len(remain) == 0:
                        break
                    elif time + remain[0][1] <= new_work_time:
                        time = time + remain[0][1]
                        result.append(remain[0][0])
                        remain.pop(0)
                    elif time + remain[0][1] > new_work_time:
                        remain[0][1] = abs(new_work_time - (time + remain[0][1]))
                        time = new_work_time
                        break

                check.append(x)
                work_start = check[0][1].split(":")
                work_minute = int(work_start[0]) * 60 + int(work_start[1])
                work_check = int(work_start[0]) * 60 + int(work_start[1]) + int(check[0][2])

    result.append(check[0][0])
    final = [v for v, w in remain]
    result = result + final

    return result
# 다른 사람 풀이

def solution(plans):
    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])

    lst = []
    while plans:
        x = plans.pop()
        for i, v in enumerate(lst):
            if v[0] > x[1]:
                lst[i][0] += x[2]
        lst.append([x[1] + x[2], x[0]])
    lst.sort()

    return list(map(lambda x: x[1], lst))
