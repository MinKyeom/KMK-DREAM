"""

m명 마다 서버 1대
m명 이하 증설 필요x
n*m <= x <(n+1)*m : n대 서버 필요
k 값에 따라 그 시간 동안만 이용 후 반납 해야한다.
5시간 마다 증설 > 사라짐 heapq 관련 생각 예약 후 빠져나간다는 생각
목표: 증설 횟수 구하기

"""
import heapq


def solution(players, m, k):
    result = 0

    # 서버 최대 수용 인원
    max_people = 0

    # 서버 설치 시간, 대수 ,사라지는 시간
    heap = []

    for num, p in enumerate(players):
        # 만료된 서버 제거
        if len(heap) > 0 and heap[0][0] == num:
            make, n = heapq.heappop(heap)
            max_people -= n

            if max_people > p:
                continue

            # 서버 설치를 해야할 경우
            else:
                charge = p - max_people

                if charge / m == charge // m:
                    heapq.heappush(heap, (num + k, charge))
                    max_people += p
                    result += charge

                else:
                    heapq.heappush(heap, (num + k, (m + 1) * (charge // m)))
                    max_people += (m + 1) * (charge // m)
                    result += (m + 1) * (charge // m)

        elif len(heap) == 0 and p > 0:
            nessary = p / m

            if p / m == p // m:
                heapq.heappush(heap, (num + k, p))
                max_people += p

            else:
                heapq.heappush(heap, (num + k, (m + 1) * (p // m)))
                max_people += (m + 1) * (p // m)

    print(result)

    answer = 0
    return answer