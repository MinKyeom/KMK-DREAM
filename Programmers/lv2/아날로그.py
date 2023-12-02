# 내 풀이(개선 중)
def solution(h1, m1, s1, h2, m2, s2):
    result = 0
    # 총 시간 계산
    h_1 = h1 * 60 * 60 + m1 * 60 + s1
    h_2 = h2 * 60 * 60 + m2 * 60 + s2
    start = s1

    check_h = 60 * 60 * 12
    """
    시간 60**2*12초동안 360도 
    분 60**2초 동안 360도
    초 60초동안 360도
    """

    for k in range(h_1, h_2 + 1):
        h = float(k / check_h)  # -int(k*360/(60*60*12))
        m = float(k / (60 * 60))  # -int(k*360/(60*60))
        s = float(k / 60) - int(k / 60)

        print(h, m, s)
        print(h * 360, m * 360, s * 360)
        break
        if round(h - s, 10) == 0 or round(m - s, 10) == 0:
            result += 1

    return result

# 다른 사람 풀이