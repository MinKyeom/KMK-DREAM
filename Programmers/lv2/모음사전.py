# 내 풀이
def solution(word):
    from itertools import product
    eng = list("AEIOU")
    alpha = []

    for k in range(1, 6):
        t = list(product(eng, repeat=k))
        alpha += t

    final = []

    for c in alpha:
        c = list(c)
        final.append(c)

    result = []

    for d in final:
        d = "".join(d)
        result.append(d)

    result.sort()

    finish = result.index(word)

    return finish + 1

# 다른 사람 풀이
from itertools import product

solution = lambda word: sorted(["".join(c) for i in range(5) for c in product("AEIOU", repeat=i+1)]).index(word) + 1