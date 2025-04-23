"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/131129
"""
# 풀이 과정
# 점수를 깎아서 0점으로 만듬 단, 남은 점수보다 큰 점수로 득점하면 버스트 후 실격

# 조건:
# 싱글: 해당 점수 더블:해당 점수 2배 트리플: 해당 점수 3배
# 불, 아우터 불: 50점

# 승리 조건: 더 빨리 0점 만든 선수(같은 라운드의 경우 그 중 싱글 또는 불을 더 많이 던진 선수)

# 빨리 0점을 만들면서 싱글 또는 불을 최대한 많이 던지는 방법

# 목표:[다트 던진 횟수,싱글 횟수+불 횟수]

# 생각방향: 무조건 1번에 끝나지 않는 경우 불과 싱글과 함께된 조합으로 동일한 횟수로 해결 가능할 경우 그 경우의 수 조합 생각
# 불과 싱글인 수로 뺀 것 그렇지 않은 경우 두 가지 밖에 없다
# 기본 전제 생각 조건: 가장 빨리 끝나는 라운드에서 싱글과 불이 제일 많아야한다
# dfs로 생각 후 접근 방향 생각! > 시간초과
# 같은 수들로 끊임없이 작게 만들어 원하는 값을 얻는 방식 > dp 접근
# 다트의 수가 차이나는 순간에 대하여 고찰 후 문제를 접근 > 시간 단축 및 정답!


import heapq
from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

result = []


def dfs(count, sb, num, s, d):
    global result

    for i in range(len(s) - 1, -1, -1):
        if num - s[i] >= 0:
            if s[i] in d and num - s[i] == 0:
                result.append([count + 1, sb + 1])

            elif not s[i] in d and num - s[i] == 0:
                result.append([count + 1, sb])

            elif s[i] in d and num - s[i] > 0:
                if len(result) > 0:
                    if count + 1 >= result[0][0]:
                        break
                dfs(count + 1, sb + 1, num - s[i], s, d)
                break
            elif not s[i] in d and num - s[i] > 0:
                if len(result) > 0:
                    if count + 1 >= result[0][0]:
                        break
                dfs(count + 1, sb, num - s[i], s, d)

    return result


def solution(target):
    t = target
    global result

    # 다트판 (싱글 가능판)
    d = [k + 1 for k in range(20)]

    # 점수 얻을 수 있는 판
    s = []

    for i in d:
        s.append(i)
        s.append(i * 2)
        s.append(i * 3)

    s.append(50)

    s = list(set(s))

    d.append(50)

    s.sort()

    count, sb, num = 0, 0, t

    if t > 300:
        count += (t - 300) // 60
        num = 300 + (t - 300) % 60

    dfs(count, sb, num, s, d)

    result = sorted(result, key=lambda x: (x[0], -x[1]))

    return result[0]
# 내 풀이(개선 중)
# 점수를 깎아서 0점으로 만듬 단, 남은 점수보다 큰 점수로 득점하면 버스트 후 실격

# 조건:
# 싱글: 해당 점수 더블:해당 점수 2배 트리플: 해당 점수 3배
# 불, 아우터 불: 50점

# 승리 조건: 더 빨리 0점 만든 선수(같은 라운드의 경우 그 중 싱글 또는 불을 더 많이 던진 선수)

# 빨리 0점을 만들면서 싱글 또는 불을 최대한 많이 던지는 방법

# 목표:[다트 던진 횟수,싱글 횟수+불 횟수]

# 생각방향: 무조건 1번에 끝나지 않는 경우 불과 싱글과 함께된 조합으로 동일한 횟수로 해결 가능할 경우 그 경우의 수 조합 생각
# 불과 싱글인 수로 뺀 것 그렇지 않은 경우 두 가지 밖에 없다
# 기본 전제 생각 조건: 가장 빨리 끝나는 라운드에서 싱글과 불이 제일 많아야한다

import heapq
from collections import deque

def solution(target):
    t = target

    # 다트판 (싱글 가능판)
    d = [k + 1 for k in range(20)]

    # 점수 얻을 수 있는 판
    s = []

    for i in d:
        s.append(i)
        s.append(i * 2)
        s.append(i * 3)

    s.append(50)

    s = list(set(s))

    d.append(50)

    s.sort()

    # 최단라운드 구하기
    if t > 60:
        a = t // 60
        b = t % 60
        count = 0
        while True:
            flag = False
            for c in range(len(s) - 1, -1, -1):
                if b >= s[c]:
                    b -= s[c]
                    if b == 0:
                        count += 1
                        flag = True
                    else:
                        count += 1
                    break
            if flag == True:
                r = count + a
                break
    else:
        b = t
        count = 0
        while True:
            flag = False
            for c in range(len(s) - 1, -1, -1):
                if b >= s[c]:
                    b -= s[c]
                    if b == 0:
                        count += 1
                        flag = True
                    else:
                        count += 1
                    break

            if flag == True:
                r = count
                break

    result = []
    q = deque([[0, t]])
    new = []

    result_round = r

    while q:
        sb, num = q.popleft()
        for n in range(len(s) - 1, -1, -1):
            if num >= s[n] and (num - s[n]) - ((60) * (r - 1)) <= 0:
                if s[n] in d:
                    new.append([sb + 1, num - s[n]])
                    if num - s[n] == 0:
                        result.append([result_round, sb + 1])
                    break
                else:
                    new.append([sb, num - s[n]])
                    if num - s[n] == 0:
                        result.append([result_round, sb])


            elif (num - s[n]) - ((60) * (r - 1)) > 0:
                break

        if len(q) == 0:
            r -= 1
            if r == 0:
                break
            else:
                q = list(q)
                new = sorted(new, key=lambda x: (-x[0], x[1]))
                q += new
                new = []
                q = deque(q)

    result = sorted(result, key=lambda x: (x[0], -x[1]))

    return result[0]

# 내 풀이(개선 중)
# 점수를 깎아서 0점으로 만듬 단, 남은 점수보다 큰 점수로 득점하면 버스트 후 실격

# 조건:
# 싱글: 해당 점수 더블:해당 점수 2배 트리플: 해당 점수 3배
# 불, 아우터 불: 50점

# 승리 조건: 더 빨리 0점 만든 선수(같은 라운드의 경우 그 중 싱글 또는 불을 더 많이 던진 선수)

# 빨리 0점을 만들면서 싱글 또는 불을 최대한 많이 던지는 방법

# 목표:[다트 던진 횟수,싱글 횟수+불 횟수]

# 생각방향: 무조건 1번에 끝나지 않는 경우 불과 싱글과 함께된 조합으로 동일한 횟수로 해결 가능할 경우 그 경우의 수 조합 생각
# import heapq
from collections import deque


def solution(target):
    t = target

    # 다트판
    d = [k + 1 for k in range(20)]

    # 점수 얻을 수 있는 판
    s = []

    for i in d:
        s.append(i)
        s.append(i * 2)
        s.append(i * 3)
    s.append(50)

    s = list(set(s))

    d.append(50)

    s.sort()

    q = deque([[0, 0, t]])
    result = []
    new = []  # 라운드 별 새로 추가 할 q

    while q:
        # 라운드,(불 또는 싱글),점수
        r, c, t = q.popleft()

        for i in range(len(s) - 1, -1, -1):
            if t >= s[i]:
                # print(s[i],"s[i]")
                if s[i] in d:
                    new.append([r + (t // s[i]), c + (t // s[i]), (t % s[i])])

                    if (t % s[i]) == 0:
                        result.append([r + (t // s[i]), c + (t // s[i])])


                else:
                    new.append([r + (t // s[i]), c, t % s[i]])

                    if (t % s[i]) == 0:
                        result.append([r + (t // s[i]), c])

        if len(q) == 0:
            q = list(q)
            q += new
            q = deque(q)
            new = []

    result = sorted(result, key=lambda x: (x[0], -x[1]))

    return result[0]

# 다른 사람 풀이
def solution(target):
    dyn = [[100000, 0] for col in range(target+1)]
    dyn[0][0] = 0
    count = 0
    while target > 1000:
        target -= 60
        count += 1

    for i in range(target):
        for j in range(1, 21):

            if i+j <= target and (dyn[i+j][0] > dyn[i][0] + 1 or (dyn[i+j][0] == dyn[i][0]+1 and dyn[i+j][1] < dyn[i][1]+1)):
                dyn[i+j][0] = dyn[i][0] + 1
                dyn[i+j][1] = dyn[i][1] + 1
            if i+j+j <= target and (dyn[i+j+j][0] > dyn[i][0] + 1 or (dyn[i+j+j][0] == dyn[i][0]+1 and dyn[i+j+j][1] < dyn[i][1])):
                dyn[i+j+j][0] = dyn[i][0] + 1
                dyn[i+j+j][1] = dyn[i][1]
            if i+j+j+j <= target and (dyn[i+j+j+j][0] > dyn[i][0] + 1 or (dyn[i+j+j+j][0] == dyn[i][0]+1 and dyn[i+j+j+j][1] < dyn[i][1])):
                dyn[i+j+j+j][0] = dyn[i][0] + 1
                dyn[i+j+j+j][1] = dyn[i][1]
        if i+50 <= target and (dyn[i+50][0] > dyn[i][0]+1 or (dyn[i+50][0] == dyn[i][0]+1 and dyn[i+50][1] < dyn[i][1]+1)):
            dyn[i+50][0] = dyn[i][0] + 1
            dyn[i+50][1] = dyn[i][1] + 1

    dyn[target][0] += count
    answer = dyn[target]
    return answer

# 다른 사람 풀이
def solution(target):
    answer = []

    sin_bull = [x for x in range(1, 21)] + [50]
    dou_tri = sorted([2 * x for x in range(1, 21)] + [3 * x for x in range(1, 21)])

    table = [[int(1e5) for _ in range(target + 1)] for _ in range(2)]
    table[0][0] = table[1][0] = 0
    for trg in range(1, target + 1):
        for i in sin_bull:
            if trg - i >= 0:
                if table[0][trg - i] + 1 < table[0][trg]:
                    table[0][trg] = table[0][trg - i] + 1
                    table[1][trg] = table[1][trg - i] + 1
                elif table[0][trg - i] + 1 == table[0][trg]:
                    table[1][trg] = max(table[1][trg], table[1][trg - i] + 1)
            else:
                break

        for j in dou_tri:
            if trg - j >= 0:
                if table[0][trg - j] + 1 < table[0][trg]:
                    table[0][trg] = table[0][trg - j] + 1
                    table[1][trg] = table[1][trg - j]
                elif table[0][trg - j] + 1 == table[0][trg]:
                    table[1][trg] = max(table[1][trg], table[1][trg - j])
            else:
                break

    return [table[0][-1], table[1][-1]]