# baekjun 11000번

"""
의문 담고 있는포인트

1. 의문포인트 n과 Si,Ti범위는 고려하지 않아도 되는가? 여부
2. 수업 진행 시간에 대한 고려 포인트
"""


"""

import heapq
n=int(input())
print("일단 확인",n)
lecture_list=[list(map(int,input().split())) for _ in range(n)]
print("확인")
lecture_list.sort()

lecture_queue=[]
heapq.heappush(lecture_queue,lecture_list[0][1])

for i in range(1,n):
    if lecture_list[i][0]<lecture_queue[0]:
        heapq.headppush(lecture_queue,lecture_list[i][1])

    else:
        heapq.heapop(lecture_queue)
        heapq.headppush(lecture_queue,lecture_list[i][1])

print(len(lecture_queue))

"""






