# 내 풀이
def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))

    check = []

    for k in range(row_begin - 1, row_end):
        count = 0
        for t in range(len(data[k])):
            count += data[k][t] % (k + 1)
        check.append(count)

    for x in range(len(check)):
        if x == 0:
            result = check[x]
        else:
            result = result ^ check[x]

    return result

# 다른 사람 풀이
from functools import reduce

def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x : (x[col-1], -x[0]))
    return reduce(lambda x, y: x ^ y,
                  [sum(map(lambda x: x%(i+1), data[i])) for i in range(row_begin-1, row_end)])