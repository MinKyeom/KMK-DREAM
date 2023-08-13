# 내 풀이 (수정 중)
def solution(s):
    if len(s) == 1:
        return 0

    if len(s) == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 0

    k = list(s)
    count = 0

    while count < len(k) - 1:
        if k[count] == k[count + 1]:
            del k[count]
            del k[count]

            if len(k) >= 1 and count >= 1:
                count -= 1
                continue
            elif count == 0:
                count = 0
                continue
            else:
                return 1
        count += 1

    return 1 if len(k) == 0 else 0

# 다른 사람 풀이
