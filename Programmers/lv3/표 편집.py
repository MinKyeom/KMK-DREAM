"""
출처: 프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/81303
"""

# 내 풀이
"""
# 비슷한 문제 존재 연관짓기 think
# 조건

"U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.

"D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.

"C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.

"Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.(되돌리기)


# 제시된 조건:
 n:처음 행의 개수 
 k:처음 시작할 행의 위치

 # 목표:삭제된 행 아닌 행 구분

 # 생각방향: 링크드리스트 > 빈 곳을 일일이 방금 안해도 된다!
 딕셔너리의 각각의 수는 고유명사로 봐줘야한다
"""

def solution(n, k, cmd):
    result = ["O"] * n

    # 이전 존재,이후 존재
    linked_list = {i: [i - 1, i + 1] for i in range(n)}

    # 현 위치
    progress = k

    backup = []

    for command in cmd:

        # 삭제
        if command == "C":

            # 현재 항 바꾸기
            result[progress] = "X"

            before = linked_list[progress][0]
            after = linked_list[progress][1]

            # 백업 기록
            backup.append((before, progress, after))

            # 현 위치 변경: 다음 위치가 마지막을 넘어가는 경우
            if after == n:
                progress = before
            else:
                progress = after

            # linked_list 변경: 이어주기
            if before == -1:
                linked_list[after][0] = before
            elif after == n:
                linked_list[before][1] = after
            else:
                linked_list[before][1] = after
                linked_list[after][0] = before

        # 되돌리기
        elif command == "Z":
            z_before, z_now, z_after = backup.pop()

            result[z_now] = "O"

            if z_before == -1:
                linked_list[z_after][0] = z_now

            elif z_after == n:
                linked_list[z_before][1] = z_now

            else:
                linked_list[z_after][0] = z_now
                linked_list[z_before][1] = z_now

        # 위치 변경
        else:
            c = command.split(" ")

            if c[0] == "U":
                count = int(c[1])

                for num in range(count):
                    progress = linked_list[progress][0]

            else:
                count = int(c[1])

                for num in range(count):
                    progress = linked_list[progress][1]

    return "".join(result)


# 내 풀이(개선 중)
"""
# 비슷한 문제 존재 연관짓기 think
# 조건

"U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.

"D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.

"C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.

"Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.(되돌리기)


# 제시된 조건:
 n:처음 행의 개수 
 k:처음 시작할 행의 위치

 # 목표:삭제된 행 아닌 행 구분
 
 # 자료구조 링크드인리스트 활용 생각해보기! 
"""
from collections import deque


def solution(n, k, cmd):
    check = [i for i in range(n)]
    backup = []

    # 진행도
    progress = k

    for command in cmd:
        c = command.split(" ")

        if c[0] == "U":

            count = int(c[1])
            progress = max(0, progress - count)

        elif c[0] == "D":
            count = int(c[1])
            progress = min(len(check) - 1, progress + count)

        elif c[0] == "C":
            new = check[progress]
            backup.append(new)

            del check[progress]

            progress = min(progress, len(check) - 1)

        elif c[0] == "Z":
            add = backup.pop()

            before = check[progress]

            check = deque(check)

            new_check = []

            while check:
                num = check.popleft()
                if num > add:
                    new_check.append(add)
                    new_check.append(num)
                    break
                else:
                    new_check.append(num)
            else:
                new_check.append(add)

            check = list(check)

            check = new_check + check

            progress = check.index(before)

    result = ["X"] * n

    for r in check:
        result[r] = "O"

    return "".join(result)


# 내 풀이 (개선 중)
"""
# 비슷한 문제 존재 연관짓기 think
# 조건

"U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.

"D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.

"C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.

"Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.(되돌리기)


# 제시된 조건:
 n:처음 행의 개수 
 k:처음 시작할 행의 위치

 # 목표:삭제된 행 아닌 행 구분
"""
from collections


def solution(n, k, cmd):
    def solution(n, k, cmd):
        # 변경 할 표
        end = [i for i in range(n)]

        result = ["O"] * n

        # 지워질 경우 되돌릴 것
        backup = []

        progress = k

        for command in cmd:

            c = command

            if c[0] == "U":
                count = int(c[2])

                while count > 0 and progress > 0:
                    if end[progress - 1] == "O":
                        progress -= 1
                        count -= 1
                    else:
                        progress -= 1

            elif c[0] == "D":
                count = int(c[2])

                while count > 0 and progress < len(end) - 1:
                    if end[progress + 1] == "O":
                        progress += 1
                        count -= 1
                    else:
                        progress += 1

            elif c[0] == "C":
                backup.append(progress)

                # 맨 마지막 행일 경우
                if progress == len(end) - 1:
                    end[progress] = "X"
                    progress -= 1

                else:
                    end[progress] = "X"
                    progress += 1

            elif c[0] == "Z":
                z = backup.pop()
                end[z] = "O"

        return "".join(end)

        return 0


# 내 풀이(개선 중)_시간 초과
"""
# 비슷한 문제 존재 연관짓기 think
# 조건

"U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.

"D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.

"C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.

"Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.(되돌리기)


# 제시된 조건:
 n:처음 행의 개수 
 k:처음 시작할 행의 위치

 # 목표:삭제된 행 아닌 행 구분
"""


