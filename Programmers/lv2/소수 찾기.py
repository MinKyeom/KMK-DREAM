# 내 풀이
def solution(numbers):
    from itertools import permutations
    result = 0

    final = []

    k = list(numbers)

    check = []

    for a in range(1, len(numbers) + 1):
        t = list(permutations(k, a))
        check += t

    num = []  # 0을 앞자리에 둔 중복 숫자 확인

    for b in check:
        n = int("".join(b))

        if n not in num and n != 1:
            num.append(n)
        else:
            continue

        count = 0

        for c in range(1, int(n ** 0.5) + 1):
            if n % c == 0:
                count += 1
            if count > 1:
                break

        if count == 1:
            final.append(n)
            result += 1

    return result

# 다른 사람 풀이
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)