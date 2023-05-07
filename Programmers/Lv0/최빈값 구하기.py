# 내 풀이
def solution(array):
    x = set(array)
    num = []
    for a in x:
        if not len(num) == 0 and array.count(a) >= array.count(num[0]):
            if array.count(a) > array.count(num[0]):
                num = []
                num.append(a)
            elif array.count(a) == array.count(num[0]):
                num.append(a)
        elif len(num) == 0:
            num.append(a)
        else:
            continue

    if len(num) == 1:
        return num[0]
    else:
        return -1

# 다른 사람 풀이
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1