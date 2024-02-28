# 내 풀이(개선 중)
# 이분탐색 접근 생각
def solution(sequence):
    t1 = [1, -1]  # 1,-1,1...
    t2 = [-1, 1]  # -1,1,-1...
    result = []
    s = sequence

    i, j = divmod(len(s), 2)
    t1 += [1, -1] * (i - 1)
    t2 += [-1, 1] * (i - 1)

    t1 += [1] * j
    t2 += [-1] * j

    a = []
    b = []

    result = []

    if len(s) == 1:
        t1 = [1]
        t2 = [-1]

    for k in range(len(s)):
        a.append(t1[k] * s[k])
        b.append(t2[k] * s[k])

    start = 0
    end = 0

    while start < len(s) - 1:
        one = sum(a[start:end + 1])
        two = sum(b[start:end + 1])

        result.append(one)
        result.append(two)

        if start == end and end < len(s) - 1:
            end += 1
        else:
            if end < len(s) - 1:
                end += 1
            elif end == len(s) - 1:
                start += 1
                end = start

                if end == len(s) - 1:
                    result.append(a[end])
                    result.append(b[end])
                    break

    return max(result)

# 다른 사람 풀이
