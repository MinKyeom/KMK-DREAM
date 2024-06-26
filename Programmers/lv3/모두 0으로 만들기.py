"""
출처: 프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/76503
"""

# 내 풀이(개선 중)
"""

생각방향:
리프노드를 모두 0으로 만든 후의 생각 접근 
핵심 접근 생각 방향 시작:한 곳으로 모으기 생각
#각 점이 간선의 개수가 많은 곳으로 옮기기
#각 점이 간선의 개수가 같다면 가중치가 많은 쪽으로 이동 
#위의 두 개 조차 같다면 번호가 작은쪽으로 

목표:모든 점들의 가중치를 0으로 만들기 

"""
from collections import defaultdict
from collections import deque
import copy


def solution(a, edges):
    # a: 각 점의 가중치를 의미 edges: 간선

    if sum(a) != 0:
        return -1


    else:
        m = defaultdict(list)

        for i, j in edges:
            m[i].append(j)
            m[j].append(i)

        result = 0

        check = copy.deepcopy(edges)

        while check:
            v, w = check.pop()

            # a에서 b로 가중치 옮기기
            if len(m[v]) <= len(m[w]):
                if a[v] >= 0:
                    a[w] -= a[v]
                    result += abs(a[v])
                    a[v] = 0

                else:
                    a[w] += a[v]
                    result += abs(a[v])
                    a[v] = 0
            else:
                if a[w] >= 0:
                    a[v] -= a[w]
                    result += abs(a[w])
                    a[w] = 0

                else:
                    a[v] += a[w]
                    result += abs(a[w])
                    a[w] = 0

            if a[v] != 0 or a[w] != 0:
                check.append([v, w])

        return result


