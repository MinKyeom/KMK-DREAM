# 내 풀이
def solution(msg):
    from collections import deque

    eng = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    result = []

    result = result + eng

    finish = []

    k = deque(list(msg))

    before = ""

    while k:
        a = k.popleft()
        before += a

        if len(k) > 0:
            if not before + k[0] in result:
                t = result.index(before)
                finish.append(t + 1)
                result.append(before + k[0])
                before = ""

            else:
                continue

        else:
            t = result.index(before)
            finish.append(t + 1)

    return finish

# 다른 사람 풀이
def solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {k:v for (k,v) in zip(alphabet, list(range(1,27)))}
    answer = []

    while True:
        if msg in d:
            answer.append(d[msg])
            break
        for i in range(1, len(msg)+1):
            if msg[0:i] not in d:
                answer.append(d[msg[0:i-1]])
                d[msg[0:i]] = len(d)+1
                msg = msg[i-1:]
                break

    return answer