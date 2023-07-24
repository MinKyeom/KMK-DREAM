# 내 풀이
def solution(r1, r2):
    count = 0
    for x in range(1, r2 + 1):
        a = (r2 ** 2 - x ** 2) ** 0.5
        b = 0 if x > r1 else (r1 ** 2 - x ** 2) ** 0.5
        if a - b <= 1:
            if int(a) == a and int(b) != b:
                count += 1
            elif int(a) != a and int(b) == b:
                count += 1
            elif int(a) == 0 and int(b) == 0:
                count += 1
            else:
                count += int(a) - int(b)
        elif a - b >= 1 and int(a) == a and int(b) == b:
            count += int(a) - int(b) + 1
        elif a - b >= 1 and int(b) == b:
            count += int(a) - int(b) + 1
        elif a - b >= 1 and int(a) == a:
            count += int(a) - int(b)
        else:
            count += int(a) - int(b)

    return count * 4
# 다른 사람 풀이
from math import sqrt

def solution(r1, r2):
    quar = 0
    for i in range(0, r1):
        quar += int(sqrt(r2**2 - i**2)) - int(sqrt(r1**2 - i**2 - 1))
    for i in range(r1, r2):
        quar += int(sqrt(r2**2 - i**2))
    return quar * 4
