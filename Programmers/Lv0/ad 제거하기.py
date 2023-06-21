# 내 풀이
def solution(strArr):
    result = []
    for x in range(len(strArr)):
        if not "ad" in strArr[x]:
            result.append(strArr[x])

    return result
# 다른 사람 풀이
def solution(strArr):
    answer = []
    for x in strArr:
        if 'ad' in x: continue
        answer.append(x)
    return answer
