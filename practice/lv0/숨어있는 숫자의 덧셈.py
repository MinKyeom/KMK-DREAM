# 내 풀이
def solution(my_string):
    x = list(my_string)
    count = 0
    result = []
    a = "abcdefghijklmnopqrstuvwxyz"
    b = a.upper()
    for c in range(len(x)):
        if x[c] in a or x[c] in b:
            x[c] = "영"
            continue
        else:
            continue

    for d in range(len(x)):
        if x[d] == "영":
            if not len(result) == 0:
                e = "".join(result)
                count += int(e)
                result.clear()
        else:
            result.append(x[d])
            if d == len(x) - 1:
                e = "".join(result)
                count += int(e)
                return count

    answer = count
    return answer


# 다른 사람 풀이
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())
