# 내 풀이
def solution(begin, end):
    road_num = [k for k in range(begin, end + 1)]
    road = [1 for _ in range(begin, end + 1)]

    for i in range(len(road)):
        t = int(road_num[i] ** 0.5)

        if t == 1:
            road[i] == 1
            continue

        check = []

        for j in range(2, t + 1):
            if road_num[i] % j == 0:
                check.append(j)
                if road_num[i] / j <= 10000000:
                    road[i] = road_num[i] // j
                    break
            else:
                continue

        else:
            if len(check) >= 1:
                road[i] = check[-1]

    if begin == 1:
        road[0] = 0

    return road

# 다른 사람 풀이
"""
def get_max_divisor(n:int)->int:
    if n==1:
        return 0

    data=[]

    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            data.append(i)
            if n//i<=10000000:
                return n//i
    if len(data)>=1:
        return data[-1]
    return 1

def solution(begin, end):
    answer = []

    for i in range(begin,end+1):#O(5000)
        # 약수 중에서 자기 자신을 제외한 최대 약수를 구한다.
        max_divisor=get_max_divisor(i)
        answer.append(max_divisor)

    return answer
"""