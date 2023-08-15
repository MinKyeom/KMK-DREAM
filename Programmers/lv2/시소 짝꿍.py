# 내 풀이(시간 초과 발생)
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


# 내 풀이

def solution(weights):
    from itertools import combinations

    result = 0

    k = set(weights)

    l = list(combinations(k, 2))

    c = []

    for a, b in l:
        if a / b == 2 or a / b == 1.5 or a / b == 4 / 3 or a / b == 1 / 2 or a / b == 2 / 3 or a / b == 3 / 4:
            c.append([a, b])

    for d, e in c:
        f = weights.count(d)
        g = weights.count(e)

        result += f * g

    for h in k:
        i = weights.count(h)
        if i > 1:
            result += (i * (i - 1)) / 2

    return result

# 다른 사람 풀이
from collections import defaultdict

def solution(weights):
    answer = 0
    dict1 = defaultdict(int)
    w_dict = defaultdict(int)

    for i in weights:
        tmp = dict1[i*2] + dict1[i*3] + dict1[i*4]
        if tmp != 0 and i in w_dict:
            tmp -= 2 * w_dict[i]
        for j in range(2,5):
            dict1[i*j] += 1
        w_dict[i] += 1
        answer += tmp
    return answer


solution([100,180,360,100,270])


