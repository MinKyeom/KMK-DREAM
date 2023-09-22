# 내 풀이
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

# 다른 사람 풀이
def solution(que1, que2):
    queSum = (sum(que1) + sum(que2))
    if queSum % 2:
        return -1
    target = queSum // 2

    n = len(que1)
    start = 0
    end = n - 1
    ans = 0

    cur = sum(que1)
    que3 = que1 + que2
    while cur != target:
        if cur < target:
            end += 1
            if end == n * 2:
                return -1
            cur += que3[end]
        else:
            cur -= que3[start]
            start += 1
        ans += 1
    return ans

# 다른 사람 풀이
def solution(queue1, queue2):
    indicator2=sum(queue1)-int(sum(queue1+queue2)/2)
    answer=0
    sub_list=(queue1+queue2+queue1)[::-1]
    add_list=(queue2+queue1+queue2)[::-1]
    while indicator2!=0:
        try:
            if indicator2>0:
                indicator2-=sub_list.pop()
            else:
                indicator2+=add_list.pop()
        except:
            return -1
        answer+=1
    return answer