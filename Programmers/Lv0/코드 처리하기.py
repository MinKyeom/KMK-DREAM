# 내 풀이
def solution(code):
    mode = 0
    result = []
    if len(code) == 0:
        return "EMPTY"

    for x in range(len(code)):
        if code[x] == "1":
            if mode == 0:
                mode = 1
                continue
            elif mode == 1:
                mode = 0
                continue

        else:
            if mode == 0 and x % 2 == 0:
                result.append(code[x])

            elif mode == 1 and x % 2 == 1:
                result.append(code[x])

            else:
                continue

    if len(result) == 0:
        return "EMPTY"

    return "".join(result)
# 다른 사람 풀이

def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"