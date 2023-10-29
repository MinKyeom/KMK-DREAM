# 내 풀이(개선 중)
def solution(rows, columns, queries):
    from collections import deque
    result = []
    map = [[False] * columns for a in range(rows)]
    count = 1

    # 기본 맵
    for a in range(rows):
        for b in range(columns):
            map[a][b] = count
            count += 1

    # 맵 모양 변경
    for c in queries:
        num_list = []
        check = map.copy()
        four = c.pop()
        three = c.pop()
        two = c.pop()
        one = c.pop()

        # 맨 윗줄

        for d in range(two - 2, four - 2):
            check[one - 1][d] = map[one - 1][d + 1]

        # 맨 오른쪽

        for e in range(one - 2, three - 2):
            check[e][four - 1] = map[e + 1][four - 1]
            print(check[e][four - 1])
        print("확")
        # 맨 아랫줄

        for f in range(four - 2, two - 2, -1):
            check[three - 1][f] = map[three - 1][f + 1]
            print(map[three - 1][f], f, three - 1)
        print("인")

    answer = []
    return answer

# 다른 사람 풀이
