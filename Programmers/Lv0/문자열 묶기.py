# 내 풀이
def solution(strArr):
    num = []
    result = []
    for x in range(len(strArr)):
        num.append(len(strArr[x]))

    for k in range(31):
        s = num.count(k)
        result.append(s)

    return max(result)
# 다른 사람 풀이
def solution(strArr):
    a=[0]*31
    for x in strArr: a[len(x)]+=1
    return max(a)