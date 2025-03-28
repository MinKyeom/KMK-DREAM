"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/12927
"""

# 풀이 과정
import heapq


def solution(n, works):
    # map(lambda x:x*x,works)

    new = []

    for i in works:
        heapq.heappush(new, -i)

    while n > 0:
        k = heapq.heappop(new)
        k += 1
        heapq.heappush(new, k)
        n -= 1

    if new[0] >= 0:
        # print(new)
        return 0

    return sum(list(map(lambda x: x * x, new)))

# 다른 사람 풀이
def noOvertime(n, works):
  if n>=sum(works):
    return 0;

  while n > 0:
    works[works.index(max(works))] -= 1
    n -= 1

  result = sum([w ** 2 for w in works])

  return result