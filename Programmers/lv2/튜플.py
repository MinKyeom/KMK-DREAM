# 내 풀이(개선 중)
def solution(s):
    from collections import deque
    s = s[1:len(s) - 1]
    c = s.replace(",", " ")
    d = c.replace("{", "")
    t = d.split("}")
    print(t)
    for a in t:
        print(a)

    return 1

    s = deque(list(s))
    result = []
    result_check = []

    while s:
        k = s.popleft()

        if k == "{":
            check = []
            while True:
                a = s.popleft()

                if a == "}":
                    result_check.append(check)
                    break
                elif a != "," and a != "}" and int(a) in t:
                    check.append(int(a))

    result_check.sort(key=lambda x: len(x))

    for a in result_check:
        for b in a:
            if not int(b) in result:
                result.append(int(b))

    return result