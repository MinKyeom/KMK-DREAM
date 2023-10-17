# 내 풀이(갱신 중)
def solution(word):
    from itertools import permutations
    eng = list("AEIOU")
    alpha = []

    for k in range(1, 6):
        t = list(permutations(eng, k))
        alpha += t

    final = []

    for c in alpha:
        c = list(c)
        final.append(c)

    result = []

    for d in final:
        str = ""
        for e in d:
            str += e

        result.append(str)

    result.sort()

    print(result)
    answer = 0
    return answer