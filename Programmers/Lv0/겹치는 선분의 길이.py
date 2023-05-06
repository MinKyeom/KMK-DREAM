#내 풀이
#점 개념 선 개념 정확히 생각 후 풀기! 핵심 생각
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
    y = (b & c)  # - (a & b & c)
    print("y", y)
    if not len(y) == 0:
        result += len(y) - 1
    print("2", result)
    z = (a & c)  # - (a & b & c)
    print("z", z)
    if not len(z) == 0:
        result += len(z) - 1
    print(result)
    if not len(a & b & c) == 0:
        result -= 2 * (len(a & b & c) - 1)
        return result

    else:
        return result


# 다른 사람 풀이
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])


"""
중간에 틀렸던 풀이과정

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


def solution(lines):
    result=0
    num=[]
    for a,b in lines:
        num.append(range(a,b+1))
    a=set(num[0])
    b=set(num[1])
    c=set(num[2])
    if a&b==0:
        x=(b&c)
    x=(a&b)|(b&c)|(c&a)
    print(x)
    return len(x)-1
"""
