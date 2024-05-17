"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/92344
"""

# 내 풀이 (개선 중)

"""

조건:행:m 열:n
적군 내구도가 0으로 되면 파괴
아군 내구도를 높임
타입1:적 타입2:아군

특이점:파괴된 건물도 공격받으면 내구도가 더 하락한다!

목표:파괴되지 않은 건물의 개수를 구하시오

생각방향:skill의 조건을 감안하면 skill의 한 번의 루프로 board를 구성하는 방향성에서 생각해보기
중복되는 면적에 대한 생각 사고
"""


def solution(board, skill):
    # 행
    m = len(board)

    # 열
    n = len(board[0])

    result = 0

    check = [[0] * n for _ in range(m)]

    # team: 아군 enemy: 적
    """
    for s in skill:
        ax,ay=s[1],s[2]
        bx,by=s[3],s[4]
        c=s[5]

        # 적
        if s[0]==1:
            for x in range(ax,bx+1):
                for y in range(ay,by+1):
                    before=board[x][y]
                    board[x][y]-=c
                    after=board[x][y]

                    if before>0 and after<=0:
                        result-=1               
        # 아군
        else:
            for x in range(ax,bx+1):
                for y in range(ay,by+1):
                    before=board[x][y]
                    board[x][y]+=c
                    after=board[x][y]

                    if before<=0 and after>0:
                        result+=1

        """
    for s in skill:
        if s[0] == 1:
            for x in range(s[1], s[3] + 1):
                for y in range(s[2], s[4] + 1):
                    check[x][y] -= s[5]

        else:
            for x in range(s[1], s[3] + 1):
                for y in range(s[2], s[4] + 1):
                    check[x][y] += s[5]

    for i in range(m):
        for j in range(n):
            board[i][j] += check[i][j]
            if board[i][j] > 0:
                result += 1
    return result