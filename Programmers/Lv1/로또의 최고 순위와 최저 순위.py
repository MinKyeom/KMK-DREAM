# 내 풀이
def solution(lottos, win_nums):
    x = len(set(lottos) & set(win_nums))
    y = lottos.count(0)
    if x == 0 and y == 0:
        return [6 - (x + y), 6 - x]
    elif x != 0 and y == 0:
        return [7 - (x + y), 7 - x]
    elif x == 0 and y != 0:
        return [7 - (x + y), 6 - x]

    return [7 - (x + y), 7 - x]

# 다른 사람 풀이
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]