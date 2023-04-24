#풀이


def solution(lines):
    answer = 0
    result = 0
    list_num = []
    list_num_2 = []
    for a, b in lines:
        for x in range(a, b + 1):
            list_num.append(x)
    for c in range(min(list_num), max(list_num) + 1):
        if list_num.count(c) >= 2:
            list_num_2.append(c)
    for d in list_num_2:
        if d < max(list_num_2) and d + 1 in list_num_2:
            result += 1
        else:
            continue

    return result


def solution(lines):
    result = 0
    num = []
    for a, b in lines:
        num.append(range(a, b + 1))
    a = set(num[0])
    b = set(num[1])
    c = set(num[2])
    x = a & b
    print("x", x)
    if not len(x) == 0:
        result += len(x) - 1
    print("1", result)
    y = (b & c) - (a & b & c)
    print("y", y)
    if not len(y) == 0:
        result += len(y) - 1
    print("2", result)
    z = (a & c) - (a & b & c)
    print("z", z)
    if not len(z) == 0:
        result += len(z) - 1
    print("3", result)

    return result