"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/12907
"""

def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1
    for m in money:
        for now in range(m, n + 1):
            if now >= m:
                dp[now] += dp[now - m]

    # print(dp)

    return dp[n] % 1000000007

# 내 풀이_ 개선 중
"""

from collections import Counter,deque,defaultdict
import copy
import heapq

def solution(n, money):
    q=deque([(n,defaultdict(int))])
    result=[]

    while q:
        count,num =q.popleft()

        for i in money:
            if count > i:
                new=copy.deepcopy(num)
                new[i]+=1
                q.append((count-i,new))

            elif count == i:
                new=copy.deepcopy(num)
                new[i]+=1
                if not new in result:
                    result.append(new)


    return len(result)%1000000007
    """

# 내 풀이_개선 중
from collections import Counter, deque


def solution(n, money):
    q = deque([[n, []]])
    result = []

    while q:
        count, num = q.popleft()

        for i in money:
            if count > i:
                q.append([count - i, num + [i]])
            elif count == i:
                if not Counter(num + [i]) in result:
                    result.append(Counter(num + [i]))

    return len(result) % 1000000007

# 다른 사람 풀이
def change(total, coin):
    l = (total+1)*[0]
    ll = coin
    ll.sort()
    for x in ll:
        l[x]+=1
        for i in range(x+1,total+1):
            l[i]+=l[i-x]
    return l[total];