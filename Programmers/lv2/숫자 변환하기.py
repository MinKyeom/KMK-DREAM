# 내 풀이
def solution(x, y, n): # 시간초과 발생
    from collections import deque
    check = deque([x])
    count = 0
    num = 0

    while True:
        count += 1
        if x == y:
            return 0

        if check[0] <= y:
            a = check[0] + n
            b = check[0] * 2
            c = check[0] * 3

            if a == y or b == y or c == y:
                for m in range(1000000):
                    if count <= 3 ** m:
                        return m + 1

            else:
                if a < y:
                    if a + n <= y or a * 2 <= y or a * 3 <= y:
                        check.append(a)

                if b < y:
                    if b + n <= y or b * 2 <= y or b * 3 <= y:
                        check.append(b)

                if c < y:
                    if c + n <= y or c * 2 <= y or c * 3 <= y:
                        check.append(c)

                check.popleft()

                if len(check) == 0:
                    return -1
# 내 풀이2
# 개선 후 통과
def solution(x, y, n):
    from collections import deque
    check = deque([y])
    result = 0

    if x == y:
        return 0

    while True:
        newcheck = []
        result += 1

        for k in list(check):
            a = k - n
            b = k / 2
            c = k / 3
            if a == x or b == x or c == x:
                print(a, b, c)
                return result

            else:
                if a >= x:
                    newcheck.append(a)
                if b >= x and int(b) == b:
                    newcheck.append(int(b))
                if c >= x and int(c) == c:
                    newcheck.append(int(c))

        if len(newcheck) == 0:
            return -1

        check = newcheck

