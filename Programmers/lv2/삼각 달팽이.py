# 내 풀이
# 처음 배열을 false를 활용한 후 해당 상황에 맞는 값을 false 체크 후 없으면 채워 넣고 삼각형 완성!
def solution(n):
    result = []

    tri = []

    t = int(n * (1 + n) / 2)

    for a in range(1, n + 1):
        k = [False for b in range(a)]
        tri.append(k)

    count = 1
    direction = 0
    # 높이
    high = n
    start = 0  # 아래 대각선 시작 위치
    left = 0  # 왼쪽방향
    right = 0
    while count <= t:
        # 1 아래 대각선
        if direction == 0:
            for a in range(start, n):
                for b in range(left, len(tri[a])):
                    if tri[a][b] == False:
                        tri[a][b] = count
                        count += 1
                        break
                    else:
                        continue
            direction = 1

        # 2 밑변
        elif direction == 1:
            for a in range(len(tri[high - 1])):
                if tri[high - 1][a] == False:
                    tri[high - 1][a] = count
                    count += 1

            high -= 1

            direction = 2

        # 3 오른쪽 대각선
        elif direction == 2:
            for a in range(high - 1, 0, -1):
                for b in range(len(tri[a]) - 1 - right, -1, -1):
                    if tri[a][b] == False:
                        tri[a][b] = count
                        count += 1
                        break
            direction = 0
            start += 2
            left += 1
            right += 1

    for a in range(len(tri)):
        result += tri[a]

    return result

# 다른 사람 풀이
def solution(n):
    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)] # 삼각형 구조 만들기
    x, y = -1, 0 # 좌표 초기화 => 처음 시작은 아래로 내려가기 때문에
    x = -1
    num = 1
    for i in range(n): # 방향
        for j in range(i, n): # 좌표 구하기
            if i % 3 == 0: # 하
                x += 1
            elif i % 3 == 1: # 우
                y += 1
            else: # 상
                x -= 1
                y -= 1
        answer[x][y] = num
        num += 1
    return sum(answer, [])

# 다른 사람 풀이
import itertools

def snailNext(x,y,d_snail) :
    if d_snail %3 ==0 : # 아래
    x+=1
    elif d_snail %3 ==1 : # 우측
        y+=1
    else :
        x-=1
        y -=1
    return x,y

def solution(n):
    tri_snail = [[0 for k in range(1,i+1)] for i in range(1,n+1) ]
    direct_snail = range(n)  # 0부터 n 까지의 리스트
    x, y= -1, 0
    idx = 1
    for d_snail in direct_snail :  # 0 일때 아래,  1일때 오른쪽, 2일때 위
        for i in range(d_snail, n) :
            x,y = snailNext(x,y,d_snail)
            tri_snail[x][y]= idx
            idx+=1
    return list(itertools.chain(*tri_snail))
