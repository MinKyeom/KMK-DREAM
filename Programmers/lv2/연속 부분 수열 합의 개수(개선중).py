# 내 풀이
def solution(elements):
    a = 0
    check = []

    while True:
        for x in range(a + 1, len(elements) + 1):
            k = sum(elements[a:x])
            check.append(k)
            print(a, x)

        if a == len(elements) + 1:
            return len((check))


# 다른 사람 풀이
