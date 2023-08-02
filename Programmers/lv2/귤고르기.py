# 내 풀이
def solution(k, tangerine):
    count = {}
    for x in tangerine:
        if not str(x) in count:
            count[str(x)] = 1
        else:
            count[str(x)] += 1

    count = sorted(count.items(), key=lambda x: -x[1])

    result = []

    for y, z in count:
        if k > 0:
            result.append(y)
            k -= z
        else:
            break

    return len(result)

# 다른 사람 풀이

import collections
def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)

    for v in sorted(cnt.values(), reverse = True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer