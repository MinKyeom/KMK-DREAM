# 내 풀이
def solution(nums):
    from itertools import combinations
    k = int(len(nums) / 2)
    x = list(set(nums))

    if len(x) >= k:
        return k
    else:
        return len(x)


# 다른 사람 풀이
def solution(ls):
    return min(len(ls)/2, len(set(ls)))