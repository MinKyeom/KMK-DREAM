"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/12938
"""
# 내 풀이
from collections import deque, defaultdict

"""
def solution(n, s):
    if s==1:
        return [-1] 

    result=0
    q=deque([])

    for i in range(s//n,s):
        q.append([i])

    while q:
        k=q.popleft()

        if sum(k)==s and len(k)==n:
            new=1
            for t in k:
                new*=t
            if new>result:
                result=new
                result_set=k

        elif len(k)>=n:
            continue

        else:
            if s-sum(k)==1 and len(k)-1==n:
                new=1
                for t in k:
                    new*=t
                    if new>result:
                        result=new
                        result_set=k+[1]

            elif s-sum(k)==2 and len(k)-1==n:
                k=k+[2]
                new=1
                for t in k:
                    new*=t
                    if new>result:
                        result=new
                        result_set=k
            else:
                for num in range(s//n,s-sum(k)+1):
                    q.append(k+[num])

    return result_set
    """


def solution(n, s):
    if n > s:
        return [-1]

    if s % n == 0:
        return [s // n] * n

    else:
        k = s % n
        one = [s // n + 1] * k
        two = [s // n] * (n - k)
        result = two + one

    return result

# 내 풀이_개선 중
from collections import deque


def solution(n, s):
    if s == 1:
        return [-1]

    result = 0

    result_set = []

    num = int(s ** 0.5)
    print(num)

    for i in range(1, num + 1):
        if (s / i) == int(s / i):
            if int(s / i) * i > result:
                result = (s / i) * i
                result_set = {i, int(s / i)}

    print(result_set)

    return 0