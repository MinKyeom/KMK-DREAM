# 내 풀이
def solution(my_string, m, c):
    result = []
    for x in range(len(my_string)):
        if m != c:
            if (x + 1) % m == c:
                result.append(my_string[x])
        elif m == c:
            if (x + 1) % m == 0:
                result.append(my_string[x])

    return "".join(result)

# 다른 사람 풀이
def solution(s, m, c):
    return s[c-1::m]

