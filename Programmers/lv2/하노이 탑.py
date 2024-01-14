# 내 풀이(개선 중)
from collections import deque
def solution(n):
    result = []
    top_1 = deque([k for k in range(1, n + 1)])
    top_2 = deque([])
    top_3 = deque([])

    if n == 1:
        return [1, 3]

    elif n == 2:
        return [[1, 2], [1, 3], [2, 3]]

    else:
        if n % 2 == 1:
            a = top_1.popleft()
            top_3.append(a)
            result.append([1, 3])
        else:
            b = top_1.popleft()
            top_2.append(b)
            result.append([1, 2])

        while len(top_3) <= n:
            if len(top_2) == 0 or len(top_3) == 0:
                t = top_1.popleft()
                if len(top_2) == 0:
                    top_2.append(t)
                    result.append([1, 2])
                else:
                    top_3.append(t)
                    result.append([1, 3])

            else:
                if len(top_2) == len(top_3) == 1:
                    if top_2[-1] < top_3[-1]:
                        c = top_2.pop()
                        top3.append(c)
                        result.append([2, 3])
                    else:
                        d = top_3.pop()
                        top2.append(c)
                        result.append([3, 2])

                else:
                    if len(top_2) > len(top_3):
                        sub = []
                        while top_2:
                            e = top_2.pop()

                            if len(sub) == 0:
                                sub.append(e)
                                result.append([2, 1])
                            elif sub[-1] < e and top_3[-1] > e:
                                top_3.append(e)
                                result.append([2, 3])
                            elif sub[-1] < e and top_3[-1] < e:
                                s = sub.pop()
                                top_3.append(s)
                                result.append([1, 3])
                                sub.append(e)
                                result.append([])

    return result

# 다른 사람 풀이

def solution(n):
    answer = hanoi(n, 1, 3, 2)
    return answer


def hanoi(n, start, end, bypass):
    if n == 1:
        return [[start, end]]
    else:
        path = []
        path += hanoi(n - 1, start, bypass, end)
        path += [[start, end]]
        path += hanoi(n - 1, bypass, end, start)

        return path