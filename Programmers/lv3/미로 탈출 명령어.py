# 내 풀이
# 같은 곳을 두 번 방문할 수 있다
# 거리가 k로 고정
# bfs 같은 곳 방문 여러번 가능 단 거리는 k여야 한다
# dx dy [1,0]은 아래로 가는 것이다 위x 격자 미로에서 상상해야 한다

# 시간 초과 발생: 길이가 k가 되는 것들을 모아 다시 도착 지점에 있는지 확인 하는 방법 생각해보고 접근해보기!
# d,l,r,u
# ddd 다음 ddl ddr 이런 방향성에서 생각해보기 dfs로 접근도 생각해보기 bfs가 아닌

# 먼저 갈 방향성이 정해져 있다는 사실 인지 후 풀이 재구성

from collections import deque


def solution(n, m, x, y, r, c, k):
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]

    # s=[x,y] # 출발 지점
    # d=[r,c] # 도착 지점
    # n*m 격자

    result = ""

    while True:
        if 1 <= x + 1 <= n and abs(x + 1 - r) + abs(y - c) + len(result) + 1 <= k:
            result = result + "d"
            x += 1
        elif 1 <= y - 1 <= m and abs(x - r) + abs(y - 1 - c) + len(result) + 1 <= k:
            result = result + "l"
            y -= 1
        elif 1 <= y + 1 <= m and abs(x - r) + abs(y + 1 - c) + len(result) + 1 <= k:
            result = result + "r"
            y += 1
        elif 1 <= x - 1 <= n and abs(x - 1 - r) + abs(y - c) + len(result) + 1 <= k:
            result = result + "u"
            x -= 1
        else:
            return "impossible"

        # len(result)==k
        if len(result) == k:
            if x == r and y == c:
                return result
            else:
                return "impossible"

    # return result if flag==False else "impossible"

# 내 풀이(개선 중)
# 같은 곳을 두 번 방문할 수 있다
# 거리가 k로 고정
# bfs 같은 곳 방문 여러번 가능 단 거리는 k여야 한다
# dx dy [1,0]은 아래로 가는 것이다 위x 격자 미로에서 상상해야 한다

# 시간 초과 발생: 길이가 k가 되는 것들을 모아 다시 도착 지점에 있는지 확인 하는 방법 생각해보고 접근해보기!
# d,l,r,u
# ddd 다음 ddl ddr 이런 방향성에서 생각해보기 dfs로 접근도 생각해보기 bfs가 아닌

from collections import deque


def solution(n, m, x, y, r, c, k):
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]

    # s=[x,y] # 출발 지점
    # d=[r,c] # 도착 지점

    result = []

    q = deque([["", [x, y]]])

    while q:
        i = q.popleft()
        # print(i,"len(I)",len(i),"[r,c]",[r,c])
        if abs(i[-1][0] - r) + abs(i[-1][1] - c) + len(i[0]) > k:
            continue
        if len(i[0]) == k and i[-1] == [r, c]:
            i.pop()
            # print(i)
            # i.sort()
            # final="".join(i)
            # print(final)
            # result.append(final)
            result.append(i[0])
        elif len(i[0]) == k and i[-1] != [r, c]:
            continue

        else:
            v = i[-1][0]
            w = i[-1][1]
            i.pop()  # 맨 뒤 리스트 제거
            for a, b in zip(dx, dy):
                new = ""
                if 1 <= v + a <= n and 1 <= w + b <= m:
                    if a == 1 and b == 0:
                        new += str(i[0])
                        new += "d"
                        q += [[new, [v + a, w + b]]]

                    elif a == -1 and b == 0:
                        new += str(i[0])
                        new += "u"
                        q += [[new, [v + a, w + b]]]

                    elif a == 0 and b == 1:
                        new += str(i[0])
                        new += "r"
                        q += [[new, [v + a, w + b]]]

                    elif a == 0 and b == -1:
                        new += str(i[0])
                        new += "l"
                        q += [[new, [v + a, w + b]]]

    result.sort()

    return result[0] if len(result) > 0 else "impossible"

# 내 풀이(개선 중)
# 같은 곳을 두 번 방문할 수 있다
# 거리가 k로 고정
# bfs 같은 곳 방문 여러번 가능 단 거리는 k여야 한다
# dx dy [1,0]은 아래로 가는 것이다 위x 격자 미로에서 상상해야 한다

# 시간 초과 발생: 길이가 k가 되는 것들을 모아 다시 도착 지점에 있는지 확인 하는 방법 생각해보고 접근해보기!
from collections import deque


def solution(n, m, x, y, r, c, k):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # s=[x,y] # 출발 지점
    # d=[r,c] # 도착 지점

    result = []

    q = deque([["", [x, y]]])

    while q:
        i = q.popleft()
        # print(i,"len(I)",len(i),"[r,c]",[r,c])
        if abs(i[-1][0] - r) + abs(i[-1][1] - c) + len(i[0]) > k:
            continue
        if len(i[0]) == k and i[-1] == [r, c]:
            i.pop()
            # print(i)
            # i.sort()
            # final="".join(i)
            # print(final)
            # result.append(final)
            result.append(i[0])
        elif len(i[0]) == k and i[-1] != [r, c]:
            continue

        else:
            v = i[-1][0]
            w = i[-1][1]
            i.pop()  # 맨 뒤 리스트 제거
            for a, b in zip(dx, dy):
                new = ""
                if 1 <= v + a <= n and 1 <= w + b <= m:
                    if a == 1 and b == 0:
                        new += str(i[0])
                        new += "d"
                        q += [[new, [v + a, w + b]]]
                    elif a == -1 and b == 0:
                        new += str(i[0])
                        new += "u"
                        q += [[new, [v + a, w + b]]]
                    elif a == 0 and b == 1:
                        new += str(i[0])
                        new += "r"
                        q += [[new, [v + a, w + b]]]
                    elif a == 0 and b == -1:
                        new += str(i[0])
                        new += "l"
                        q += [[new, [v + a, w + b]]]

    result.sort()

    return result[0] if len(result) > 0 else "impossible"

# 다른 사람 풀이
def solution(n, m, x, y, r, c, k):
    answer = ''
    #x,y -> r,c
    #좌상단이 1,1/ 우하단이 n,m
    #세로,가로  -> 2.3이 S
    diff = abs(x-r)+abs(y-c)
    if diff%2!=k%2 or diff>k:
        return 'impossible'
    #dlru 순서

    rest = k-diff
    lcount = 0
    rcount = 0
    dcount = 0
    ucount = 0
    if x<r : #내려가야함
        dcount = r-x
    else:
        ucount = x-r
    if y<c :
        rcount = c-y
    else:
        lcount = y-c

    dplus = min( n-max(x,r), rest//2)
    rest -= dplus*2

    lplus = min( min(y,c)-1, rest//2)
    rest -= lplus*2

    answer = 'd'*(dcount+dplus)+'l'*(lcount+lplus)+'rl'*(rest//2)+'r'*(rcount+lplus)+'u'*(dplus+ucount)
    print(lcount,lplus,rcount,rest)


    return answer