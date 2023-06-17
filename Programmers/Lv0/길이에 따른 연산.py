# 내 풀이
def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        count = 1
        for x in range(len(num_list)):
            count *= num_list[x]

    return count


# 다른 사람 풀이
def solution(num_list):
    if len(num_list) >= 11:
        return eval('+'.join(list(map(str, num_list))))
    else:
        return eval('*'.join(list(map(str, num_list))))

