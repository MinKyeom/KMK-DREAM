# 내 풀이
def solution(weights):
    from itertools import combinations

    k = list(combinations(weights, 2))

    count = 0

    for a, b in k:
        if min([a, b]) * 2 == max([a, b]):
            count += 1
        elif min([a, b]) * 3 == max([a, b]):
            count += 1
        elif min([a, b]) * 4 == max([a, b]):
            count += 1
        elif min([a, b]) == max([a, b]):
            count += 1
        elif min([a, b]) * 4 == max([a, b]) * 2:
            count += 1
        elif min([a, b]) * 4 == max([a, b]) * 3:
            count += 1
        elif min(a, b) * 3 == max([a, b]) * 2:
            count += 1
    return count