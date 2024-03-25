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