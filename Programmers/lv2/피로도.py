"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/87946
"""
# 플이 과정
def solution(k, dungeons):
    # 목표: 최대 던전 수
    """
    일단 k가 던전 최소 피로도, 소모피로도 보다 클 시 클리어를 전제로 한 후 만약 그보다 좋은 조건의 던전이 나올 시 그것부터 클리어 한 후 다시 최종 추가는 나중에?!
    """
    from collections import deque
    from itertools import permutations

    t = deque(list(permutations(dungeons, len(dungeons))))

    result = []

    dungeons.sort(key=lambda x: (x[1], -x[0]))

    for a in t:
        count = 0
        p = k
        a = deque(list(a))

        while a:
            c = a.popleft()
            if p >= c[0]:
                if p >= c[1]:
                    p -= c[1]
                    count += 1
        result.append(count)

    return max(result)

# 다른 사람 풀이
solution = lambda k, d: max([solution(k - u, d[:i] + d[i+1:]) + 1 for i, (m, u) in enumerate(d) if k >= m] or [0])