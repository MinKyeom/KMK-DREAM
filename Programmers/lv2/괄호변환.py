# 내 풀이(개선 중)
from collections import deque


# u 변환
def change_u(sub):
    sub = deque(sub)
    sub.popleft()
    sub.pop()

    for a in range(len(sub)):
        if sub[a] == "(":
            sub[a] = ")"
        else:
            sub[a] = "("

    sub.appendleft("(")
    sub.append(")")

    return sub


# sub가 v인지 check
def check_v(sub, result):
    sub = deque(sub)
    new_sub = []
    check = []
    count_1 = 0
    count_2 = 0

    while sub:
        k = sub.popleft()
        new_sub.append(k)

        if k == "(":
            count_1 += 1
        else:
            count_2 += 1

        if len(check) == 0:
            check.append(k)
        else:

            if k == ")" and check[-1] == "(":
                check.pop()
            else:
                check.append(k)

            if count_1 == count_2:
                if len(check) == 0:
                    t = "".join(new_sub)
                    result = result + t
                    check = []
                    new_sub = []
                    count_1 = 0
                    count_2 = 0
                else:
                    new = change_u(new_sub)
                    result = check_v(new, result)
                    check = []
                    new_sub = []
                    count_1 = 0
                    count_2 = 0

    return result


# 전체
def solution(p):
    p = deque(list(p))

    result = ""

    check = []
    sub = []

    count_1 = 0  # (

    count_2 = 0  # )

    while p:
        k = p.popleft()
        sub.append(k)

        if k == "(":
            count_1 += 1
        else:
            count_2 += 1

        if len(check) == 0:
            check.append(k)
        else:
            if check[-1] == "(" and k == ")":
                check.pop()
            else:
                check.append(k)

            if count_1 == count_2:
                if len(check) == 0:
                    t = "".join(sub)
                    result = result + t

                    sub = []
                    check = []

                    count_1 = 0
                    count_2 = 0

                else:
                    sub = change_u(sub)

                    result = check_v(sub, result)

                    sub = []
                    check = []

                    count_1 = 0
                    count_2 = 0

                print(result)
    return result