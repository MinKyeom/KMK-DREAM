# N=int(input())
#point_review
"""

input 과정 중 헷갈렸던 point
a=int(input().split())

a,d= input().split()

b,c=map(int,input().split())

e=map(int,input().split())

print("a,d",a,d) 

print("b,c",b,c)

print("c",c)
#print("list(c)",list(c))

"""


"""
sort 나열할 때 2차 행렬시 나열 
# a=[(1,3),(2,4),(1,5),(1,7)]
# 
# a.sort()
# #[0][x] 일단 [0]을 순서대로 나열 후 [x]를 그 다음 순서대로 나열!
# print(a)
"""
"""
import heapq

n=int(input())
lecture=[]
for x in range(n):
    lecture.append(list(map(int,input().split())))
lecture.sort()
lecture_list=[]
heapq.heappush(lecture_list,lecture[0][1])

for y in range(1,n):
    if lecture[y][0]<lecture_list[0]:
        heapq.heappush(lecture_list,lecture[y][1])

    else:
        heapq.heappop(lecture_list)
        heapq.heappush(lecture_list,lecture[y][1])

print(len(lecture_list))
"""

import heapq
import sys

n=int(input())
lecture=[]

for x in range(n):
    lecture.append(list(map(int,sys.stdin.readline().split())))

lecture.sort() #nlog(n)
lecture_list=[]
heapq.heappush(lecture_list,lecture[0][1]) #log(n)

for y in range(1,n):
    if lecture[y][0]<lecture_list[0]:
        heapq.heappush(lecture_list,lecture[y][1])

    else:
        heapq.heappop(lecture_list)
        heapq.heappush(lecture_list,lecture[y][1])
#(n-1)log(n)
print(len(lecture_list))


# 시간복잡도 계산시 유의사항
#입력 받는 부분 제외!


