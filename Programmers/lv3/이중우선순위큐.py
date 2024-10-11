"""
출처: 프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/42628
"""
# 내 풀이
import heapq
from collections import defaultdict


def solution(operations):
    max_q = []
    min_q = []
    number = defaultdict(int)

    for command in operations:
        if command == "D -1":
            while True:
                if len(min_q) == 0:
                    break
                if number[min_q[0]] == 0:
                    heapq.heappop(min_q)
                else:
                    break
            if len(min_q) == 0:
                continue

            num = heapq.heappop(min_q)
            number[num] -= 1

        elif command == "D 1":
            while True:
                if len(max_q) == 0:
                    break
                if number[max_q[0] * (-1)] == 0:
                    heapq.heappop(max_q)
                else:
                    break

            if len(max_q) == 0:
                continue

            num = heapq.heappop(max_q)
            number[num * (-1)] -= 1

        else:
            n = command.split(" ")
            c = int(n[1])
            heapq.heappush(max_q, c * (-1))
            heapq.heappush(min_q, c)
            number[c] += 1

    # print(max_q,min_q)
    # print(number)

    max_number = float("-inf")
    min_number = float("inf")

    for i in min_q:
        if number[i] > 0:
            max_number = max(max_number, i)
            min_number = min(min_number, i)

    if max_number == float("-inf"):
        return [0, 0]

    return [max_number, min_number]


# 다른 사람 풀이
from heapq import heappush, heappop

def solution(arguments):
    max_heap = []
    min_heap = []
    for arg in arguments:
        if arg == "D 1":
            if max_heap != []:
                heappop(max_heap)
                if max_heap == [] or -max_heap[0] < min_heap[0]:
                    min_heap = []
                    max_heap = []
        elif arg == "D -1":
            if min_heap != []:
                heappop(min_heap)
                if min_heap == [] or -max_heap[0] < min_heap[0]:
                    max_heap = []
                    min_heap = []
        else:
            num = int(arg[2:])
            heappush(max_heap, -num)
            heappush(min_heap, num)
    if min_heap == []:
        return [0, 0]
    return [-heappop(max_heap), heappop(min_heap)]


# 다른 사람 풀이
from collections import deque
from typing import List

class deheap:
    def __init__(self):
        self.sorted_elements = deque()

    def insert(self, val) -> None:
        begin, end = 0, len(self.sorted_elements)
        mid = (begin + end) // 2

        while begin < end:
            if self.sorted_elements[mid] > val:
                if begin != end:
                    end = mid
                else: break
            else:
                begin = mid + 1

            mid = (begin + end) // 2

        mid = max(mid, 0)  # mid is negative if val is the new minimum.
        self.sorted_elements.insert(mid, val)

    def empty(self) -> bool:
        return len(self.sorted_elements) == 0

    def delete_max(self) -> None:
        self.sorted_elements.pop()

    def delete_min(self) -> None:
        self.sorted_elements.popleft()

    def get_max_min(self) -> List:
        return [self.sorted_elements[-1], self.sorted_elements[0]]

def solution(operations):
    operations = [string.split() for string in operations]
    operations = [(cmd, int(num)) for cmd, num in operations]

    heap = deheap()
    for cmd, num in operations:
        if cmd == "I":
            heap.insert(num)
        elif cmd == "D" and not heap.empty():
            if num == 1:
                heap.delete_max()
            if num == -1:
                heap.delete_min()

    if heap.empty(): return [0, 0]
    return heap.get_max_min()