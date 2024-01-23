# 내 풀이(개선 중)
# 1.재귀로 연속으로 숫자를 바꾸기
# 2.조합으로 생각 후 연속 된 숫자를 나눠서 위치로 숫자 찾기
def solution(n):
    num = ["1", "2", "4"]
    result = ""

    n = 6

    if n == 1:
        return "1"
    elif n == 2:
        return "2"
    elif n == 3:
        return "4"

    while True:
        i, j = divmod(n, 3)

        if i == 0:
            result += num[j - 1]
            break
        elif j == 0:
            result += num[-1]
            n = j
        else:
            result += num[i - 1]
            n = j

    return result

# 다른 사람 풀이