# 내 풀이
def solution(n, m, section):
    count = 0
    check = section[0]
    if len(section) == 1:
        return 1
    for x in range(1, len(section)):
        if x == 1:
            if abs(section[x] - check + 1) > m:
                count += 2
                check = section[x]
            else:
                count += 1
        else:
            if abs(section[x] - check + 1) > m:
                count += 1
                check = section[x]
            else:
                continue

    return count
# 다른 사람 풀이
def solution(n, m, section):
    answer = 1
    prev = section[0]
    for sec in section:
        if sec - prev >= m:
            prev = sec
            answer += 1

    return answer