# 내 풀이
def solution(scoville, K):
    import heapq
    t = scoville
    heap = []
    result = 0

    # for문 len(t) 개수만큼이라 t.sort()로 한 후 시작한거랑 동일!
    while t:
        a = t.pop()
        heapq.heappush(heap, a)

    while heap:

        a = heapq.heappop(heap)

        if a < K:
            if len(heap) > 0:
                result += 1
                b = heapq.heappop(heap)
                count = (a + b * 2)
                heapq.heappush(heap, count)
            else:
                return -1  # 다 섞어도 k 못넘음
        else:
            break

    return result

# 다른 사람 풀이
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1

    return answer