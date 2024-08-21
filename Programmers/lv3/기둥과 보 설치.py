"""
출처:프로그래머스
https://school.programmers.co.kr/learn/challenges?order=recent&levels=3&languages=python3&page=3
"""
# 내 풀이
from collections import deque

# sol2

# 기둥 유지 가능 여부 확인
def check_up(x, y, check):
    # 그 아래 기둥이 있는 경우
    if (x, y - 1, x, y) in check:
        # check.add((x,y,x,y+1))
        return True
        # 그 아래 보가 있을 경우
    elif (x - 1, y, x, y) in check or (x, y, x + 1, y) in check:
        # check.add((x,y,x,y+1))
        return True
    else:
        return set([(x, y, x, y + 1)])

    # 보 유지 가능 여부 확인


def check_right(x, y, check):
    # 밑에 기둥이 있거나, 양쪽 보가 존재가 할 경우
    if (x, y - 1, x, y) in check or (x + 1, y - 1, x + 1, y) in check:
        # check.add((x,y,x+1,y))
        return True
    # 양쪽 보가 존재할 경우
    elif (x - 1, y, x, y) in check and (x + 1, y, x + 2, y) in check:
        # check.add((x,y,x+1,y))
        return True
    else:
        return set([(x, y, x + 1, y)])


def solution(n, build_frame):
    # 기둥,보 설치 확인
    check = set([])

    for x, y, a, b in build_frame:
        # 설치 1
        if b == 1:
            # 기둥
            if a == 0:
                # 바닥인경우
                if y == 0:
                    check.add((x, y, x, y + 1))

                else:
                    # 그 아래 기둥이 있는 경우
                    if (x, y - 1, x, y) in check:
                        check.add((x, y, x, y + 1))

                    # 그 아래 보가 있을 경우
                    elif (x - 1, y, x, y) in check or (x, y, x + 1, y) in check:
                        check.add((x, y, x, y + 1))

            # 보
            else:
                if y != 0:
                    # 밑에 기둥이 있거나, 양쪽 보가 존재가 할 경우
                    if (x, y - 1, x, y) in check or (x + 1, y - 1, x + 1, y) in check:
                        check.add((x, y, x + 1, y))
                    # 양쪽 보가 존재할 경우
                    elif (x - 1, y, x, y) in check and (x + 1, y, x + 2, y) in check:
                        check.add((x, y, x + 1, y))


        else:
            q = deque([])
            up = [(0, 1, 0, 2), (-1, 1, 0, 1), (0, 1, 1, 1)]  # 기둥
            right = [(1, 0, 2, 0), (1, 0, 1, 1), (-1, 0, 0, 0), (0, 0, 0, 1)]  # 보

            # 기둥
            if a == 0:
                k = set([(x, y, x, y + 1)])
                check = check - k  # 기둥 제거
                # 제거되는지 여부 판단
                for a, b, c, d in up:
                    if (x + a, y + b, x + c, y + d) in check:
                        # 기둥
                        if d - b == 1:
                            flag = check_up(x + a, y + b, check)
                            if flag != True:
                                check = check | k
                                break
                        else:
                            flag = check_right(x + a, y + b, check)
                            if flag != True:
                                check = check | k
                                break
                else:
                    k = set([(x, y, x, y + 1)])
                    check = check - k  # 기둥 제거
                """
                for a,b,c,d in up:
                    if (x+a,y+b,x+c,y+d) in check:
                        q.append((x+a,y+b,x+c,y+d))
                """
            # 보 제거 여부 판단
            else:
                k = set([(x, y, x + 1, y)])
                check = check - k  # 기둥 제거

                # 제거되는지 여부 판단
                for a, b, c, d in right:
                    if (x + a, y + b, x + c, y + d) in check:
                        # 기둥
                        if d - b == 1:
                            flag = check_up(x + a, y + b, check)

                            if flag != True:
                                check = check | k
                                break
                        else:
                            flag = check_right(x + a, y + b, check)
                            if flag != True:
                                check = check | k
                                break
                else:
                    k = set([(x, y, x + 1, y)])
                    check = check - k  # 기둥 제거

                """
                for a,b,c,d in right:
                    if (x+a,y+b,x+c,y+d) in check:
                        q.append((x+a,y+b,x+c,y+d))
                        break
                else:        
                    k=set([(x,y,x+1,y)])
                    check=check-k # 보 제거
                """

                """
                for a,b,c,d in right:
                    if (x+a,y+b,x+c,y+d) in check:
                        q.append((x+a,y+b,x+c,y+d))

                """

            # 기둥 또는 보를 제거함으로써 주변 제거할 기둥 보 탐색
            """
            while q:
                k=q.popleft()

                # 기둥
                if k[3]-k[1]!=0:
                    shape="기둥"
                    exist=check_up(k[0],k[1],check)
                # 보
                else:
                    shape="보"
                    exist=check_right(k[0],k[1],check)

                if exist==True:
                    continue

                else:
                    check=check-exist
                    if shape=="기둥":
                        for a,b,c,d in up:
                            if (k[0]+a,k[1]+b,k[0]+c,k[1]+d) in check:
                                    q.append((k[0]+a,k[1]+b,k[0]+c,k[1]+d))

                    else:
                        for a,b,c,d in right:
                            if (k[0]+a,k[1]+b,k[0]+c,k[1]+d) in check:
                                    q.append((k[0]+a,k[1]+b,k[0]+c,k[1]+d))                        
            """
        # print(check,"check")

    # 마무리 단계 재 구조화
    result = []

    for a, b, c, d in check:
        if d - b == 1:
            s = 0
        else:
            s = 1
        result.append([a, b, s])

    result.sort()

    return result


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
