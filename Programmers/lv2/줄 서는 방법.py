# 내 풀이(개선 중)
from itertools import permutations
from collections import deque

eng = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
       "w", "x", "y", "z"]


def solution(n, k):
    check = []

    for _ in range(n):
        check.append(eng[_])

    new = list(permutations(check, n))

    new = deque(list(new[k - 1]))

    result = []

    while new:
        num = eng.index(new.popleft())
        result.append(num + 1)

    return result

# 다른 사람 풀이 