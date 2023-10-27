# 내 풀이
def solution(numbers):
    result = []
    for a in numbers:
        k = list(str(bin(a))[2:])
        t = k[::-1]
        flag = False

        for b in range(len(t)):
            if t[b] == "0":
                c = b
                flag = True
                break

        if flag == True:
            d = "1" + "0" * (b - 1)
            e = int(d, 2)
            result.append(a + e)

        else:
            d = "1" + "0" * (len(k) - 1)
            e = int(d, 2)
            result.append(a + e)

    return result

# 다른 사람 풀이
def solution(numbers):
    answer = []
    for idx, val in enumerate(numbers):
        answer.append(((val ^ (val+1)) >> 2) +val +1)

    return answer

# 다른 사람 풀이
def solution(numbers):
    answer = []
    for number in numbers:
        if number & 1:
            target = number
            idx = 0
            while number > 0:
                if number % 2 == 0:
                    break
                number //= 2
                idx += 1
            answer.append(target + 2 ** (idx) - 2 ** (idx-1))
        else:
            answer.append(number+1)

    return answer

