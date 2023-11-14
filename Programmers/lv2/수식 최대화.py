# 내 풀이(개선 중)
def solution(expression):
    from itertools import permutations
    num = []
    ex = []
    check = ["*", "-", "+"]
    k = list(expression)

    for a in range(len(k)):
        if k[a] in check:
            ex.append(k[a])
            k[a] = " "

    l = "".join(k)
    l = l.split(" ")

    # t_num=list(permutations(l,len(l)))
    # t_ex=list(permutations(ex,len(ex)))

    ex_ = set(ex)
    ex_ = list(ex_)
    ex__ = list(permutations(ex_, len(ex_)))  # 연산기호 우선순위

    result = 0

    while ex__:
        v = ex__.pop()
        x = expression

        for a in range(len(v)):
            pass

        break

        break

        if abs(int(start)) > result:
            result = abs(int(start))

    return result