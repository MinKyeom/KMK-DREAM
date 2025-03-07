"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/148653
"""
# 풀이 과정
def solution(storey):
    x = list(str(storey))
    x = list(map(int, x))
    count = 0

    if len(x) == 1:
        return x[0] if x[0] <= 5 else 10 - x[0] + 1

    for k in range(len(x) - 1, 0, -1):
        a = 10 - x[k]
        b = x[k]
        if b < 5:
            count += b
        elif b == 5:
            if k - 1 >= 0 and x[k - 1] >= 5:
                x[k - 1] = x[k - 1] + 1
                count += b
            else:
                count += b

        else:
            count += a
            if k - 1 >= 0:
                x[k - 1] += 1

    if x[0] <= 5:
        return count + x[0]
    else:
        return count + 10 - x[0] + 1


# 다른 사람 풀이
def solution(storey):
    if storey < 10 :
        return min(storey, 11 - storey)
    left = storey % 10
    return min(left + solution(storey // 10), 10 - left + solution(storey // 10 + 1))


# 풀이2
def solution(storey):
    answer = 0

    while(storey!=0):
        n = storey%10
        num = 0
        if n < 5:
            num = n
            storey -= n
        elif n > 5:
            num = 10 - n
            storey += num
        else:
            num = 5


        if num == 5:
            _storey = storey // 10
            if _storey % 10 >= 5:
                storey += num
            elif _storey % 10 < 5:
                storey -= num
        storey = storey // 10
        answer += num
    return answer