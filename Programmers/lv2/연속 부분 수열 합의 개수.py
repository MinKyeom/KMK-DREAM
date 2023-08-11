# 내 풀이
def solution(elements):
    new_elements = elements + elements

    a = 0
    b = 0

    check = []

    while True:
        for x in range(a + 1, a + len(elements) + 1):
            k = sum(new_elements[a:x])
            check.append(k)

        if a == len(new_elements) - 1:
            return len(set(check))

        a += 1


# 다른 사람 풀이
def solution(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j%ll]
            res.add(ssum)
    return len(res)