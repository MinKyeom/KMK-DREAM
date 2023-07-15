# 내 풀이
def solution(dartResult):
    score = "SDT*#"
    check = list("SDT*#")
    k = list(dartResult)
    m = dartResult
    for x in check:
        m = m.replace(x, "-")

    n = m.split("-")
    num = []

    for y in n:
        if y.isdigit() == True:
            num.append(y)
        else:
            continue

    option = dartResult
    print(option)
    for z in str(num):
        option = option.replace(z, " ")
    print(option)
    # option=option.replace("0"," ")

    option_result = option.split(" ")
    option = []

    for a in option_result:
        if not a == "":
            option.append(a)
        else:
            continue
    print("op", option)
    result = []

    for v, w in zip(num, option):
        v = int(v)
        if len(w) >= 2:
            u = list(w)
            if u[0] == "S":
                if u[1] == "#":
                    result.append(-v)
                    continue
                else:
                    result.append(v)
            elif u[0] == "D":
                if u[1] == "#":
                    result.append((-1) * (v ** 2))
                    continue
                else:
                    result.append(v ** 2)
            elif u[0] == "T":
                if u[1] == "#":
                    result.append((-1) * (v ** 3))
                    continue
                else:
                    result.append(v ** 3)
            for a in range(len(result)):
                if len(result) <= 2:
                    result[a] = result[a] * 2
                else:
                    if a >= 1:
                        result[a] = result[a] * 2


        elif len(w) == 1:
            if w == "S":
                result.append(v)
            elif w == "D":
                result.append(v ** 2)
            elif w == "T":
                result.append(v ** 3)

    print(result)
    return sum(result)

# 다른 사람 풀이
def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)