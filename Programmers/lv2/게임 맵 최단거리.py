"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/1844
"""
# 내 풀이 (개선 후) 정답처리된 풀이

from collections import deque


def solution(maps):
    q = deque([[0, 0, 1]])

    visit = [[False] * len(maps[0]) for _ in range(len(maps))]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y, z = q.popleft()

        visit[x][y] = True

        for new_x, new_y in zip(dx, dy):
            if 0 <= x + new_x < len(maps) and 0 <= y + new_y < len(maps[0]) and visit[x + new_x][y + new_y] == False and \
                    maps[x + new_x][y + new_y] != 0:
                q.append([x + new_x, y + new_y, z + 1])
                visit[x + new_x][y + new_y] = True

        if visit[len(maps) - 1][len(maps[0]) - 1] == True:
            return z + 1

    return -1
# 내 풀이(개선 중)
from collections import deque
def solution(maps):
    q = deque([[0, 0, 0]])  # 3번째는 지난 날짜
    block = []  # 벽
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # for i in range(len(maps)):
    #     for j in range(len(maps[0])):
    #         if maps[i][j]==0:
    #             block.append([i,j])

    visit = []
    # result=float("inf")
    flag = False

    while q:
        x, y, z = q.popleft()
        visit.append([x, y])
        if [x, y] == [len(maps) - 1, len(maps[0]) - 1]:
            return z + 1
            # if result>z:
            #     result=z
            #     flag=True

        # 남
        if 0 <= x + 1 < len(maps) and 0 <= y < len(maps[0]) and not [x + 1, y] in visit and maps[x + 1][y] != 0:
            # if 0<=x+1<len(maps) and 0<=y<len(maps[0]) and maps[x+1][y]!=0:
            #     if not [x+1,y] in visit:
            #         visit.append([x+1,y])
            #         q.append([x+1,y,z+1])
            visit.append([x + 1, y])
            q.append([x + 1, y, z + 1])
            # if [x+1,y]==[len(maps)-1,len(maps[0])-1]:
            #     if result>z+1:
            #         result=z+1
            #         flag=True
        # 북
        if 0 <= x - 1 < len(maps) and 0 <= y < len(maps[0]) and not [x - 1, y] in visit and maps[x - 1][y] != 0:
            # if 0<=x-1<len(maps) and 0<=y<len(maps[0]) and maps[x-1][y]!=0:
            #     if not [x-1,y] in visit:
            #         visit.append([x-1,y])
            #         q.append([x-1,y,z+1])
            visit.append([x - 1, y])
            q.append([x - 1, y, z + 1])
            # if [x-1,y]==[len(maps)-1,len(maps[0])-1]:
            #     if result>z+1:
            #         result=z+1
            #         flag=True
        # 동
        if 0 <= x < len(maps) and 0 <= y + 1 < len(maps[0]) and not [x, y + 1] in visit and maps[x][y + 1] != 0:
            # if 0<=x<len(maps) and 0<=y+1<len(maps[0]) and maps[x][y+1]!=0:
            #     if not [x,y+1] in visit:
            #         visit.append([x,y+1])
            #         q.append([x,y+1,z+1])
            visit.append([x, y + 1])
            q.append([x, y + 1, z + 1])
            # if [x,y+1]==[len(maps)-1,len(maps[0])-1]:
            #     if result>z+1:
            #         result=z+1
            #         flag=True
        # 서
        if 0 <= x < len(maps) and 0 <= y - 1 < len(maps[0]) and not [x, y - 1] in visit and maps[x][y - 1] != 0:
            # if 0<=x<len(maps) and 0<=y-1<len(maps[0]) and maps[x][y-1]!=0:
            #     if not [x,y-1] in visit:
            #         visit.append([x,y-1])
            #         q.append([x,y-1,z+1])
            visit.append([x, y - 1])
            q.append([x, y - 1, z + 1])
            # if [x,y-1]==[len(maps)-1,len(maps[0])-1]:
            #     if result>z+1:
            #         result=z+1
            #         flag=True

    #         for new_x,new_y in zip(dx,dy):
    #             if 0<=x+new_x<len(maps) and 0<=y+new_y<len(maps[0]) and not [x+new_x,y+new_y] in visit and not [x+new_x,y+new_y] in block:
    #                 visit.append([x+new_x,y+new_y])
    #                 q.append([x+new_x,y+new_y,z+1])

    #                 if [x+new_x,y+new_y]==[len(maps)-1,len(maps[0])-1]:
    #                     if result>z+1:
    #                         result=z+1
    #                         flag=True

    return result + 1 if flag != False else -1from collections import deque
def solution(maps):
    q=deque([[0,0,0]]) #3번째는 지난 날짜
    block=[] #벽
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    # for i in range(len(maps)):
    #     for j in range(len(maps[0])):
    #         if maps[i][j]==0:
    #             block.append([i,j])

    visit=[]
    # result=float("inf")
    flag=False

    while q:
        x,y,z=q.popleft()
        visit.append([x,y])
        if [x,y]==[len(maps)-1,len(maps[0])-1]:
            return z+1
            # if result>z:
            #     result=z
            #     flag=True

        #남
        if 0<=x+1<len(maps) and 0<=y<len(maps[0]) and not [x+1,y] in visit and maps[x+1][y]!=0:
        # if 0<=x+1<len(maps) and 0<=y<len(maps[0]) and maps[x+1][y]!=0:
        #     if not [x+1,y] in visit:
        #         visit.append([x+1,y])
        #         q.append([x+1,y,z+1])
            visit.append([x+1,y])
            q.append([x+1,y,z+1])
            # if [x+1,y]==[len(maps)-1,len(maps[0])-1]:
            #     if result>z+1:
            #         result=z+1
            #         flag=True
        #북
        if 0<=x-1<len(maps) and 0<=y<len(maps[0]) and not [x-1,y] in visit and maps[x-1][y]!=0:
        # if 0<=x-1<len(maps) and 0<=y<len(maps[0]) and maps[x-1][y]!=0:
        #     if not [x-1,y] in visit:
        #         visit.append([x-1,y])
        #         q.append([x-1,y,z+1])
            visit.append([x-1,y])
            q.append([x-1,y,z+1])
            # if [x-1,y]==[len(maps)-1,len(maps[0])-1]:
            #     if result>z+1:
            #         result=z+1
            #         flag=True
        #동
        if 0<=x<len(maps) and 0<=y+1<len(maps[0]) and not [x,y+1] in visit and maps[x][y+1]!=0:
        # if 0<=x<len(maps) and 0<=y+1<len(maps[0]) and maps[x][y+1]!=0:
        #     if not [x,y+1] in visit:
        #         visit.append([x,y+1])
        #         q.append([x,y+1,z+1])
            visit.append([x,y+1])
            q.append([x,y+1,z+1])
            # if [x,y+1]==[len(maps)-1,len(maps[0])-1]:
            #     if result>z+1:
            #         result=z+1
            #         flag=True
        #서
        if 0<=x<len(maps) and 0<=y-1<len(maps[0]) and not [x,y-1] in visit and maps[x][y-1]!=0:
        # if 0<=x<len(maps) and 0<=y-1<len(maps[0]) and maps[x][y-1]!=0:
        #     if not [x,y-1] in visit:
        #         visit.append([x,y-1])
        #         q.append([x,y-1,z+1])
            visit.append([x,y-1])
            q.append([x,y-1,z+1])
            # if [x,y-1]==[len(maps)-1,len(maps[0])-1]:
            #     if result>z+1:
            #         result=z+1
            #         flag=True

#         for new_x,new_y in zip(dx,dy):
#             if 0<=x+new_x<len(maps) and 0<=y+new_y<len(maps[0]) and not [x+new_x,y+new_y] in visit and not [x+new_x,y+new_y] in block:
#                 visit.append([x+new_x,y+new_y])
#                 q.append([x+new_x,y+new_y,z+1])

#                 if [x+new_x,y+new_y]==[len(maps)-1,len(maps[0])-1]:
#                     if result>z+1:
#                         result=z+1
#                         flag=True

    return result+1 if flag!=False else -1

# 내 풀이(개선 중)
from collections import deque


def solution(maps):
    q = deque([[0, 0, 1]])

    visit = [[False] * len(maps[0]) for _ in range(len(maps))]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y, z = q.popleft()

        visit[x][y] = True

        if [x, y] == [len(maps) - 1, len(maps[0]) - 1]:
            return z

        for new_x, new_y in zip(dx, dy):
            if 0 <= x + new_x < len(maps) and 0 <= y + new_y < len(maps[0]) and visit[x + new_x][y + new_y] == False and \
                    maps[x + new_x][y + new_y] != 0:
                q.append([x + new_x, y + new_y, z + 1])

    #         if 0<=x+1<len(maps) and 0<=y<len(maps[0]) and visit[x+1][y]==False and maps[x+1][y]!=0:
    #             q.append([x+1,y,z+1])

    #         if 0<=x-1<len(maps) and 0<=y<len(maps[0]) and visit[x-1][y]==False and maps[x-1][y]!=0:
    #             q.append([x-1,y,z+1])

    #         if 0<=x<len(maps) and 0<=y+1<len(maps[0]) and visit[x][y+1]==False and maps[x][y+1]!=0:
    #             q.append([x,y+1,z+1])

    #         if 0<=x<len(maps) and 0<=y-1<len(maps[0]) and visit[x][y-1]==False and maps[x][y-1]!=0:
    #             q.append([x,y-1,z+1])

    return -1

# 내 풀이 (개선 후)
from collections import deque


def solution(maps):
    q = deque([[0, 0, 1]])

    visit = [[False] * len(maps[0]) for _ in range(len(maps))]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y, z = q.popleft()

        visit[x][y] = True

        for new_x, new_y in zip(dx, dy):
            if 0 <= x + new_x < len(maps) and 0 <= y + new_y < len(maps[0]) and visit[x + new_x][y + new_y] == False and \
                    maps[x + new_x][y + new_y] != 0:
                q.append([x + new_x, y + new_y, z + 1])
                visit[x + new_x][y + new_y] = True

        if visit[len(maps) - 1][len(maps[0]) - 1] == True:
            return z + 1

    return -1