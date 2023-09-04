# 내 풀이 (아직 개선중)
def solution(n, l, r):
    k = "11011"
    count = 1
    count_l = 0
    count_r = 0
    while len(k) <= r:
        count += 1
        k = k * 2 + "0" * (5 ** (count - 1)) + k * 2

    result = k[l - 1:r].count("1")

    return result

