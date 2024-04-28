"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/118669
"""
# 내 풀이(개선 중)
# 조건: 1~n번의 지점: 출입구 ,쉼터, 산봉우리 중 하나
# intensity:휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 의미
# 출입구는 처음 끝 한번씩 산봉우리 한 번 포함하는 다시 원래 출입구로 돌아오는 등산코스 다른 출입구 한 번더 반복 x
# 거리 가중치 최소화를 처음 보고 든 생각 다익스트라 알고리즘
# 출입구와 산봉우리를 제외하면 모두 휴식터로 분류한다

# 지점 수:n 등산로 정보:paths 출입구 정보: gates 산봉우리들 번호:summits
# [intensity 최소로 만드는 산봉우리, 그 때의 intensity] 산봉우리가 여러 개 일시 가장 낮은 번호의 산봉우리

# 목표: intensity가 최소가 되도록 등산 코스 정하기

# 생각 방향 등산로를 만들면서 쉼터,산봉우리 갈 시 intensity 재갱신 후 최대로 된 걸 체크
# dfs로 산을 오른 후 경로에 따라 피로도 중 최대를 재갱신 후 산봉우리 도착과 입구와 출구와 같은 지점을 결고값에 넣은 후
# 그 중 sort 이후 최소 값을 답으로 낸다
# 한 번에 여러 조건을 검증하기 보다 출입구로 다시 돌아오는 경로만 추린 후 (if문이 너무 여러 번 쓰여 오히려 복잡해진다)
# 다시 경로 재정제하는 방향으로 전환
# dfs로 할 시 중복되는 부분들에 대한 리스트 정리 생각 부족
# dfs 사용시 서로 연결 된 경로가 중복된 경우에 대한 개념 정리


from collections import defaultdict
from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

result = []


# m:경로 start:시작 지점 s:산봉우리 i:피로도 top:도착한 산봉우리 g:출입구

def dfs(start, m, q, s, g, d, check):
    global result
    q = deque(q)
    while q:
        a, c, p, count = q.popleft()  # 출발 지점

        for b in m[a[-1]]:

            # 정상 도착
            if b in s and c == False:
                c = b
                count += d[(a[-1], b)]  # 정상은 휴식처 x
                p = max(p, count)
                q.append([a + [b], c, p, count])

                # dfs(b,m,q)

            # 산봉우리 방문 이후 재방문
            elif b in s and c != False:
                continue

            # 처음 입구인 경우
            elif b == start and c != False:
                count += d[(a[-1], b)]
                p = max(count, p)
                result.append([c, p])
                check.append(p)
                # print("a",a,"c",c,"p",p,"count",count)

            # 또다른 출입구 방문
            elif b == start and c == False:
                continue

            elif b != start and b in g:
                continue
            else:
                if len(check) > 0:
                    if a.count(b) <= 1:
                        count += d[(a[-1], b)]
                        p = max(count, p)  # 초기화 전에 피로도 체크
                        count = 0  # 휴게소 도착과 동시에 초기화
                        q.append([a + [b], c, p, count])

                elif a.count(b) <= 1:
                    count += d[(a[-1], b)]
                    p = max(count, p)  # 초기화 전에 피로도 체크
                    count = 0  # 휴게소 도착과 동시에 초기화
                    q.append([a + [b], c, p, count])
        print(q)
    return 0


def solution(n, paths, gates, summits):
    global result

    # 거리
    d = defaultdict(list)
    # 경로
    m = defaultdict(list)

    p = paths  # 경로
    g = gates  # 출입구
    s = summits  # 산봉우리

    # 등산로 별 시간 기록
    for a, b, c in p:
        d[(a, b)] = c
        d[(b, a)] = c
        m[a].append(b)
        m[b].append(a)

    check = []

    # 출입구에 따른 스타트에 따른 경로
    for start in g:
        i = 0  # 피로도

        # 경로, 정상 도착 여부, 최고 누적 피로도, 피로누적
        q = [[[start], False, 0, 0]]

        # m:경로 start:시작 지점 s:산봉우리 i:피로도 top:도착한 산봉우리 g:출입구
        dfs(start, m, q, s, g, d, check)

    # print(result,"result")

    finish = []

    """
    while result:
        k=result.popleft()

        # 정상 도달 여부
        top_flag=False

        tired=0

        count=0 # 누적 피로도 계산

        for i in range(1,len(k)):

            if k[i] in g or k[i] in s:
                count+=d[(k[i-1],k[i])]
                tired=max(tired,count)
            else:
                tired=max(tired,count)
                count=0
                tired=max(tired,d[(k[i-1],k[i])])


            if k[i] in s and top_flag==False:
                top_flag=k[i]

        else:
            if len(finish)==0 and top_flag!=False:
                finish=[top_flag,tired]

            elif len(finish)!=0 and top_flag!=False:
                if finish[1]>=tired:
                    finish=[top_flag,tired]

        """

    return finish

# 내 풀이(개선 중)
# 조건: 1~n번의 지점: 출입구 ,쉼터, 산봉우리 중 하나
# intensity:휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 의미
# 출입구는 처음 끝 한번씩 산봉우리 한 번 포함하는 다시 원래 출입구로 돌아오는 등산코스 다른 출입구 한 번더 반복 x
# 거리 가중치 최소화를 처음 보고 든 생각 다익스트라 알고리즘

# 지점 수:n 등산로 정보:paths 출입구 정보: gates 산봉우리들 번호:summits
# [intensity 최소로 만드는 산봉우리, 그 때의 intensity] 산봉우리가 여러 개 일시 가장 낮은 번호의 산봉우리

# 목표: intensity가 최소가 되도록 등산 코스 정하기

# 생각 방향 등산로를 만들면서 쉼터,산봉우리 갈 시 intensity 재갱신 후 최대로 된 걸 체크
# dfs로 산을 오른 후 경로에 따라 피로도 중 최대를 재갱신 후 산봉우리 도착과 입구와 출구와 같은 지점을 결고값에 넣은 후
# 그 중 sort 이후 최소 값을 답으로 낸다
# 한 번에 여러 조건을 검증하기 보다 출입구로 다시 돌아오는 경로만 추린 후 (if문이 너무 여러 번 쓰여 오히려 복잡해진다)
# 다시 경로 재정제하는 방향으로 전환
# dfs로 할 시 중복되는 부분들에 대한 리스트 정리 생각 부족
# dfs 사용시 서로 연결 된 경로가 중복된 경우에 대한 개념 정리



from collections import defaultdict
from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

result = []


# m:경로 start:시작 지점 s:산봉우리 i:피로도 top:도착한 산봉우리 g:출입구

def dfs(start, m, q, s, g):
    global result

    while q:
        a, c = q.pop()  # 출발 지점
        # m[a]:k에서 연결된 산 경로
        count = 0

        for b in m[a[-1]]:
            if b in s and c == False:
                q.append([a + [b], True])
                # dfs(b,m,q)

            # 산봉우리 방문 이후 재방문
            elif b in s and c == True:
                continue

            # 처음 입구인 경우
            elif b == start and c == True:
                result.append(a + [b])

            # 또다른 출입구 방문
            elif b in g:
                continue

            else:
                if a.count(b) <= 1:
                    q.append([a + [b], c])

    return 0


def solution(n, paths, gates, summits):
    global result

    # 거리
    d = defaultdict(list)
    # 경로
    m = defaultdict(list)

    p = paths  # 경로
    g = gates  # 출입구
    s = summits  # 산봉우리

    # 등산로 별 시간 기록
    for a, b, c in p:
        d[(a, b)] = c
        d[(b, a)] = c
        m[a].append(b)
        m[b].append(a)

    # 출입구에 따른 스타트에 따른 경로
    for start in g:
        i = 0  # 피로도

        q = [[[start], False]]

        # m:경로 start:시작 지점 s:산봉우리 i:피로도 top:도착한 산봉우리 g:출입구
        dfs(start, m, q, s, g)

    result = deque(result)

    finish = []

    check = []

    while result:
        k = result.popleft()

        # 정상 도달 여부
        top_flag = False

        tired = 0

        count = 0  # 누적 피로도 계산

        for i in range(1, len(k)):

            if k[i] in g or k[i] in s:
                count += d[(k[i - 1], k[i])]
                tired = max(tired, count)
            else:
                tired = max(tired, count)
                count = 0
                tired = max(tired, d[(k[i - 1], k[i])])

            if k[i] in s and top_flag == False:
                top_flag = k[i]

        else:
            if len(finish) == 0 and top_flag != False:
                finish = [top_flag, tired]

            elif len(finish) != 0 and top_flag != False:
                if finish[1] >= tired:
                    finish = [top_flag, tired]

    return finish

# 내 풀이(개선 중)
# 조건: 1~n번의 지점: 출입구 ,쉼터, 산봉우리 중 하나
# intensity:휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 의미
# 출입구는 처음 끝 한번씩 산봉우리 한 번 포함하는 다시 원래 출입구로 돌아오는 등산코스 다른 출입구 한 번더 반복 x
# 거리 가중치 최소화를 처음 보고 든 생각 다익스트라 알고리즘

# 지점 수:n 등산로 정보:paths 출입구 정보: gates 산봉우리들 번호:summits
# [intensity 최소로 만드는 산봉우리, 그 때의 intensity] 산봉우리가 여러 개 일시 가장 낮은 번호의 산봉우리

# 목표: intensity가 최소가 되도록 등산 코스 정하기

# 생각 방향 등산로를 만들면서 쉼터,산봉우리 갈 시 intensity 재갱신 후 최대로 된 걸 체크
# dfs로 산을 오른 후 경로에 따라 피로도 중 최대를 재갱신 후 산봉우리 도착과 입구와 출구와 같은 지점을 결고값에 넣은 후
# 그 중 sort 이후 최소 값을 답으로 낸다
# 한 번에 여러 조건을 검증하기 보다 출입구로 다시 돌아오는 경로만 추린 후 (if문이 너무 여러 번 쓰여 오히려 복잡해진다)
# 다시 경로 재정제하는 방향으로 전환
# dfs로 할 시 중복되는 부분들에 대한 리스트 정리 생각 부족
# dfs 사용시 서로 연결 된 경로가 중복된 경우에 대한 개념 정리


from collections import defaultdict
from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

result = []


# m:경로 start:시작 지점 s:산봉우리 i:피로도 top:도착한 산봉우리 g:출입구

def dfs(start, m, v, q):
    global result

    while q:
        a = q.pop()  # 출발 지점
        # m[a]:k에서 연결된 산 경로
        for b in m[a]:
            if not b in v:
                v.append(b)
                q += [b]
                dfs(b, m, v, q)

            elif b == v[0]:
                end = v[:]
                end = end + [v[0]]
                result.append(end)

            print(v)

    return 0


def solution(n, paths, gates, summits):
    global result

    # 거리
    d = defaultdict(list)
    # 경로
    m = defaultdict(list)

    p = paths  # 경로
    g = gates  # 출입구
    s = summits  # 산봉우리

    # 등산로 별 시간 기록
    for a, b, c in p:
        d[(a, b)] = c
        d[(b, a)] = c
        m[a].append(b)
        m[b].append(a)

    # 출입구에 따른 스타트에 따른 경로
    for start in g:
        i = 0  # 피로도
        v = [start]
        q = [start]
        # m:경로 start:시작 지점 s:산봉우리 i:피로도 top:도착한 산봉우리 g:출입구
        dfs(start, m, v, q)

    print(result)

    return 0

# 내 풀이(개선 중)
# 조건: 1~n번의 지점: 출입구 ,쉼터, 산봉우리 중 하나
# intensity:휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 의미
# 출입구는 처음 끝 한번씩 산봉우리 한 번 포함하는 다시 원래 출입구로 돌아오는 등산코스 다른 출입구 한 번더 반복 x
# 거리 가중치 최소화를 처음 보고 든 생각 다익스트라 알고리즘

# 지점 수:n 등산로 정보:paths 출입구 정보: gates 산봉우리들 번호:summits
# [intensity 최소로 만드는 산봉우리, 그 때의 intensity] 산봉우리가 여러 개 일시 가장 낮은 번호의 산봉우리

# 목표: intensity가 최소가 되도록 등산 코스 정하기

# 생각 방향 등산로를 만들면서 쉼터,산봉우리 갈 시 intensity 재갱신 후 최대로 된 걸 체크
# dfs로 산을 오른 후 경로에 따라 피로도 중 최대를 재갱신 후 산봉우리 도착과 입구와 출구와 같은 지점을 결고값에 넣은 후
# 그 중 sort 이후 최소 값을 답으로 낸다
# 한 번에 여러 조건을 검증하기 보다 출입구로 다시 돌아오는 경로만 추린 후 (if문이 너무 여러 번 쓰여 오히려 복잡해진다)
# 다시 경로 재정제하는 방향으로 전환
# 다익스트라 알고리즘으로 생각도 같이 해보기!

from collections import defaultdict
from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

result = []


# m:경로 start:시작 지점 s:산봉우리 i:피로도 top:도착한 산봉우리 g:출입구

def dfs(start, m, v, check):
    global result

    q = deque([start])

    while q:
        a = q.popleft()  # 출발 지점

        # m[a]:k에서 연결된 산 경로
        for b in m[a]:
            if b == v[0]:
                v.append(v[0])
                check += [v]
                v.pop()

            elif not b in v:
                v.append(b)
                dfs(b, m, v, check)

    return 0


def solution(n, paths, gates, summits):
    global result

    # 거리
    d = defaultdict(list)
    # 경로
    m = defaultdict(list)

    p = paths  # 경로
    g = gates  # 출입구
    s = summits  # 산봉우리

    # 등산로 별 시간 기록
    for a, b, c in p:
        d[(a, b)] = c
        d[(b, a)] = c
        m[a].append(b)
        m[b].append(a)

    check = []

    # 출입구에 따른 스타트에 따른 경로
    for start in g:
        i = 0  # 피로도
        v = [start]
        # m:경로 start:시작 지점 s:산봉우리 i:피로도 top:도착한 산봉우리 g:출입구
        dfs(start, m, v, check)

    print(check)

    return 0

# 내 풀이(개선 중)
# 조건: 1~n번의 지점: 출입구 ,쉼터, 산봉우리 중 하나
# intensity:휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 의미
# 출입구는 처음 끝 한번씩 산봉우리 한 번 포함하는 다시 원래 출입구로 돌아오는 등산코스 다른 출입구 한 번더 반복 x
# 거리 가중치 최소화를 처음 보고 든 생각 다익스트라 알고리즘

# 지점 수:n 등산로 정보:paths 출입구 정보: gates 산봉우리들 번호:summits
# [intensity 최소로 만드는 산봉우리, 그 때의 intensity] 산봉우리가 여러 개 일시 가장 낮은 번호의 산봉우리

# 목표: intensity가 최소가 되도록 등산 코스 정하기

# 생각 방향 등산로를 만들면서 쉼터,산봉우리 갈 시 intensity 재갱신 후 최대로 된 걸 체크
# dfs로 산을 오른 후 경로에 따라 피로도 중 최대를 재갱신 후 산봉우리 도착과 입구와 출구와 같은 지점을 결고값에 넣은 후
# 그 중 sort 이후 최소 값을 답으로 낸다
# 한 번에 여러 조건을 검증하기 보다 출입구로 다시 돌아오는 경로만 추린 후 (if문이 너무 여러 번 쓰여 오히려 복잡해진다)
# 다시 경로 재정제하는 방향으로 전환

from collections import defaultdict
from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

result = []


# m:경로 start:시작 지점 s:산봉우리 i:피로도 top:도착한 산봉우리 g:출입구

def dfs(start, m, v, check):
    global result

    q = deque([start])

    while q:
        a = q.popleft()  # 출발 지점

        # m[a]:k에서 연결된 산 경로
        for b in m[a]:
            if b == v[0]:
                v.append(v[0])
                check += [v]
                v.pop()

            elif not b in v:
                v.append(b)
                dfs(b, m, v, check)

    return 0


def solution(n, paths, gates, summits):
    global result

    # 거리
    d = defaultdict(list)
    # 경로
    m = defaultdict(list)

    p = paths  # 경로
    g = gates  # 출입구
    s = summits  # 산봉우리

    # 등산로 별 시간 기록
    for a, b, c in p:
        d[(a, b)] = c
        d[(b, a)] = c
        m[a].append(b)
        m[b].append(a)

    check = []

    # 출입구에 따른 스타트에 따른 경로
    for start in g:
        i = 0  # 피로도
        v = [start]
        # m:경로 start:시작 지점 s:산봉우리 i:피로도 top:도착한 산봉우리 g:출입구
        dfs(start, m, v, check)

    print(check)

    return 0

# 내 풀이(생각 방향 정리)
# 조건: 1~n번의 지점: 출입구 ,쉼터, 산봉우리 중 하나
# intensity:휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 의미
# 출입구는 처음 끝 한번씩 산봉우리 한 번 포함하는 다시 원래 출입구로 돌아오는 등산코스 다른 출입구 한 번더 반복 x
# 거리 가중치 최소화를 처음 보고 든 생각 다익스트라 알고리즘

# 지점 수:n 등산로 정보:paths 출입구 정보: gates 산봉우리들 번호:summits
# [intensity 최소로 만드는 산봉우리, 그 때의 intensity] 산봉우리가 여러 개 일시 가장 낮은 번호의 산봉우리

# 목표: intensity가 최소가 되도록 등산 코스 정하기

# 생각 방향 등산로를 만들면서 쉼터,산봉우리 갈 시 intensity 재갱신 후 최대로 된 걸 체크

from collections import defaultdict


def solution(n, paths, gates, summits):
    map = defaultdict(list)
    print(map)

    answer = []
    return answer