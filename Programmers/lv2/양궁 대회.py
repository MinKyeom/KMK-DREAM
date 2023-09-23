# 내 풀이(개선 중)
def solution(queue1, queue2):
    from collections import deque

    queue1, queue2 = deque(queue1), deque(queue2)

    a, b = sum(queue1), sum(queue2)

    k = a + b

    if k % 2 == 1:
        return -1

    else:
        c = k / 2
        if a == c:
            return 0
    d = (len(queue1) + len(queue2))

    count = 0

    while count <= 2 * d:
        if a < c:
            t = queue2.popleft()
            queue1.append(t)
            a = a + t
            b = b - t
            count += 1

        elif a > c:
            t = queue1.popleft()
            queue2.append(t)
            a = a - t
            b = b + t
            count += 1

        elif a == c:
            return count

    return -1

