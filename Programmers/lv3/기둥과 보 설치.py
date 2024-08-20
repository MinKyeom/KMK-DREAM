"""
출처:프로그래머스
https://school.programmers.co.kr/learn/challenges?order=recent&levels=3&languages=python3&page=3
"""

# 내 풀이 (개선 중)
"""
생각 방향

기둥 > 세로 이동
보 > 가로 이동 

[x,y,a,b]
x,y 설치 or 삭제 좌표 [ 가로, 세로 ]
a: 구조물 종류 0 기둥 1 보
b: 설치 or 삭제 0:설치 1:삭제

삭제함으로써 > 기존 기둥 구조들이 사라지는거 확인
예전 카카오 액셀 삭제 추가 문제 기억

# 풀다 느낀 포인트 사고

삭제 된 후 이미 건축된 구조물 재구성 
보를 판단할 선분 처리 방식 생각

"""
# sol1
"""
from collections import deque

def solution(n, build_frame):
    check=[[False]*n for _ in range(n)]

    # 4방향 탐색
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    # 3방향 탐색
    x_=[-1,0,0]
    y_=[0,1,-1]

    for x,y,a,b in build_frame:
        if b==1:
            if a==0:
                check[x][y],check[x-1][y]=False,False
                # 삭제함으로써 관련된 구조물 삭제
                q=deque([(x,y)])

                visit=[[False]*n for _ in range(n)]

                while q:
                    v,w=q.popleft()

                    visit[v][w]=True
                    # 해당점 존재 가능 여부 확인 
                    case1=False
                    case2=False

                    #1 바닥에 지지대 존재
                    if 0<=v+1<n:
                        if check[v+1][w]==True:
                            case1=True
                            pass
                    #2 양쪽에 지지대 존재 
                    if 0<=w+1<n and 0<=w-1<n:
                        if check[v][w+1]==True and check[v][w-1]==True:
                            case2=True
                            pass
                    if case1==False and case2==False:
                        check[v][w]=False

                    # 주변 점검 재탐색 
                    for nx,ny in zip(x_,y_):
                        if 0<=v+nx<n and 0<=w+nx<n:
                            if visit[v+nx][w+nx]==False and check[v+nx][w+nx]==True:
                                visit[v+nx][w+nx]=True
                                q.append((v+nx,w+nx))



            else:
                check[x][y],check[x][y+1]=False,False
                # 삭제함으로써 관련된 구조물 삭제
                q=deque([(x,y),(x,y+1)])
                visit=[[False]*n for _ in range(n)]

                while q:
                    v,w=q.popleft()

                    visit[v][w]=True
                    # 해당점 존재 가능 여부 확인 
                    case1=False
                    case2=False

                    #1 바닥에 지지대 존재
                    if 0<=v+1<n:
                        if check[v+1][w]==True:
                            case1=True
                            pass
                    #2 양쪽에 지지대 존재 
                    if 0<=w+1<n and 0<=w-1<n:
                        if check[v][w+1]==True and check[v][w-1]==True:
                            case2=True
                            pass
                    if case1==False and case2==False:
                        check[v][w]=False

                    # 주변 점검 재탐색 
                    for nx,ny in zip(x_,y_):
                        if 0<=v+nx<n and 0<=w+nx<n:
                            if visit[v+nx][w+nx]==False and check[v+nx][w+nx]==True:
                                visit[v+nx][w+nx]=True
                                q.append((v+nx,w+nx))

        else:
            # 기둥
            if a==0:
                # 맨 아래
                if x==n-1:
                    check[x][y],check[x-1][y]=True,True

                else:
                    if check[x+1][y]==True:
                        check[x][y],check[x-1][y]=True,True
            # 보
            else:
                if x==n-1:
                    continue
                else:
                    # 두 점 (x,y),(x,y+1)





    return 0

"""

# 다른 사람 풀이
def check_build(answer):
    for x, y, a in answer:
        # 기둥인 경우
        if a == 0:
            # 좌표가 바닥에 해당 x
            # 좌표 아래에 기둥이 존재 x
            # 보의 한 쪽 위 x
            if (y != 0 and
                    [x, y - 1, 0] not in answer and
                    [x - 1, y, 1] not in answer and
                    [x, y, 1] not in answer):
                return False
        # 보인 경우
        else:
            # 아래애 기둥 존재 x
            # 양쪽에 보 존재 x
            if ([x, y - 1, 0] not in answer and
                    [x + 1, y - 1, 0] not in answer and
                    ([x - 1, y, 1] not in answer or
                     [x + 1, y, 1] not in answer)):
                return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        # 삭제라면
        if b == 0:
            answer.remove([x, y, a])
            # 삭제 후, check가 통과되지 못한다면, 재설치
            if not check_build(answer):
                answer.append([x, y, a])

# 다른 풀이
def check(answer):
    for x, y, stuff in answer:
        if stuff == 0: #기둥 체크
            #'바닥 위' or '보의 한쪽 끝 위' or '또 다른 기둥 위'
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif stuff == 1: #보 체크
            #'한쪽 끝 부분이 기둥 위' or '양쪽 끝 부분이 다른 보와 동시 연결'
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y, stuff, operation = build
        if operation == 1: # 설치
            answer.append([x, y, stuff])
            if not check(answer): answer.remove([x, y, stuff])
        elif operation == 0: # 삭제
            answer.remove([x, y, stuff])
            if not check(answer): answer.append([x, y, stuff])
    answer.sort()
    print(answer)
    return answer
