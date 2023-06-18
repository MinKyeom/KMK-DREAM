# 내 풀이
def solution(strArr):
    for x in range(len(strArr)):
        if x % 2 == 0:
            strArr[x] = strArr[x].lower()
        else:
            strArr[x] = strArr[x].upper()

    return strArr
# 다른 사람 풀이
def solution(strArr):
    return [s.lower() if i % 2 == 0 else s.upper() for i, s in enumerate(strArr)]

