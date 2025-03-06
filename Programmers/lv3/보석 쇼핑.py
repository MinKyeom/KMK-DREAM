"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/67258
"""
# 풀이 과정
"""
투포인터
"""

import heapq
from collections import defaultdict
from collections import deque
from collections import Counter


def solution(gems):
    # 종류
    check = len(set(gems))

    start, end = 0, 0

    my = defaultdict(int)

    result = float("inf")
    result_start, result_end = float("inf"), float("inf")

    my[gems[start]] += 1

    while start <= len(gems) - 1:
        if len(my) != check:
            if end < len(gems) - 1:
                end += 1
                my[gems[end]] += 1
            else:
                break
        else:
            if end - start < result:
                result = end - start
                result_start, result_end = start, end

            if start == end:
                return [start + 1, end + 1]

            else:
                my[gems[start]] -= 1

                if my[gems[start]] == 0:
                    del my[gems[start]]

                start += 1

    # 마지막
    if not result_start <= len(gems) and not result_end <= len(gems):
        return [1, len(gems)]

    return [result_start + 1, result_end + 1]

# 내 풀이(개선 중)
"""
이진탐색 
"""

import heapq
from collections import defaultdict
from collections import deque


def solution(gems):
    j = set(gems)
    check = defaultdict(int)

    for i in j:
        check[i] = 0

    heap = []

    new = deque([])
    start, end = 0, 0

    new.append(gems[start])

    while start < len(gems) - 1 and end <= len(gems) - 1:

        if len(j - set(new)) == 0:
            heapq.heappush(heap, (end - start, start, end))

            if start == end:
                end += 1
                new.append(gems[end])

            else:
                start += 1
                new.popleft()

        else:
            end += 1
            if end >= len(gems):
                break
            new.append(gems[end])

    return [heap[0][1] + 1, heap[0][2] + 1]

# 다른 사람 풀이

def solution(gems):
    answer = [0, len(gems)]
    size = len(set(gems))  # 보석 종류 갯수
    left, right = 0, 0  # left는 보석 빼 줄 포인터, right는 보석 더해 줄 포인터
    gem_dict = {gems[0]: 1}

    while left < len(gems) and right < len(gems):  # 투 포인터가 범위를 벗어나면 무한루프 종료
        # 딕셔너리에 보석 종류가 다 들어오는 경우
        if len(gem_dict) == size:
            if right - left < answer[1] - answer[0]:  # 최소 크기 확인
                answer = [left, right]
            else:
                gem_dict[gems[left]] -= 1
                if gem_dict[gems[left]] == 0:
                    del gem_dict[gems[left]]  # count가 0이 되면 key가 없어야하므로 반드시 del
                left += 1

        else:
            right += 1

            if right == len(gems):
                break

            if gems[right] in gem_dict:  # 딕셔너리 key에 있으면 count
                gem_dict[gems[right]] += 1

            else:  # 없으면 추가
                gem_dict[gems[right]] = 1

    return [answer[0] + 1, answer[1] + 1]  # 시작 인덱스가 1번 진열대 부터 라서 1 증가

