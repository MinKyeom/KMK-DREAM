# 풀이 1

#문제를 정확히 이해하지 않고 풀었기에 틀렸음!!

def solution(dots):
    from itertools import permutations
    for a, b, c, d in list(permutations(dots, 4)):
        if (a[1] - b[1]) / (a[0] - b[0]) == (c[1] - d[1]) / (c[0] - d[0]):
            return 1
        else:
            continue

    return 0


# 다른 사람 풀이
def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]=dots
    answer1 = ((y1-y2)*(x3-x4) == (y3-y4)*(x1-x2))
    answer2 = ((y1-y3)*(x2-x4) == (y2-y4)*(x1-x3))
    answer3 = ((y1-y4)*(x2-x3) == (y2-y3)*(x1-x4))
    return 1 if answer1 or answer2 or answer3 else 0