# 내 풀이
def solution(files):
    f = files
    from collections import deque

    check = []

    for i in f:
        all_new = []  # head, middle, tail 전부 들어감

        # 세 부분 나누기

        head = []
        middle = []
        tail = []

        i = deque(list(i))
        part = "head"

        while i:
            k = i.popleft()

            if k.isdigit() == False and part == "head":
                head.append(k)

            elif k.isdigit() == True and part == "head":
                all_new.append(list(head))
                middle = []
                middle.append(k)
                part = "middle"

            elif k.isdigit() == True and part == "middle":
                middle.append(k)

            elif k.isdigit() == False and part == "middle":
                tail.append(k)
                tail += list(i)
                all_new.append(list(middle))
                all_new.append(list(tail))
                break

        if len(tail) == 0:
            all_new.append(list(middle))
            all_new.append([])

        check.append(all_new)

    check.sort(key=lambda x: (("".join(x[0]).upper()), int("".join(x[1]))))

    final = []

    for a, b, c in check:
        A = "".join(a)

        B = "".join(list(map(str, b)))

        C = "".join(list(map(str, c)))

        final.append(A + B + C)
    return final

# 다른 사람 풀이
import re

def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b