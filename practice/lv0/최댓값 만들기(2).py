# 내 풀이
def solution(numbers):
    from itertools import combinations
    num=[]
    for x,y in list(combinations(numbers,2)):
        num.append(x*y)
    return max(num)


# 다른 사람 풀이
def solution(numbers):
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2])