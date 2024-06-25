"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/77486
"""
# 내 풀이
"""

생각방향:등비급수처럼 리스트를 만든 후 맨 위에 지속적으로 더해주는 형태

목표:enroll에 적힌 판매원들의 수익을 출력
"""

from collections import defaultdict
import math

# 판매원 수익 명단 dic
check = []
name = []


# 추천인 분배
def divide(e, r, n, p):
    global check, name

    # 1원 미만으로 분배금이 떨어질 경우 분배금 발생 x
    while n >= 1:

        # 등록자 번호 위치
        k = name[p]

        # 추천인이 없는 경우
        if r[k] == "-":
            break

        # 추천인이 있는 경우
        else:
            check[r[k]] += math.ceil(n * (0.9))

            n = int(n * (0.1))

            # 더 위의 상위순번 추천자 시작
            p = r[k]

    return 0


def solution(enroll, referral, seller, amount):
    global check, name

    check = defaultdict(int)

    name = defaultdict(int)

    for i, j in enumerate(enroll):
        check[j] = 0
        name[j] = i

    # 구성원
    e = enroll

    # 추천인 찾기
    r = referral

    # 판매 집계 데이터의 판매원 이름
    s = seller

    # 판매 집계 데이터
    a = amount

    for i in range(len(a)):
        n = a[i] * 100  # 판매량*단가
        p = s[i]  # 판매원

        # 처음 판매자 수익금 가져가기
        check[p] += math.ceil((0.9) * (n))

        # 분배할 금액
        n = int(n * (0.1))

        # 구성원 명단,추천인 명단,남은 분배금액, 최초 판매자
        divide(e, r, n, p)

    result = []

    for f in enroll:
        result.append(check[f])

    return result


# 다른 사람 풀이
def solution(enroll, referral, seller, amount):
    graph,ans = {},{e:0 for e in enroll}

    for e,r in zip(enroll,referral): graph[e]=r

    for s,a in zip(seller,amount):
        money = a*100
        rate = money//10
        ans[s] += money-rate
        x = graph[s]

        while x != "-":
            if rate==0: break
            ans[x] += rate-rate//10
            rate//=10
            x = graph[x]

    return list(ans.values())