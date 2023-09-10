# 내 풀이(개선 중)
def solution(n, k, enemy):
    if k == len(enemy):
        return k

    check = [x for x in range(k)]

    while k > 0:

    answer=0
    
    return answer
# 내 풀이
def solution(n, k, enemy):
    import heapq
    result = 0
    heap = []

    check = 0

    for x in enemy:
        heapq.heappush(heap, -x)
        check += x

        if check > n:
            if k == 0:
                break
            y = heapq.heappop(heap)
            k -= 1
            n += (-y)

        result += 1

    return result

# 다른 사람 풀이

from heapq import heappop, heappush


def solution(n, k, enemy):
    answer, sumEnemy = 0, 0
    heap = []

    for e in enemy:
        heappush(heap, -e)
        sumEnemy += e
        if sumEnemy > n:
            if k == 0: break
            sumEnemy += heappop(heap)
            k -= 1
        answer += 1
    return answer
