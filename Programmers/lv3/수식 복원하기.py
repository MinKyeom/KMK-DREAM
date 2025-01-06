"""
출처 프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/340210
"""

# 풀이 과정

# n:바꾸고 싶은 수 #q:나누는 수

def num_change(n, q):
    change = ''

    while n > 0:
        n, mod = divmod(n, q)
        change += str(mod)

    if change == "":
        return "0"
    return str(change[::-1])


def solution(expressions):
    e = expressions

    # 만족여부
    check = [False] * 10  # 0~9진법

    """
    모든 진법으로 각각 값을 확인 후 True 여부가 하나일 경우 결과 도출 그 이상일 경우 ?로 변경
    """

    for num in range(2, 10):
        for ex in e:
            num_list = list(ex)
            flag = False
            for t in num_list:
                if t.isdigit() == True:
                    if int(t) >= num:
                        flag = True
                        break
            if flag == True:
                break

            if "X" in ex:
                continue

            else:
                k = ex.split("=")
                q_list = k[0].split(" ")
                a = str(int(k[1]))

                q = ""

                for n in q_list:
                    if n.isdigit() == True:
                        if max(list(map(int, list(n)))) >= num:
                            break
                        else:
                            q += str(int(n, num))

                    else:
                        q += n
                else:
                    if max(list(map(int, list(a)))) >= num:
                        break
                    else:

                        if eval(q) == int(a, num):
                            continue
                        else:
                            break

                break
        else:
            check[num] = True

    result = []

    if check.count(True) != 1:
        for i in e:
            if "X" in i:
                num_set = set([])

                for c in range(2, 10):
                    if check[c] == True:
                        k = i.split("=")
                        new = k[0].split(" ")
                        q = ""

                        for o in new:
                            if o.isdigit() == True:
                                q += str(int(o, c))
                            else:
                                q += o

                        x_q = eval(q)
                        x_num = num_change(x_q, c)
                        num_set.add(x_num)
                if len(num_set) >= 2:
                    new = i.replace("X", "?")
                else:
                    new = i.replace("X", list(num_set)[0])

                result.append(new)
    else:
        num = check.index(True)

        for i in e:
            if "X" in i:
                k = i.split("=")
                new = k[0].split(" ")
                q = ""

                for o in new:
                    if o.isdigit() == True:
                        q += str(int(o, num))
                    else:
                        q += o

                x_q = eval(q)
                x_num = num_change(x_q, num)
                new = i.replace("X", x_num)
                result.append(new)

    return result