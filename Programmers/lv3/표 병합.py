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