# sol1

def solution(n, k, cmd):
    # 시작 표
    # start=[i for i in range(n)]

    # 변경 할 표
    end = [j for j in range(n)]

    # 중간에 담을 표
    # middle=[t for t in range(n)]

    # 지워질 경우 되돌릴 것
    backup = []

    progress = k

    for command in cmd:
        # c=command.split(" ")
        c = command

        if c[0] == "U":
            count = int(c[2])

            # 비어있는 경우
            if len(end) == 0:
                continue

            if progress - count >= 0:
                progress -= count
            else:
                progress = 0

        elif c[0] == "D":
            count = int(c[2])
            if len(end) == 0:
                continue

            if progress + count < len(end):
                progress += count

            else:
                progress = len(end) - 1

        elif c[0] == "C":
            # 리스트 형태가 아니라 new 안바뀜
            new = end[progress]
            # middle[new]="null"

            backup.append(new)

            # 맨 마지막 행일 경우
            if progress == len(end) - 1:
                del end[progress]
                progress -= 1

            else:
                del end[progress]

        elif c[0] == "Z":
            # 최근에 삭제된 자료
            now = end[progress]
            new = backup.pop()

            # middle[new]=new

            #             e=[]

            #             for re in middle:
            #                 if re!="null":
            #                     e.append(re)

            # end=e

            end.append(new)
            end.sort()

            # 현재 위치 그대로
            progress = end.index(now)

    # print(middle)

    result = ["X"] * n

    for r in end:
        result[r] = "O"

    return "".join(result)


# sol2
"""
def solution(n, k, cmd):
    check=[i for i range(n)]

    p=k

    # 백업 리스트
    b=[]

    for command in cmd:
        c=command.split(" ")

        if c[0]=="U":
            count=c[1]

            while count
            pass
        elif c[0]=="D":

            pass
        elif c[0]=="C":

            pass
        elif c[0]=="Z":

            pass


    return 0
"""

# 다른 사람 풀이
def solution(n, k, cmd):
    cur = k
    table = { i:[i - 1, i + 1] for i in range(n) }
    answer = ['O'] * n
    table[0] = [None, 1]
    table[n - 1] = [n - 2, None]
    stack = []
    for c in cmd:
        if c == "C":
            # 삭제
            answer[cur] = 'X'
            prev, next = table[cur]
            stack.append([prev, cur, next])
            if next == None:
                cur = table[cur][0]
            else:
                cur = table[cur][1]
            if prev == None:
                table[next][0] = None
            elif next == None:
                table[prev][1] = None
            else:
                table[prev][1] = next
                table[next][0] = prev

        elif c == "Z":
            # 복구
            prev, now, next = stack.pop()
            answer[now] = 'O'
            if prev == None:
                table[next][0] = now
            elif next == None:
                table[prev][1] = now
            else:
                table[next][0] = now
                table[prev][1] = now

        else:
            # 커서 이동
            c1, c2 = c.split(' ')
            c2 = int(c2)
            if c1 == 'D':
                for _ in range(c2):
                    cur = table[cur][1]
            else:
                for _ in range(c2):
                    cur = table[cur][0]
    return ''.join(answer)

# 다른 사람 풀이
N = 10**9


class Node:
    # 활성, 비활성
    live = True

    # 이전 노드와 다음 노드
    def __init__(self, p, n):
        self.prev = p if p >= 0 else None
        self.next = n if n < N else None


def solution(n, k, camaand):
    global N
    N = n

    # linked list
    table = {i: Node(i-1, i+1) for i in range(n)}

    # 현재 선택된 행
    now = k

    # 삭제된 번호
    stack = []


    for cmd in camaand:
        # 삭제
        if cmd[0] == 'C':
            # 비활성
            table[now].live = False
            stack.append(now)

            prev, next = table[now].prev, table[now].next

            # 이전 노드가 있다면 현재 노드의 다음 노드와 연결
            if prev is not None:
                table[prev].next = next

            # 다음 노드가 있다면 이전 노드를 다음 노드와 연결
            if next is not None:
                table[next].prev = prev

            # 다음 노드가 없다면 이전 노드 선택, 아니면 다음 노드 선택택
            if table[now].next is None:
                now = table[now].prev
            else:
                now = table[now].next

        # 복구
        elif cmd[0] == 'Z':
            # 활성
            re = stack.pop()
            table[re].live = True

            prev, next = table[re].prev, table[re].next

            # 이전 노드가 있다면 복구 행과 이전노드 연결
            if prev is not None:
                table[prev].next = re

            # 다음 노드가 있다면 복구 행과 다음 노드 연결
            if next is not None:
                table[next].prev = re


        else:
            c, amout = cmd.split()
            # 위
            if c == 'U':
                # 연결된 이전 노드로 계속 변경
                for _ in range(int(amout)):
                    now = table[now].prev

            # 아래
            else:
                # 연결된 다음 노드로 계속 이동
                for _ in range(int(amout)):
                    now = table[now].next

    return ''.join('O' if table[i].live else 'X' for i in range(n))