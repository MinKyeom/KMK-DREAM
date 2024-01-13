# 내 풀이(개선 중)
from collections import deque


def solution(n):
    top_1 = deque([k for k in range(n, 0, -1)])
    top_2 = deque([])
    top_3 = deque([])
    count = 0
    result = 0
    print(top_1)
    flag = False

    #     while len(top_3)<=n:
    #         # 큰 거 옮겨주기
    #         if len(top_2)==0 or len(top_3)==0:
    #             a=top_1.popleft()
    #             if len(top_2)==0:
    #                 top_2.append(a)
    #             else:
    #                 top_3.append(a)

    #             result+=1
    #         # 합치기
    #         else:
    #             if top_3[-1]>top_2[-1]:
    #                 b=top_2.pop()

    return result
