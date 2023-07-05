# 내 풀이
def solution(ingredient):
    k = []
    count = 0
    for x in ingredient:
        k.append(x)
        print(k[-4:])
        if k[-4:] == [1, 2, 3, 1]:
            count += 1
            for y in range(4):
                k.pop()

    return count
# 다른 사람 풀이
def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for i in range(4):
                s.pop()
    return cnt