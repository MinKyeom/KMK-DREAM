# 내 풀이(개선 중)
# 조건: 시계 방향으로만 돌리는거 가능, 한 번당 90도 단 상하좌우도 같이 돌아간다
# 모서리 3개만 돌아감 꼭짓점:2개 돌아감
# 시계 0:12 1:3 2:6 3:9
# 해결 가능한 퍼즐만 주어집니다.

# 목표: 최소한의 횟수로 퍼즐 해결

# 생각방향: 각각의 모든 수는 3번을 초과하지 않는다(제자리로 돌아가기 때문이다)
# 주어진 조건을 봤을 때 완탐으로해도 시간초과 발생 가능성 적음
# for문을 바탕으로 전체를 둘러본 후 주변이 해당 시계를 포함하여 주변이 전부 0이 아닐경우 실행
# 그리고 만약 해당 시계를 바꿨음에도 주변이 모두 0 아닐경우 하나라도 0일 경우 stop
# 완탐의 경우 모든 시계 내 원소가 0 1 2 3 중 하나라는 생각접근
# 각 칸의 돌려지는 횟수가 총합으로 각 칸이 돌려져야 될 횟수를 4로 나눴을때 나머지 횟수랑 동일해야한다.

# 시계 돌리기

# def operation:

#     return check

def solution(clockHands):
    change = [0, 1, 2, 3]
    result = 0
    c = clockHands

    check = c[:]

    row = len(c)
    col = len(c[0])

    #     for i in range(row):
    #         for j in range(col):

    #             if i+1<row and i-1>=0 and j+1<col and j-1>=0:
    #                 if check[i][j]!=0 and check[i+1][j]!=0 and check[i-1][j]!=0 and check[i][j+1]!=0 and check[i][j-1]!=0:
    #                     check=operation(check,i,j)

    #             # 좌상단 꼭짓점
    #             elif i-1<0 and j-1<0:
    #                 pass

    #             # 우상단 꼭짓점
    #             elif i-1<0 and j+1>=col:
    #                 pass

    #             # 좌하단 꼭짓점
    #             elif i+1>=row and j-1<0:
    #                 pass

    #             # 우하단 꼭짓점
    #             elif i+1>=row and j+1>=col:
    #                 pass

    #             # 모서리
    #             else:
    #                 pass

    return result
# 내 풀이(개선 중)

# 조건: 시계 방향으로만 돌리는거 가능, 한 번당 90도 단 상하좌우도 같이 돌아간다
# 모서리 3개만 돌아감 꼭짓점:2개 돌아감
# 시계 0:12 1:3 2:6 3:9
# 해결 가능한 퍼즐만 주어집니다.

# 목표: 최소한의 횟수로 퍼즐 해결

# 생각방향: 각각의 모든 수는 3번을 초과하지 않는다(제자리로 돌아가기 때문이다)
# 주어진 조건을 봤을 때 완탐으로해도 시간초과 발생 가능성 적음
# for문을 바탕으로 전체를 둘러본 후 주변이 해당 시계를 포함하여 주변이 전부 0이 아닐경우 실행
# 그리고 만약 해당 시계를 바꿨음에도 0이 아닐경우 반복 생각
# 완탐의 경우 모든 시계 내 원소가 0 1 2 3 중 하나라는 생각접근

def solution(clockHands):
    change = [0, 1, 2, 3]
    result = 0
    c = clockHands

    check = c[:]

    row = len(c)
    col = len(c[0])

    #     for i in range(row):
    #         for j in range(col):

    #             if i+1<row and i-1>=0 and j+1<col and j-1>=0:
    #                 pass

    #             # 좌상단 꼭짓점
    #             elif i-1<0 and r

    return result