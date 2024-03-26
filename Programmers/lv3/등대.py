# 내 풀이(개선 중)
# bfs,dfs 동시 활용 방안 고려: 시간 초과 및 순서에 따른 리스트 변경 관련 의문 사항 해결 필요
# 등대: n개 뱃길:n-1개
# 목표: 켜 두어야하는 최소한의 등대 개수
# 한 붓 그리기인줄 알았으나 그 부분에서는 벗어나있다
# 애매하게 기억나는 포인트: 딕셔너리 생성시 리스트 생성으로 하는 라이브러리 체크 (시간복잡도 감소)
# dfs로 한 후 중간에 그것보다 적은 등대 개수로 한 경우가 발생하던가 했을 경우 돌아가 백트래킹 생각해보기

import heapq
from collections import deque


def solution(n, lighthouse):
    m = {}

    l = lighthouse  # 축약

    island = [i + 1 for i in range(n)]

    # 딕션너리 활용해 그래프 형태로 만들기

    for i, j in l:

        if not i in m:
            m[i] = [j]
        else:
            heapq.heappush(m[i], j)
        if not j in m:
            m[j] = [i]
        else:
            heapq.heappush(m[j], i)

    # print(m, "first")

    # 키값내 values내부 정렬 정렬
    for v in m:
        m[v].sort(key=lambda x: -len(m[x]))

    # print(m,"second")

    # 키값을 values 길이에 따라 정렬
    new_m = sorted(m.items(), key=lambda x: -len(x[1]))

    # print(new_m,"third")

    start_len = 0

    result = []

    for start, arrive in new_m:
        q = deque([start])
        check = []
        visit = []
        count = 0

        while q:
            s = q.popleft()

            if len(set(m[s]) - set(check)) > 0:
                if not s in check:
                    visit.append(s)
                    check.append(s)

                check += m[s]
                q = list(q)
                q = deque(m[s])

            if len(set(island) - set(check)) == 0:
                result.append(visit)
                visit = [start]
                break

            count += 1

    print(result)

    return 0

# 내 풀이(개선 중)
# 등대: n개 뱃길:n-1개
# 목표: 켜 두어야하는 최소한의 등대 개수
# 한 붓 그리기인줄 알았으나 그 부분에서는 벗어나있다
# 애매하게 기억나는 포인트: 딕셔너리 생성시 리스트 생성으로 하는 라이브러리 체크 (시간복잡도 감소)

import heapq


def solution(n, lighthouse):
    m = {}

    l = lighthouse  # 축약

    count = 0

    for i, j in l:

        if not i in m:
            m[i] = [j]
        else:
            heapq.heappush(m[i], j)
        if not j in m:
            m[j] = [i]
        else:
            heapq.heappush(m[j], i)

    check = []

    for v in m:
        m[v].sort(key=lambda x: -len(m[x]))

    print(m)

    new_m = sorted(m.items(), key=lambda x: -len(x[1]))

    print(new_m)

    return 0