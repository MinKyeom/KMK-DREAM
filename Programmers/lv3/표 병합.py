"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/150366
"""

# 풀이 과정
# 이후 (r1, c1) 와 (r2, c2) 중 어느 위치를 선택하여도 병합된 셀로 접근합니다. 중요포인트
#  병합된 셀의 경우 따로 체크 리스트를 만든 후 병합과 삭제 시 따로 함수를 만들어서 구현! (시간과 효율성에 관하여 생각도 해보기!) 03 07 20시 추가!
# 업데이트 된 셀 또한 통합이 되어있을 경우 통째로 바뀌어야 한다!
from collections import deque


def merge(m, s, fir, sec, check):
    check = deque(check)
    flag = False
    n = len(check)
    count = 0
    r1 = fir[0]
    c1 = fir[1]
    r2 = sec[0]
    c2 = sec[1]
    new = [[r1, c1], [r2, c2]]
    while count < n:
        i = check.popleft()
        if [r1, c1] in i or [r2, c2] in i:
            for v, w in i:
                if not [v, w] in new:
                    new.append([v, w])
            flag = True
        else:
            check.append(i)

        count += 1

    if flag == False:
        check.append([[r1, c1], [r2, c2]])
        m[r1][c1] = s
        m[r2][c2] = s
    else:
        for v, w in new:
            m[v][w] = s
        check.append(new)

    return m, list(check)


def unmerge(m, check, s, fir):
    r = fir[0]
    c = fir[1]
    check = deque(check)
    n = len(check)
    count = 0

    while count < n:
        i = check.popleft()

        if [r, c] in i:
            for v, w in i:
                m[v][w] = "EMPTY"

            m[r][c] = s
            break

        check.append(i)

        count += 1

    m[r][c] = s

    return m, list(check)


def solution(commands):
    m = [["EMPTY"] * 50 for _ in range(50)]  # 표

    k = commands  # 축약

    check = []  # sum cell
    result = []

    for i in k:
        # update
        if "UPDATE" in i:
            if i.count(" ") == 3:
                t = i.split(" ")
                r = int(t[1]) - 1
                c = int(t[2]) - 1
                value = t[3]

                for v in check:
                    if [r, c] in v:
                        # print(check,value)
                        for a, b in v:
                            m[a][b] = value

                        break
                else:
                    m[r][c] = value

            elif i.count(" ") == 2:
                t = i.split(" ")
                value1 = t[1]
                value2 = t[2]
                # 모든 셀 변환
                for v1 in range(50):
                    for v2 in range(50):
                        if m[v1][v2] == value1:
                            m[v1][v2] = value2

        # merge
        elif "MERGE" in i and not "UN" in i:
            t = i.split(" ")
            # index를 위해 -1
            r1 = int(t[1]) - 1
            c1 = int(t[2]) - 1
            r2 = int(t[3]) - 1
            c2 = int(t[4]) - 1

            fir = [r1, c1]
            sec = [r2, c2]

            if m[r1][c1] == "EMPTY":
                s = m[r2][c2]
            else:
                s = m[r1][c1]
            # print(check,"before",s)
            m, check = merge(m, s, fir, sec, check)
            # print(check,"after",s)

        # unmerge
        elif "UNMERGE" in i:
            t = i.split(" ")
            r = int(t[1]) - 1
            c = int(t[2]) - 1
            s = m[r][c]
            # print(s,[r,c])
            fir = [r, c]
            m, check = unmerge(m, check, s, fir)

        elif "PRINT" in i:
            t = i.split(" ")
            r = int(t[1]) - 1
            c = int(t[2]) - 1
            result.append(m[r][c])

        # print(check,"all",t[0])

    return result

# 내 풀이(개선 중)
# 이후 (r1, c1) 와 (r2, c2) 중 어느 위치를 선택하여도 병합된 셀로 접근합니다. 중요포인트
#  병합된 셀의 경우 따로 체크 리스트를 만든 후 병합과 삭제 시 따로 함수를 만들어서 구현! (시간과 효율성에 관하여 생각도 해보기!) 03 07 20시 추가!
def solution(commands):
    m = [["EMPTY"] * 50 for _ in range(50)]  # 표

    k = commands  # 축약

    check = []  # sum cell
    result = []

    for i in k:
        # update
        if "UPDATE" in i:
            if i.count(" ") == 3:
                t = i.split(" ")
                r = int(t[1]) - 1
                c = int(t[2]) - 1
                value = t[3]
                m[r][c] = value

            elif i.count(" ") == 2:
                t = i.split(" ")
                value1 = t[1]
                value2 = t[2]

                # 모든 셀 변환
                for v1 in range(50):
                    for v2 in range(50):
                        if m[v1][v2] == value1:
                            m[v1][v2] = value2

        # merge
        elif "MERGE" in i and not "UN" in i:
            t = i.split(" ")
            # index를 위해 -1
            r1 = int(t[1]) - 1
            c1 = int(t[2]) - 1
            r2 = int(t[3]) - 1
            c2 = int(t[4]) - 1

            if [r1, c1] != [r2, c2]:
                if m[r1][c1] == "EMPTY":
                    m[r1][c1] = m[r2][c2]
                else:
                    m[r2][c2] = m[r1][c1]

        # unmerge
        elif "UNMERGE" in i:
            t = i.split(" ")
            r = int(t[1]) - 1
            c = int(t[2]) - 1

            m[r][c] = "EMPTY"

        elif "PRINT" in i:
            t = i.split(" ")
            r = int(t[1]) - 1
            c = int(t[2]) - 1
            result.append([r, c])
    final = []
    for x, y in result:
        final.append(m[x][y])
    print(result)
    return final
# 내 풀이(개선 중)
# 이후 (r1, c1) 와 (r2, c2) 중 어느 위치를 선택하여도 병합된 셀로 접근합니다. 중요포인트

def solution(commands):
    m = [["EMPTY"] * 50 for _ in range(50)]  # 표

    k = commands  # 축약

    result = []

    for i in k:
        # update
        if "UPDATE" in i:
            if i.count(" ") == 3:
                t = i.split(" ")
                r = int(t[1]) - 1
                c = int(t[2]) - 1
                value = t[3]
                m[r][c] = value

            elif i.count(" ") == 2:
                t = i.split(" ")
                value1 = t[1]
                value2 = t[2]

                # 모든 셀 변환
                for v1 in range(50):
                    for v2 in range(50):
                        if m[v1][v2] == value1:
                            m[v1][v2] = value2
        # merge
        elif "MERGE" in i:
            break
            t = i.split(" ")
            # index를 위해 -1
            r1 = int(t[1]) - 1
            c1 = int(t[2]) - 1
            r2 = int(t[3]) - 1
            c2 = int(t[4]) - 1

            if m[r1][c1] != m[r2][c2]:
                if m[r1][c1] == "EMPTY":
                    m[r1][c1] = m[r2][c2]
                else:
                    m[r2][c2] = m[r1][c1]

        # unmerge
        elif "UNMERGE" in i:
            t = i.split(" ")
            r = int(t[1]) - 1
            c = int(t[2]) - 1

            m[r][c] = "EMPTY"

        elif "PRINT" in i:
            t = i.split(" ")
            r = int(t[1]) - 1
            c = int(t[2]) - 1
            result.append(m[r][c])

    return result

# 다른 사람 풀이
values = ['' for _ in range(50 * 50)]
parent = [i for i in range(50 * 50)]


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x1, x2):
    root1 = find(x1)
    root2 = find(x2)

    if not values[root1] and values[root2]:
        parent[root1] = root2
        values[root1] = values[root2]
    else:
        parent[root2] = root1
        values[root2] = values[root1]


def solution(commands):
    answer = []

    for command in commands:
        command = list(command.split())
        if command[0] == 'UPDATE':
            if len(command) == 4:   # r, c의 root value만을 바꿔준다.
                r, c, value = command[1:]
                r, c = int(r) - 1, int(c) - 1
                x = r * 50 + c
                rootx = find(x)
                values[rootx] = value

            else: # value1을 모두 찾아, value2로 바꿔준다.
                value1, value2 = command[1:]
                for i in range(50 * 50):
                    if values[i] == value1:
                        values[i] = value2

        elif command[0] == 'MERGE':
            r1, c1, r2, c2 = map(lambda x: int(x) - 1, command[1:])

            x1 = r1 * 50 + c1
            x2 = r2 * 50 + c2
            if parent[x1] != parent[x2]:
                union(x1, x2)

        elif command[0] == 'UNMERGE':
            r, c = map(lambda x: int(x) - 1, command[1:])
            x = r * 50 + c
            rootx = find(x)
            valuex = values[rootx]

            nodes = []
            for i in range(50 * 50):
                if find(i) == rootx:
                    nodes.append(i)

            for node in nodes:
                values[node] = ''
                parent[node] = node

            values[x] = valuex

        elif command[0] == 'PRINT':
            r, c = map(lambda x: int(x) - 1, command[1:])
            x = r * 50 + c
            rootx = find(x)

            if not values[rootx]:
                answer.append('EMPTY')
            else:
                answer.append(values[rootx])

    return answer

# 다른 사람풀이
TABLE_SIZE = 50;


def update(value1, value2, table):
    for r in range(1, TABLE_SIZE + 1):
        for c in range(1, TABLE_SIZE + 1):
            if table[r][c] == value1:
                table[r][c] = value2


def merge(r1, c1, r2, c2, table, group):
    group[r2][c2] = group[r1][c1]
    table[r2][c2] = table[r1][c1]


def unmerge(r, c, table, group):
    table[r][c] = ""
    group[r][c] = 51 * r + c


def solution(commands):
    table = [[""] * (TABLE_SIZE + 1) for _ in range(TABLE_SIZE + 1)]
    group = [[0] * (TABLE_SIZE + 1) for _ in range(TABLE_SIZE + 1)]
    group_dict = dict()

    result = []

    for r in range(1, TABLE_SIZE + 1):
        for c in range(1, TABLE_SIZE + 1):
            group[r][c] = 51 * r + c
            group_dict[group[r][c]] = [[r, c]]

    for command in commands:
        order, *rest = command.split(" ")

        if order == "UPDATE":
            if len(rest) == 2:   # UPDATE value1 value2
                value1, value2 = rest
                update(value1, value2, table)
            else:                # UPDATE r c value
                r, c, value = rest
                r, c = int(r), int(c)

                for nr, nc in group_dict[group[r][c]]:
                    table[nr][nc] = value
        elif order == "MERGE":   # MERGE r1 c1 r2 c2
            r1, c1, r2, c2 = map(int, rest)

            if group[r1][c1] == group[r2][c2]:
                continue

            if not table[r1][c1] and table[r2][c2]:
                r1, r2 = r2, r1
                c1, c2 = c2, c1

            merged_group = group[r2][c2]

            for nr, nc in group_dict[merged_group]:
                merge(r1, c1, nr, nc, table, group)

            group_dict[group[r1][c1]].extend(group_dict[merged_group])
            group_dict[merged_group] = []
        elif order == "UNMERGE": # UNMERGE r c
            r, c = map(int, rest)
            original_group = group[r][c]
            original_value = table[r][c]
            original_group_values = group_dict[original_group]

            for nr, nc in group_dict[original_group]:
                unmerge(nr, nc, table, group)
                group_dict[nr * 51 + nc] = [[nr, nc]]

            table[r][c] = original_value
        elif order == "PRINT":   # PRINT r c
            r, c = map(int, rest)

            if table[r][c]:
                result.append(table[r][c])
            else:
                result.append("EMPTY")

    return result
