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


# 다른 사람 풀이
# n = int(input())
# cnt = 0
# result = 666
#  
# while True:
#     if '666' in str(result):
#         cnt += 1
#  
#     if cnt == n:
#         break
#  
#     result += 1
#  
# print(result)
