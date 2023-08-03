# 내 풀이
def solution(m, n, startX, startY, balls):
    result = []
    for x, y in balls:
        check = []
        # 아랫쪽 벽
        d_1 = abs(startX - x)
        st_down = d_1 * startY / (startY + y)
        if startX >= x:
            result_1 = ((st_down ** 2 + startY ** 2) ** 0.5 + ((x - (startX - st_down)) ** 2 + y ** 2) ** 0.5) ** 2

        else:
            result_1 = ((st_down ** 2 + startY ** 2) ** 0.5 + ((x - (startX + st_down)) ** 2 + y ** 2) ** 0.5) ** 2
        if x == startX and startY >= y:
            pass
        else:
            check.append(result_1)
            print("아래")

        # 왼쪽 벽
        d_2 = abs(startY - y)
        st_left = d_2 * startX / (startX + x)
        if startY >= y:
            result_2 = ((st_left ** 2 + startX ** 2) ** 0.5 + ((y - (startY - st_left)) ** 2 + x ** 2) ** 0.5) ** 2

        else:
            result_2 = ((st_left ** 2 + startX ** 2) ** 0.5 + ((y - (startY + st_left)) ** 2 + x ** 2) ** 0.5) ** 2
        if y == startY and startX >= x:
            pass
        else:
            check.append(result_2)
            print("왼쪽")

        # 위쪽 벽
        d_3 = abs(startX - x)
        st_up = d_3 * (n - startY) / (n * 2 - startY - y)
        if startX >= x:
            result_3 = ((st_up ** 2 + (n - startY) ** 2) ** 0.5 + (
                        (x - (startX - st_up)) ** 2 + (n - y) ** 2) ** 0.5) ** 2
        else:
            result_3 = ((st_up ** 2 + (n - startY) ** 2) ** 0.5 + (
                        (x - (startX + st_up)) ** 2 + (n - y) ** 2) ** 0.5) ** 2
        if x == startX and startY <= y:
            pass
        else:
            check.append(result_3)
            print("up")

        # 오른쪽 벽
        d_4 = abs(startY - y)
        st_right = d_4 * (m - startX) / (2 * m - startX - x)
        if startY >= y:
            result_4 = ((st_right ** 2 + (m - startX) ** 2) ** 0.5 + (
                        (y - (startY - st_right)) ** 2 + x ** 2) ** 0.5) ** 2

        else:
            result_4 = ((st_right ** 2 + (m - startX) ** 2) ** 0.5 + (
                        (y - (startY + st_right)) ** 2 + x ** 2) ** 0.5) ** 2
        if y == startY and startX <= x:
            pass
        else:
            check.append(result_4)
            print("right")

        print(check)

        if min(check) > int(min(check)) + 0.9999:
            result.append(int(min(check)) + 1)
        else:
            result.append(min(check))

    return result