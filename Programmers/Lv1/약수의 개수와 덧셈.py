# 내 풀이
def solution(left, right):
    result = 0
    for x in range(left, right + 1):
        count = []
        for y in range(1, int(x ** (1 / 2)) + 1):
            if x % y == 0:
                k = int(x / y)
                if k != y:
                    count.append(y)
                    count.append(k)
                else:
                    count.append(k)
        if len(count) % 2 == 0:
            result += x
        else:
            result -= x

    return result

# 다른 사람 풀이
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer