"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/17678
"""

# 풀이 과정
"""
셔틀 운행 횟수 n 
셔틀 운행 간격 t 
한 셔틀에 탈 수 있는 최대 크루 수 m 
크루가 대기열에 도착하는 시각을 모은 배열 timetable
"""
from collections import deque


def change_time(x):
    H = x // 60
    M = x % 60

    if len(str(H)) == 1:
        H = "0" + str(H)
    else:
        H = str(H)
    if len(str(M)) == 1:
        M = "0" + str(M)
    else:
        M = str(M)
    return H + ":" + M


def change_hour(k):
    x = k.split(":")
    hour = int(x[0]) * 60 + int(x[1])
    return hour


def solution(n, t, m, timetable):
    bus_table = []

    gap = 0
    bus = 9 * 60

    for b in range(n):
        bus_table.append(bus + gap)
        gap += t

    person = []

    for t in timetable:
        p = change_hour(t)
        person.append(p)

    while person:
        p = person.pop()
        if p > bus_table[-1]:
            continue
        else:
            person.append(p)
            break

    if len(person) == 0:
        return change_time(bus_table[-1])

    person.sort()
    person = deque(person)

    # 최종시간을 알아보는 기준 지표
    now = 0
    # 최종탑승자 시간
    last_person = -1

    for b in bus_table:
        # 한 버스당 타는 인원
        count = 0
        while person:
            cru = person.popleft()
            if cru <= b and count < m:
                count += 1
                last_person = cru
            else:
                person.appendleft(cru)
                break
        now = b
        if len(person) == 0 and count < m:
            return change_time(bus_table[-1])

    return change_time(last_person - 1)

# 다른 사람 풀이
def solution(n,t,m,timetable):
    timetable=[int(i[:2])*60+int(i[3:]) for i in timetable]
    timetable.sort()
    bustable=[9*60+t*i for i in range(n)]
    for i in bustable:
        passenger=[p for p in timetable if p<=i]
        if i==bustable[-1]:
            if len(passenger)>=m:
                answer=passenger[m-1]-1
            elif len(passenger)<m:
                answer=i
            else:
                answer=passenger[-1]
        elif len(passenger)<m:
            timetable=timetable[len(passenger):]
        elif len(passenger)>=m:
            timetable=timetable[m:]
    answer= str(divmod(answer,60)[0]).rjust(2,'0')+':'+str(divmod(answer,60)[1]).rjust(2,'0')
    return answer
