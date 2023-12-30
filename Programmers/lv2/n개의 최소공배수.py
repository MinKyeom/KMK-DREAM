# 내 풀이
def solution(arr):
    result = 2

    for a in arr:
        if result != 1 and result % a == 0:
            continue

        else:
            count = min(a, result)

            while count > 1:
                if result % count == 0 and a % count == 0:
                    break
                else:
                    count -= 1

            result = (a * result) // count

    return result

# 다른 사람 풀이
from fractions import gcd


def nlcm(num):
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer

print(nlcm([2,6,8,14]));