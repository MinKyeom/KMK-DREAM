# 내 풀이
def solution(keymap, targets):
    result = []
    for x in targets:
        count = 0
        k = list(x)
        for y in range(len(k)):
            sub = []
            check = []
            for z in keymap:
                f = z.find(k[y])
                if f == -1:
                    continue
                sub.append(f + 1)
            if len(sub) == 0:
                result.append(-1)
                check.append(-1)
                break
            else:
                count += min(sub)
        if count != 0 and -1 not in check:
            result.append(count)
        check = []

    return result

# 다른 사람 풀이
def solution(keymap, targets):
    answer = []
    hs = {}
    for k in keymap:
        for i, ch in enumerate(k):
            hs[ch] = min(i + 1, hs[ch]) if ch in hs else i + 1

    for i, t in enumerate(targets):
        ret = 0
        for ch in t:
            if ch not in hs:
                ret = - 1
                break
            ret += hs[ch]
        answer.append(ret)

    return answer
