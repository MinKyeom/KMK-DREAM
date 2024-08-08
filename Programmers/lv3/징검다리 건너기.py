"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/64062
"""

# 내 풀이(개선 중)
"""
돌 연결 > 링크드리스트 접근 생각 한 번 해보기 다음 돌 체크하는 방향에서 생각 접근
이유: 왜 밟을 필요가 없어진 돌을 굳이 매 번 일일이 확인해야 할까? > 그렇다면 제거 후 이전과 연결 > 링크드리스트
"""
"""
def solution(stones, k):
    # 건넌 사람 수 
    result=0

    # 사람이 건널 돌 위치
    location=0

    # 건너 뛴 돌 개수
    count=0
    new=[]
    person=float("inf")
    while True:
        # 건너 뛸 수 있는 위치안에 돌 횟수가 있을 경우 
        if stones[location+count]>0:
            #stones[location+count]-=1
            person=min(person,stones[location+count])
            new.append(location+count)
            location+=(count+1)
            count=0

            if location>=len(stones):
                for i in new:
                    stones[i]-=person
                result+=person
                new=[]
                person=float("inf")
                location=0
                count=0

        elif location+count>=len(stones):
                for i in new:
                    stones[i]-=person
                result+=person

                new=[]
                person=float("inf")
                location=0
                count=0

        else:
            count+=1

            if count>k-1:
                return result

            elif location+count>=len(stones):
                for i in new:
                    stones[i]-=person

                result+=person
                new=[]
                person=float("inf")
                location=0
                count=0

    return 0
"""
from collections import deque
import heapq


def solution(stones, k):
    node = []
    result = 0

    for i in range(len(stones)):
        if stones[i] > 0:
            node.append(i)

    while True:
        location = node[0]

        num = float("inf")

        if location >= k or node[-1] + k < len(stones) - 1:
            return result

        for now in node:
            # now=heapq.heappop(node)

            num = min(num, stones[now])

            if now - location > k:
                return result

            else:
                location = now

        result += num

        new = []

        for i in node:
            if stones[i] - num > 0:
                new.append(i)
                stones[i] -= num
            else:
                stones[i] -= num

        node = []
        node += new

        if len(node) == 0:
            return result

    return 0

# 다른 사람 풀이
def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        temp = stones.copy()
        mid = (left + right) // 2
        cnt = 0
        for t in temp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1

    return left