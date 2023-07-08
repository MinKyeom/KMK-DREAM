# 내 풀이
def solution(sizes):
    num_1 = []
    num_2 = []
    for x in sizes:
        l = max(x)
        num_1.append(l)
        m = min(x)
        num_2.append(m)

    return max(num_1) * max(num_2)

# 다른 사람 풀이
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)