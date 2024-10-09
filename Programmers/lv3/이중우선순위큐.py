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