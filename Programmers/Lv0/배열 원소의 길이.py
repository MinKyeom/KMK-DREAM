# 내 풀이
def solution(strlist):
    result = []
    for a in strlist:
        x = len(a)
        result.append(x)

    return result

# 다른 사람 풀이

def solution(strlist):
    answer = list(map(len, strlist))
    return answer