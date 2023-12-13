# 내 풀이
# 숫자가 클수록 우선순위가 높다!
from collections import deque


def solution(priorities, location):
    result = 0  # 실행 순서

    p = deque(priorities)

    l = location

    finish_num = p[l]

    p[l] = 0

    while True:
        q = p.popleft()

        if q == 0:

            if len(p) == 0:
                return result + 1

            else:
                if finish_num >= max(p):
                    return result + 1
                else:
                    p.append(q)

        else:
            if q >= max(p) and q >= finish_num:
                result += 1
            else:
                p.append(q)


# 다른 사람 풀이
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer