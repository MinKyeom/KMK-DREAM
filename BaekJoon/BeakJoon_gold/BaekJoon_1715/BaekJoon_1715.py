"""
처음 틀린 풀이 과정
import heapq
n=int(input("카드 묶음을 입력하세요:"))
list = []
list_1 = []
count=0
for cardlist in range(n):
    x=int(input())
    list.append(x)
    print(list[cardlist])
    print()

    heapq.heapify(list)
    list_1[0] = heapq.heappop(list)
    heapq.heapify(list)
    list_1[1] = heapq.heappop(list)
    count += (list_1[0]+list_1[1])*n

    for a in range(n-1):
        heapq.heapify(list)
        list_1[a+2]=heapq.heappop(list)
        count+=(list_1[a+2])*(n-a+1)


print(count)
위의 문장까지 내 풀이
"""

import sys
import heapq

input = sys.stdin.readline

n = int(input())

cards = []

for i in range(n):
    heapq.heappush(cards, int(input()))

result = 0

if len(cards) == 1:
    print(result)

else:
    for i in range(n - 1):
        previous = heapq.heappop(cards)
        current = heapq.heappop(cards)

        result += previous + current
        heapq.heappush(cards, previous + current)

    print(result)
"""
배운점: 
문제의 기본적인 아이디어를 잘 생각해봐야한다

이 문제의 경우도 매 번 두 묶음 카드를 비교한 것이다. 단지 가장 작은거부터 
더해서 비교가 아니라 매 번 제일 작은 두 뭉치의 카드를 비교하는것이다. 더해진 카드 뭉치 
포함!



의문점: 
n의값의 범위는 if문에 왜 넣지 않는가?여부와
int(input:)으로 받을경우 string으로 입력시 오류 발생하는 처리를 하지 않는가
"""

"""

heapq.heapop을통해 반환시에 새로운 [0]위치에는 그 리스트의 최솟값이 온다! 
그걸 통해 heapq.heapify를 통해 재정렬을 반복해줄 필요가 없었다.

"""




