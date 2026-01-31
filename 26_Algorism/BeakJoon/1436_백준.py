"""
출처:https://www.acmicpc.net/problem/1436
"""

# 풀이_개선 중

from collections import deque

n = int(input("") )

start = deque(list(str(n -1)))

while True:
  if start[0] == "0":
    start.popleft()
  
  else:
    break
front = "".join(start)
answer = int(front + "666")

print(answer)

