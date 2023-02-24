#heapq_module
import heapq
"""
최소 값을 필요로하는  알고리즘에 많이 쓰임!!

"""


"""
힙은 모든 부모 노드가 자식보다 작거나 같은 값은 갖는 이진 트리입니다."""

"""
heapq.heappush(heap,item)
→힙 불변성을 유지하면서,item 값음 heap으로 푸시합니다.
"""
heapq_1=[]
heapq.heappush(heapq_1,4)
print("1:",heapq_1)

heapq.heappush(heapq_1,5)
print("2:",heapq_1)

heapq.heappush(heapq_1,1)
print("3:",heapq_1)

print(heapq_1[0])
"""
heapq.heappop(heap)
→힙 불변성을 유지하면서, heap에서 가장 작은 항목을 팝하고 반환합니다. 힙이 비어 있으면
indexError 발생! 팝하지 않고 가장 작은 항목에서 excess하려면
heap[0]을 사용!
"""
print()
print("heapq.heappop 하기 전",heapq_1)
print("heapq.heapop:",heapq.heappop(heapq_1))

#heapop을 통해서 [0]가 빠지면 새로운 [0]에도 리스트 중 최솟값이 오게 배열된다!

print(heapq_1) #반환을 했기에 heapq[0]값이 변함!
"""
heapq.heappushpop(heap,item)
→힙에 item을 푸시한 다음 heap에서 가장 작은 항목을 팝하고 반환합니다.
"""
heapq.heappushpop(heapq_1,10)
print()
print(heapq_1)#제일 작은값이 반환된 상태로 나옴!

"""
heapq.heapify
"""
list_1=[5,2,1,3,4]
print("list_1:",list_1)
print()
heapq.heapify(list_1)
print("list_1 힙으로 변환 후:",list_1)
