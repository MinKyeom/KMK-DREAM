# 내 풀이 (개선 중)
# 예전에 나왔던 완탐 문제랑 비슷
def solution(info, query):
    # 조건:5가지
    result = [0 for c in range(len(query))]
    person = []
    check = []

    # 효율성 감안 새로운 풀이
    for a in info:
        k = a.split(" ")
        person.append(k)

    for b in range(len(query)):
        t = query[b].split(" ")
        v = [t[0], t[2], t[4], t[6], t[7]]
        check.append(v)

    print(check[0])

    for c in person:
        for d in range(len(check)):
            flag = False

            if check[d][0] == "-" or check[d][0] == c[0]:
                pass
            else:
                flag = True
                continue

            if check[d][1] == "-" or check[d][1] == c[1]:
                pass
            else:
                flag = True
                continue

            if check[d][2] == "-" or check[d][2] == c[2]:
                pass
            else:
                flag = True
                continue

            if check[d][3] == "-" or check[d][3] == c[3]:
                pass
            else:
                flag = True
                continue

            if int(check[d][4]) <= int(c[4]):
                pass
            else:
                flag = True
                continue

            result[d] += 1
    # 개선 중 풀이 3
    for b in range(len(query)):
        t = query[b].split(" ")
        v = [t[0], t[2], t[4], t[6], t[7]]
        check.append(v)

    for a in info:
        k = a.split(" ")
        # person.append(k)

        for d in range(len(check)):
            flag = False

            if check[d][0] == "-" or check[d][0] == k[0]:
                pass
            else:
                flag = True
                continue

            if check[d][1] == "-" or check[d][1] == k[1]:
                pass
            else:
                flag = True
                continue

            if check[d][2] == "-" or check[d][2] == k[2]:
                pass
            else:
                flag = True
                continue

            if check[d][3] == "-" or check[d][3] == k[3]:
                pass
            else:
                flag = True
                continue

            if int(check[d][4]) <= int(k[4]):
                pass
            else:
                flag = True
                continue

            result[d] += 1

    """
    #정확도 100 효율성 애매 풀이
    for a in info:
        k=a.split(" ")

        for b in range(len(query)):
            t=query[b].split(" ")
            v=[t[0],t[2],t[4],t[6],t[7]]

            flag=False

            for d in range(len(v)):
                if v[d]=="-":
                    continue

                else:
                    if d<4:
                        if k[d]==v[d]:
                            continue
                        else:
                            flag=True
                            break
                    else:
                        if int(k[d])>=int(v[d]):
                            continue
                        else:
                            flag=True
                            break

            if flag==False:
                result[b]+=1
                """

    return result