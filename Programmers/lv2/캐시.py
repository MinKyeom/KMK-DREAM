# 내 풀이
def solution(cacheSize, cities):
    from collections import deque

    result = 0
    check = deque([])  # cache_list

    if cacheSize == 0:
        return len(cities) * 5

    for a in cities:
        a = a.upper()
        if len(check) < cacheSize:
            if a in check:
                i = check.index(a)
                del check[i]
                check.append(a)
                result += 1

            else:
                check.append(a)
                result += 5

        else:
            if a in check:
                i = check.index(a)
                del check[i]
                check.append(a)
                result += 1

            else:
                check.popleft()
                check.append(a)
                result += 5

    return result

# 다른 사람 풀이

def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time