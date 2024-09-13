"""
출처:프로그래머스

"""
# 내 풀이
from collections import defaultdict

def solution(N, number):
    if N == number:
        return 1

    num = defaultdict(set)
    num[1].add(N)

    for i in range(2, 9):
        num[i].add(int(str(N) * i))
        for j in range(i):
            for a in num[j]:
                for b in num[i - j]:
                    num[i].add(a + b)
                    num[i].add(a - b)
                    num[i].add(a * b)
                    if b != 0:
                        num[i].add(a // b)

        if number in num[i]:
            return i

    return -1

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

# 다른 사람 풀이
def solution(N, number):
    if N == number:
        return 1

    answer = -1
    arr = [set() for _ in range(8)]

    for i in range(len(arr)):
        arr[i].add(int(str(N) * (i + 1)))

    for i in range(1, 8):
        for j in range(i):
            for op1 in arr[j]:
                for op2 in arr[i - j - 1]:
                    arr[i].add(op1 + op2)
                    arr[i].add(op1 - op2)
                    arr[i].add(op1 * op2)
                    if op2 != 0:
                        arr[i].add(op1 // op2)
        if number in arr[i]:
            answer = i + 1
            break

    return answer