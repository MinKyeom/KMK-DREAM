# 내 풀이
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

    cur_h = ((h_1 * 360) / (60 * 60 * 12)) % 360
    cur_m = ((h_1 * 360) / (60 * 60)) % 360
    cur_s = ((h_1 * 360) / 60) % 360

    if cur_h == cur_s or cur_m == cur_s:
        result += 1

    for k in range(h_1 + 1, h_2 + 1):

        after_h = ((k * 360) / (60 * 60 * 12)) % 360
        after_m = ((k * 360) / (60 * 60)) % 360
        after_s = ((k * 360) / 60) % 360

        # 시간-초
        if cur_h > cur_s and after_h < after_s:
            result += 1
        elif cur_h > cur_s and after_s == 0:
            result += 1
        elif after_h == after_s:
            result += 1

        # 분-초
        if cur_m > cur_s and after_m < after_s:
            result += 1
        elif cur_m > cur_s and after_s == 0:
            result += 1
        elif after_m == after_s:
            result += 1

        # 시간-분-초

        if after_h == after_m == after_s:
            result -= 1

        cur_h, cur_m, cur_s = after_h, after_m, after_s

    return result

# 다른 사람 풀이

def solution(h1, m1, s1, h2, m2, s2):
    vh, vm, vs = 1, 12, 720
    L = 43200
    t1, t2 = h1*3600+m1*60+s1, h2*3600+m2*60+s2
    h, m, s = vh*t1%L, vm*t1%L, vs*t1%L
    ans = 1 if h==s or m==s else 0
    flag_hs = 1 if s>=h else 0
    flag_ms = 1 if s>=m else 0
    for _ in range(t1+1,t2+1):
        h += vh
        m += vm
        s += vs
        if h == m == s:
            ans += 1
        else:
            if flag_hs==0 and s>=h:
                ans += 1
            if flag_ms==0 and s>=m:
                ans += 1
        h %= L
        m %= L
        s %= L
        flag_hs = 0 if s<h else 1
        flag_ms = 0 if s<m else 1
    return ans
