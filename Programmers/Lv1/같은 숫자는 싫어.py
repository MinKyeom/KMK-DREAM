# 내 풀이
def solution(arr):
    result = []
    for x in arr:
        if not result:
            result.append(x)
        else:
            if result[-1] != x:
                result.append(x)

    return result

# 다른 사람 풀이
def no_continuous(s):
    # 함수를 완성하세요
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

