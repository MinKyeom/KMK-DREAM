"""
출처:프로그래머스

"""

# 내 풀이(개선 중)
from itertools import product
from collections import deque


def solution(N, number):
    cal = ["", "+", "//", "*", "-"]

    if N == number:
        return 1

    count = 2

    while True:
        start = str(N) * count

        start = list(start)

        cal_set = deque(list(product(cal, repeat=count - 1)))

        min_check = []

        while cal_set:
            num = str(N)
            check = cal_set.popleft()

            for c in range(len(check)):
                num += check[c]
                num += start[c]

            #                 num=deque(list(num))

            #                 while num[0]=="0" or num[0]=="+" or num[0]=="/" or num[0]=="*":
            #                     num.popleft()

            #                 num=str(eval("".join(num)))

            num = eval(num)

            if int(num) == number:
                return count

        count += 1

        if count > 8:
            return -1

    return -1


"""
import heapq

def solution(N, number):
    q=[(0,N)]
    dp=[N]

    new=[]
    check=[]

    while q:
        count,k=q.pop()

        if k==number:
            return count

        else:
            if k>number:
                new.append((count+1,k//N))
                new.append((count+1,k-N))
                check.append(k//N)
                check.append(k-N)

            else:
                if k<0:
                    new.append((count+1,k+N))
                    check.append(k+N)
                else:
                    new.append((count+1,k+N))
                    new.append((count+1,k*N))
                    check.append(k+N)
                    check.append(k*N)

        if len(q)==0:
            new.append((count+1,int(str(N)*(count+1))))
            check.append(int(str(N)*(count+1)))
            q+=new

            print("q",q)

            if min(check)>8:
                return -1

            else:
                new=[]
                check=[]

    return -1
    """