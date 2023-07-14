# 내 풀이
def solution(n, lost, reserve):
    result = 0
    check = []
    for k in range(1, n + 1):
        if not k in lost:
            result += 1
            check.append(k)
            continue
        elif k in lost and k in reserve:
            check.append(k)
            continue
        else:
            if k - 1 in reserve:
                if k - 1 in reserve and not k - 1 in lost and not k in check:
                    reserve.remove(k - 1)
                    check.append(k)

            if k + 1 in reserve:
                if k + 1 in reserve and not k + 1 in lost and not k in check:
                    reserve.remove(k + 1)
                    check.append(k)

    return len(check)

# 다른 사람 풀이
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
