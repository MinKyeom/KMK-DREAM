# 내 풀이
def solution(arr, queries):
    result = []
    sub = []
    while len(result) < len(queries):
        for s, e, k in queries:
            num = [x for x in range(s, e + 1)]
            for z in num:
                if arr[z] > k:
                    sub.append(arr[z])
            if len(sub) == 0:
                result.append(-1)
                sub.clear()
                continue
            r = min(sub)
            result.append(r)
            sub.clear()

    return result


# 다른 사람 풀이
def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        tmp = []
        for x in arr[s:e+1]:
            if x > k:
                tmp.append(x)
        answer.append(-1 if not tmp else min(tmp))
    return answer