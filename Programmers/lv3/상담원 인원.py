# 내 풀이
# 추가 고민 포인트
# 왜 상담사 추가 기준이 완탐으로 구현하는지 여부 확인
# 대기 시간이 긴 순서로 상담사를 구현시 틀린 테케 발생!!!
# 완탐 구현시에도 시간 초과 발생x인 이유:상대적으로 적은 수의 상담수의 범위와 유형범위

from collections import deque
import heapq

"""
def find_bestnum(s,k,reqs,g,check):
    result=float("inf") # 무한대로 설정

    for i in range(len(s)):
        if s[i]==g:
            check[i]+=1

        #끝나는 시간 초기화
            for i in range(k):
                finish[i+1]=[]

        # 유형별 대기시간 초기화 
            new_s=[0 for _ in range(k)] 

        # finish[c][0]:가장 빨리 끝나는 시간 finish[c][-1]:가장 늦게 끝나는 시간

        #대기시간 재체크 
            for a,b,c in reqs:
                if len(finish[c])==0:
                    finish[c]=[a+b]
                    continue
            #상담 끝나는 시간, 시작 시간 비교
                if finish[c][0]>a:
                    #상담사 인원이 남은 경우 
                    if len(finish[c])<check[c-1]:
                        heapq.heappush(finish[c],a+b)
                    else:
                        new_s[c-1]+=abs(finish[c][0]-a)
                        num=finish[c][0]
                        heapq.heappop(finish[c])
                        heapq.heappush(finish[c],num+b)
                else:
                    heapq.heappop(finish[c])
                    heapq.heappush(finish[c],a+b)

            if sum(new_s)<result:
                best=i
                result=sum(new_s)
                #원래대로 만들기
                check[i]-=1    
    return best
"""


def solution(k, n, reqs):
    # n:멘토 k:상담 유형
    # 목표: 기다린 시간 최소
    # [a,b,c] a~b분, c 유형
    # point:유형별 상담사 수

    result = []

    # 유형별 상담 대기인원
    check = [1 for _ in range(k)]
    n = n - k
    # 유형별 멘토 최소 1명이상

    # 유형별 종료시간 체크, 상담사 수에 따라 가장 min값으로 최대로 빨리 끝나는 시간
    finish = {}

    # 유형별 대기시간
    s = [0 for _ in range(k)]

    # int로 dic 설정하는 방법 체크!
    for i in range(k):
        if not i + 1 in finish:
            finish[i + 1] = []

    for a, b, c in reqs:
        if len(finish[c]) == 0:
            finish[c] = [a + b]
            continue

        # 상담 끝나는 시간, 시작 시간 비교
        if finish[c][0] > a:
            # 상담사 인원이 남은 경우
            if len(finish[c]) < check[c - 1]:
                heapq.heappush(finish[c], a + b)
            else:
                s[c - 1] += abs(finish[c][0] - a)
                num = finish[c][0]
                heapq.heappop(finish[c])
                heapq.heappush(finish[c], num + b)
        else:
            heapq.heappop(finish[c])
            heapq.heappush(finish[c], a + b)

    # 대기 시간이 큰 순서로 하나씩 상담사 배치 남은 상담사가 0명이 될 때까지!

    while n >= 1:
        f = s.index(max(s))
        g = max(s)

        # 부족한 생각!
        # 대기할 시간이 동일한 유형에 대한 처리 생각!!!
        # 추가할 유형의 상담사 번호:f+1
        """
        if s.count(g)>1:
            f=find_bestnum(s,k,reqs,g,check)
            """
        # 매 순간 가장 상담원 추가를 위해 전체 for문 고려
        # check[f]+=1
        # n-=1
        result = float("inf")

        for f in range(len(check)):
            check[f] += 1

            # 끝나는 시간 초기화
            for i in range(k):
                finish[i + 1] = []

            # 유형별 대기시간 초기화
            s = [0 for _ in range(k)]

            # finish[c][0]:가장 빨리 끝나는 시간 finish[c][-1]:가장 늦게 끝나는 시간

            # 대기시간 재체크
            for a, b, c in reqs:
                if len(finish[c]) == 0:
                    finish[c] = [a + b]
                    continue
                # 상담 끝나는 시간, 시작 시간 비교
                if finish[c][0] > a:
                    # 상담사 인원이 남은 경우
                    if len(finish[c]) < check[c - 1]:
                        heapq.heappush(finish[c], a + b)
                    else:
                        s[c - 1] += abs(finish[c][0] - a)
                        num = finish[c][0]
                        heapq.heappop(finish[c])
                        heapq.heappush(finish[c], num + b)
                else:
                    heapq.heappop(finish[c])
                    heapq.heappush(finish[c], a + b)

            if sum(s) < result:
                result = sum(s)
                best = f
            # 상담사 수 초기화
            check[f] -= 1

        else:
            n -= 1
            check[best] += 1

            if n == 0:
                return result

        # print(finish,"finish")
        # print(check,"상담사 수")
        # print(s,"유형별 기다린 시간")

    return sum(s)

# 다른 사람 풀이
from heapq import heappush, heappop

def solution(k, n, reqs):

    max_n = n - k
    wait_k = []
    map_k_reqs = {}
    wait_init = 0
    wait_diff = []

    for k_ in range(k):
        map_k_reqs[k_] = []

    for r in reqs:
        map_k_reqs[r[2] - 1].append(r[:2])

    for k_ in range(k):
        wait_k_ = 0

        for n_ in range(max_n + 1):
            heap_n = []
            wait_time = 0

            for _ in range(n_ + 1):
                heappush(heap_n, 0)

            for req in map_k_reqs[k_]:
                min_time = heappop(heap_n)

                if min_time <= req[0]:
                    heappush(heap_n, req[0] + req[1])
                else:
                    wait_time += min_time - req[0]
                    heappush(heap_n, min_time + req[1])

            if n_ == 0:
                wait_init += wait_time
            else:
                heappush(wait_diff, wait_time - wait_k_)

            wait_k_ = wait_time

    wait_min = wait_init

    for _ in range(max_n):
        wait_min += heappop(wait_diff)

    return wait_min