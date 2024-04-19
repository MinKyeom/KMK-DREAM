"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/131129
"""

# 내 풀이(개선 중)
# 점수를 깎아서 0점으로 만듬 단, 남은 점수보다 큰 점수로 득점하면 버스트 후 실격

# 조건:
# 싱글: 해당 점수 더블:해당 점수 2배 트리플: 해당 점수 3배
# 불, 아우터 불: 50점

# 승리 조건: 더 빨리 0점 만든 선수(같은 라운드의 경우 그 중 싱글 또는 불을 더 많이 던진 선수)

# 빨리 0점을 만들면서 싱글 또는 불을 최대한 많이 던지는 방법

# 목표:[다트 던진 횟수,싱글 횟수+불 횟수]

# 생각방향: 무조건 1번에 끝나지 않는 경우 불과 싱글과 함께된 조합으로 동일한 횟수로 해결 가능할 경우 그 경우의 수 조합 생각
# import heapq
from collections import deque


def solution(target):
    t = target

    # 다트판
    d = [k + 1 for k in range(20)]

    # 점수 얻을 수 있는 판
    s = []

    for i in d:
        s.append(i)
        s.append(i * 2)
        s.append(i * 3)
    s.append(50)

    s = list(set(s))

    d.append(50)

    s.sort()

    q = deque([[0, 0, t]])
    result = []
    new = []  # 라운드 별 새로 추가 할 q

    while q:
        # 라운드,(불 또는 싱글),점수
        r, c, t = q.popleft()

        for i in range(len(s) - 1, -1, -1):
            if t >= s[i]:
                # print(s[i],"s[i]")
                if s[i] in d:
                    new.append([r + (t // s[i]), c + (t // s[i]), (t % s[i])])

                    if (t % s[i]) == 0:
                        result.append([r + (t // s[i]), c + (t // s[i])])


                else:
                    new.append([r + (t // s[i]), c, t % s[i]])

                    if (t % s[i]) == 0:
                        result.append([r + (t // s[i]), c])

        if len(q) == 0:
            q = list(q)
            q += new
            q = deque(q)
            new = []

    result = sorted(result, key=lambda x: (x[0], -x[1]))

    return result[0]