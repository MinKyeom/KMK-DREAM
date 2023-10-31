# 내 풀이
def solution(input_string):
    from collections import deque

    k = deque(list(input_string))

    check = []

    result = []

    a = k.popleft()

    check.append(a)

    before = a

    while k:
        t = k.popleft()

        if t == before:
            check.append(t)
            before = t

        elif t != before and t not in check:
            check.append(t)
            before = t

        elif t != before and t in check:
            if t not in result:
                result.append(t)
            before = t

    result.sort()
    result = "".join(result)