# 내 풀이
def solution(a, d, included):
    num = []
    result = 0
    in_num = 0
    for x in range(len(included)):
        if x == 0:
            num.append(a)
            in_num = a
        else:
            in_num += d
            num.append(in_num)

        if included[x] == True:
            result += num[x]

    return result


# 다른 사람 풀이
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + d * i) * int(included[i])
    return answer